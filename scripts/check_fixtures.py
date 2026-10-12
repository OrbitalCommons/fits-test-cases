#!/usr/bin/env python3
"""Check every FITS fixture in the repository is structurally intact.

For each tracked FITS file (gzipped files after decompression) it walks the
HDUs the way a reader does: header blocks up to END, then a data unit whose
size follows from BITPIX, NAXISn, PCOUNT and GCOUNT. Every header must start
on a 2880-byte boundary, contain only printable ASCII, and the file must end
exactly where the last data unit's padding ends. It also checks that each
fixture has its `.md` document and that git treats it as binary.

This catches binary files damaged by a text round trip, which change length
and push later HDUs off their block boundaries.

Files in ALLOW_UNPADDED were written without padding after their last data
unit by the tool that made them. They are still walked, and must end exactly
at the end of their data.

Standard library only. Run from anywhere: `python3 scripts/check_fixtures.py`.
"""
import gzip
import os
import subprocess
import sys

BLOCK = 2880
CARD = 80
EXTENSIONS = (".fits", ".fit", ".uvfits", ".metafits", ".fits.gz", ".fit.gz")

ALLOW_UNPADDED = {
    "hips/allsky_panstarrs.fits": "HiPS Allsky.fits as CDS distributes it",
    "hipsgen/Npix8.fits": "Aladin Hipsgen tile",
    "hipsgen/Npix9.fits": "Aladin Hipsgen tile",
    "hipsgen/Npix132.fits": "Aladin Hipsgen tile",
    "hipsgen/Npix133.fits": "Aladin Hipsgen tile",
    "hipsgen/Npix134.fits": "Aladin Hipsgen tile",
    "hipsgen/Npix140.fits": "Aladin Hipsgen tile",
    "hipsgen/Npix4906.fits": "Aladin Hipsgen tile",
    "hipsgen/Npix691539.fits": "Aladin Hipsgen tile",
}


def padded(n):
    return (n + BLOCK - 1) // BLOCK * BLOCK


def integer(cards, key, default=None):
    raw = cards.get(key)
    if raw is None:
        return default
    return int(float(raw.replace("D", "E")))


def read_header(data, start):
    """The header's cards (keyword -> raw value text) and where its data starts."""
    cards = {}
    pos = start
    while True:
        if pos + BLOCK > len(data):
            raise ValueError(f"header at byte {start} has no END")
        block = data[pos:pos + BLOCK]
        if any(b < 0x20 or b > 0x7E for b in block):
            raise ValueError(f"non-ASCII byte in the header block at byte {pos}")
        pos += BLOCK
        for i in range(0, BLOCK, CARD):
            card = block[i:i + CARD].decode("ascii")
            key = card[:8].strip()
            if key == "END":
                return cards, pos
            if card[8:10] == "= ":
                value = card[10:].split("/")[0].strip()
                cards.setdefault(key, value)


def data_size(cards, primary):
    bitpix = integer(cards, "BITPIX")
    naxis = integer(cards, "NAXIS", 0)
    if bitpix is None or abs(bitpix) not in (8, 16, 32, 64):
        raise ValueError(f"bad BITPIX {cards.get('BITPIX')}")
    if naxis == 0:
        return 0
    axes = [integer(cards, f"NAXIS{i}", 0) for i in range(1, naxis + 1)]
    groups = primary and cards.get("GROUPS") == "T" and axes[0] == 0
    count = 1
    for n in axes[1:] if groups else axes:
        count *= n
    pcount = integer(cards, "PCOUNT", 0)
    gcount = integer(cards, "GCOUNT", 1)
    return abs(bitpix) // 8 * gcount * (pcount + count)


def walk(data, allow_unpadded):
    """The number of HDUs, or a ValueError describing the first problem."""
    pos = 0
    hdus = 0
    while pos < len(data):
        if not hdus and not data.startswith(b"SIMPLE  ="):
            raise ValueError("does not start with SIMPLE")
        if hdus and not data[pos:pos + CARD].startswith(b"XTENSION="):
            raise ValueError(f"HDU {hdus} at byte {pos} does not start with XTENSION")
        cards, start = read_header(data, pos)
        size = data_size(cards, primary=hdus == 0)
        end = start + size
        hdus += 1
        if end > len(data):
            raise ValueError(f"HDU {hdus - 1} data runs {end - len(data)} bytes past the end of the file")
        if allow_unpadded and end == len(data):
            return hdus
        pos = start + padded(size)
        if pos > len(data):
            raise ValueError(f"file ends {pos - len(data)} bytes short of the padding after HDU {hdus - 1}")
    if pos != len(data):
        raise ValueError(f"{len(data) - pos} bytes after the last HDU")
    return hdus


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)
    tracked = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.splitlines()
    fixtures = sorted(f for f in tracked if f.lower().endswith(EXTENSIONS))
    binary = subprocess.run(
        ["git", "check-attr", "binary", "--", *fixtures], capture_output=True, text=True, check=True
    ).stdout.splitlines()
    not_binary = {line.split(": ")[0] for line in binary if not line.endswith(": set")}

    failures = []
    for f in fixtures:
        problems = []
        if not os.path.exists(f + ".md"):
            problems.append(f"no {f}.md")
        if f in not_binary:
            problems.append("not marked binary in .gitattributes")
        with open(f, "rb") as fh:
            data = fh.read()
        if f.endswith(".gz"):
            data = gzip.decompress(data)
        try:
            hdus = walk(data, f in ALLOW_UNPADDED)
        except ValueError as e:
            problems.append(str(e))
        if problems:
            failures.append(f)
            for p in problems:
                print(f"FAIL {f}: {p}")
        else:
            note = " (unpadded, allowed)" if f in ALLOW_UNPADDED else ""
            print(f"ok   {f}: {hdus} HDU{'s' if hdus != 1 else ''}{note}")

    stale = sorted(set(ALLOW_UNPADDED) - set(fixtures))
    for f in stale:
        failures.append(f)
        print(f"FAIL {f}: in ALLOW_UNPADDED but not tracked")

    print(f"\n{len(fixtures) - len(failures)}/{len(fixtures)} fixtures intact")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
