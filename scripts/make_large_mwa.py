#!/usr/bin/env python3
"""Write large MWA-shaped FITS files for testing seek-based reads and writes.

These are too large to keep in the repository, so they are generated on
demand. Output is deterministic: the same arguments always give the same
bytes (the checksums of the default outputs are in mwa-large/README.md).

    python3 scripts/make_large_mwa.py uvfits OUT.uvfits [--timesteps 8] [--chans 768]
    python3 scripts/make_large_mwa.py mwaf OUT.mwaf [--timesteps 2720] [--chans 768]

OUT may be `-` to stream to stdout, e.g. to checksum without a disk copy:

    python3 scripts/make_large_mwa.py uvfits - | sha256sum

uvfits: a random-groups primary HDU in the layout cotter and Birli write
(PCOUNT = 5: UU, VV, WW, BASELINE, DATE; data axes COMPLEX(3) x STOKES(4) x
FREQ x RA x DEC, float32) for 128 tiles, 8256 baselines including autos per
timestep, then an `AIPS AN` binary table of 128 rows. The defaults give
66,048 groups and a 2.44 GB file, so the AN table starts past byte 2^31.

mwaf: a Birli-style flag file: an empty primary with the mwaf keys, a
`FLAGS` binary table with one `<chans>X` bit column and one row per
baseline per timestep (8256 x timesteps rows), then an `OCCUPANCY` table
with the flagged fraction of each channel. The defaults give 22,456,320 rows
and a 2.16 GB file.

Every value follows from its indices (formulas below), so a reader can check
any element without a reference copy. Needs only numpy.
"""
import argparse
import hashlib
import sys

import numpy as np

BLOCK = 2880
TILES = 128
BASELINES = TILES * (TILES + 1) // 2  # 8256, autos included
OBSID = 1090008640
JD0 = 2456860.5  # PZERO5: midnight UTC before OBSID's GPS time
INTTIME = 2.0


def card(key, value=None, comment=None):
    """One 80-character header card in fixed format."""
    if value is None:
        text = f"{key:<8}" + (f"{comment}" if comment else "")
    else:
        if isinstance(value, bool):
            v = f"{'T' if value else 'F':>20}"
        elif isinstance(value, str):
            v = "'" + value.replace("'", "''").ljust(8) + "'"
            v = f"{v:<20}"
        elif isinstance(value, int):
            v = f"{value:>20}"
        else:
            v = f"{value!r:>20}".upper()
        text = f"{key:<8}= {v}" + (f" / {comment}" if comment else "")
    if len(text) > 80:
        raise ValueError(f"card too long: {text}")
    return text.ljust(80).encode("ascii")


def header(cards):
    data = b"".join(cards) + b"END".ljust(80)
    return data + b" " * (-len(data) % BLOCK)


def pad(n):
    return b"\0" * (-n % BLOCK)


def baselines():
    """Antenna pairs (0-based) in cotter/Birli order: a1 <= a2, a1 major."""
    a1, a2 = np.triu_indices(TILES)
    return a1, a2


class Out:
    """A file or stdout, with a running SHA-256 and byte count."""

    def __init__(self, path):
        self.f = sys.stdout.buffer if path == "-" else open(path, "wb")
        self.close_f = path != "-"
        self.sha = hashlib.sha256()
        self.n = 0

    def write(self, b):
        self.f.write(b)
        self.sha.update(b)
        self.n += len(b)

    def close(self):
        if self.close_f:
            self.f.close()
        print(f"{self.n} bytes, sha256 {self.sha.hexdigest()}", file=sys.stderr)


def uvfits(out, timesteps, chans):
    ngroups = BASELINES * timesteps
    cards = [
        card("SIMPLE", True, "file does conform to FITS standard"),
        card("BITPIX", -32, "number of bits per data pixel"),
        card("NAXIS", 6, "number of data axes"),
        card("NAXIS1", 0, "length of data axis 1"),
        card("NAXIS2", 3, "length of data axis 2"),
        card("NAXIS3", 4, "length of data axis 3"),
        card("NAXIS4", chans, "length of data axis 4"),
        card("NAXIS5", 1, "length of data axis 5"),
        card("NAXIS6", 1, "length of data axis 6"),
        card("EXTEND", True, "FITS dataset may contain extensions"),
        card("GROUPS", True, "random group records are present"),
        card("PCOUNT", 5, "number of random group parameters"),
        card("GCOUNT", ngroups, "number of random groups"),
        card("BSCALE", 1.0),
    ]
    for i, name in enumerate(["UU", "VV", "WW", "BASELINE", "DATE"], 1):
        cards += [card(f"PTYPE{i}", name), card(f"PSCAL{i}", 1.0), card(f"PZERO{i}", JD0 if name == "DATE" else 0.0)]
    cards += [
        card("DATE-OBS", "2014-07-21T00:00:00.0"),
        card("CTYPE2", "COMPLEX"), card("CRVAL2", 1.0), card("CRPIX2", 1.0), card("CDELT2", 1.0),
        card("CTYPE3", "STOKES"), card("CRVAL3", -5.0), card("CDELT3", -1.0), card("CRPIX3", 1.0),
        card("CTYPE4", "FREQ"), card("CRVAL4", 167.035e6), card("CDELT4", 40e3), card("CRPIX4", 1.0),
        card("CTYPE5", "RA"), card("CRVAL5", 0.0), card("CRPIX5", 1.0), card("CDELT5", 1.0),
        card("CTYPE6", "DEC"), card("CRVAL6", -27.0), card("CRPIX6", 1.0), card("CDELT6", 1.0),
        card("OBSRA", 0.0), card("OBSDEC", -27.0), card("EPOCH", 2000.0),
        card("OBJECT", "synthetic"), card("TELESCOP", "MWA"), card("INSTRUME", "MWA"),
        card("HISTORY", None, "AIPS WTSCAL =  1.0"),
        card("COMMENT", None, "Synthetic: written by fits-test-cases scripts/make_large_mwa.py"),
    ]
    out.write(header(cards))

    a1, a2 = baselines()
    gsize = 5 + 3 * 4 * chans
    chan = np.arange(chans, dtype=np.float32)
    pol = np.arange(4, dtype=np.float32)
    chunk = 1032  # baselines per write; 8256 = 8 x 1032
    for t in range(timesteps):
        date = np.float32((t + 0.5) * INTTIME / 86400.0)
        for s in range(0, BASELINES, chunk):
            b = np.arange(s, min(s + chunk, BASELINES))
            g = np.empty((len(b), gsize), dtype=">f4")
            # UU, VV, WW in seconds of light travel: tile offsets of 10, -5
            # and 0.5 m per tile number, divided by c.
            d = (a2[b] - a1[b]).astype(np.float64)
            g[:, 0] = d * 10.0 / 299792458.0
            g[:, 1] = d * -5.0 / 299792458.0 + 0.0  # + 0.0: no negative zero
            g[:, 2] = d * 0.5 / 299792458.0
            g[:, 3] = 256 * (a1[b] + 1) + (a2[b] + 1)
            g[:, 4] = date
            # Data [chan][pol][re, im, weight]: re = group index mod 65536
            # plus pol, im = channel, weight = 1 (-1 on channels 0 and 1
            # of every 32, as flagged edge channels).
            group = t * BASELINES + b
            vis = g[:, 5:].reshape(len(b), chans, 4, 3)
            vis[..., 0] = (group % 65536)[:, None, None].astype(np.float32) + pol[None, None, :]
            vis[..., 1] = chan[None, :, None]
            vis[..., 2] = np.where((np.arange(chans) % 32 < 2), -1.0, 1.0)[None, :, None]
            out.write(g.tobytes())
    out.write(pad(ngroups * gsize * 4))

    # AIPS AN table, as cotter writes it.
    cols = [("ANNAME", "8A", None), ("STABXYZ", "3D", "METERS"), ("NOSTA", "1J", None),
            ("MNTSTA", "1J", None), ("STAXOF", "1E", "METERS"), ("POLTYA", "1A", None),
            ("POLAA", "1E", "DEGREES"), ("POLCALA", "3E", None), ("POLTYB", "1A", None),
            ("POLAB", "1E", "DEGREES"), ("POLCALB", "3E", None)]
    row = np.dtype([("ANNAME", "S8"), ("STABXYZ", ">f8", 3), ("NOSTA", ">i4"), ("MNTSTA", ">i4"),
                    ("STAXOF", ">f4"), ("POLTYA", "S1"), ("POLAA", ">f4"), ("POLCALA", ">f4", 3),
                    ("POLTYB", "S1"), ("POLAB", ">f4"), ("POLCALB", ">f4", 3)])
    an = np.zeros(TILES, dtype=row)
    i = np.arange(TILES)
    an["ANNAME"] = [f"Tile{k:03d}".encode() for k in i]
    an["STABXYZ"] = np.stack([i * 10.0, i * -5.0 + 0.0, i * 0.5], axis=1)
    an["NOSTA"] = i + 1
    an["POLTYA"] = b"X"
    an["POLTYB"] = b"Y"
    cards = [
        card("XTENSION", "BINTABLE", "binary table extension"),
        card("BITPIX", 8, "8-bit bytes"),
        card("NAXIS", 2, "2-dimensional binary table"),
        card("NAXIS1", row.itemsize, "width of table in bytes"),
        card("NAXIS2", TILES, "number of rows in table"),
        card("PCOUNT", 0, "size of special data area"),
        card("GCOUNT", 1, "one data group (required keyword)"),
        card("TFIELDS", len(cols), "number of fields in each row"),
    ]
    for k, (name, form, unit) in enumerate(cols, 1):
        cards += [card(f"TTYPE{k}", name), card(f"TFORM{k}", form)]
        if unit:
            cards.append(card(f"TUNIT{k}", unit))
    cards += [
        card("EXTNAME", "AIPS AN", "name of this binary table extension"),
        card("ARRAYX", -2559453.29059553), card("ARRAYY", 5095371.73544116), card("ARRAYZ", -2849056.77357178),
        card("FREQ", 167.035e6), card("RDATE", "2014-07-21T00:00:00.0"), card("TIMSYS", "UTC"),
        card("ARRNAM", "MWA"), card("NOPCAL", 3), card("FREQID", -1), card("IATUTC", 35.0),
    ]
    out.write(header(cards))
    out.write(an.tobytes())
    out.write(pad(an.nbytes))


def mwaf(out, timesteps, chans):
    rows = BASELINES * timesteps
    rowbytes = (chans + 7) // 8
    cards = [
        card("SIMPLE", True, "file does conform to FITS standard"),
        card("BITPIX", 8, "number of bits per data pixel"),
        card("NAXIS", 0, "number of data axes"),
        card("EXTEND", True, "FITS dataset may contain extensions"),
        card("VERSION", "2.0"),
        card("OBSID", OBSID),
        card("GPSSTART", f"{OBSID}.0"),
        card("NCHANS", chans),
        card("NANTENNA", TILES),
        card("NSCANS", timesteps),
        card("NPOLS", 1),
        card("GPUBOXNO", 1),
        card("SOFTWARE", "make_large_mwa.py"),
        card("COMMENT", None, "Synthetic: written by fits-test-cases scripts/make_large_mwa.py"),
    ]
    out.write(header(cards))
    cards = [
        card("XTENSION", "BINTABLE", "binary table extension"),
        card("BITPIX", 8, "8-bit bytes"),
        card("NAXIS", 2, "2-dimensional binary table"),
        card("NAXIS1", rowbytes, "width of table in bytes"),
        card("NAXIS2", rows, "number of rows in table"),
        card("PCOUNT", 0, "size of special data area"),
        card("GCOUNT", 1, "one data group (required keyword)"),
        card("TFIELDS", 1, "number of fields in each row"),
        card("TTYPE1", "FLAGS", "label for field   1"),
        card("TFORM1", f"{chans}X", "data format of field: BIT"),
        card("EXTNAME", "FLAGS", "name of this binary table extension"),
    ]
    out.write(header(cards))

    # Bit (row r, channel c) is set when c mod 32 is 0, 1, 16, 30 or 31 (edge
    # and centre channels of each 40 kHz coarse channel) or when
    # (31 r + 17 c) mod 101 == 0. Bits are packed most significant first.
    c = np.arange(chans)
    edge = np.isin(c % 32, [0, 1, 16, 30, 31])
    counts = np.zeros(chans, dtype=np.int64)
    for t in range(timesteps):
        r = t * BASELINES + np.arange(BASELINES, dtype=np.int64)
        bits = edge[None, :] | (((31 * r[:, None]) + 17 * c[None, :]) % 101 == 0)
        counts += bits.sum(axis=0)
        out.write(np.packbits(bits, axis=1).tobytes())
    out.write(pad(rows * rowbytes))

    occ = np.zeros(chans, dtype=[("Index", ">i4"), ("Count", ">i8"), ("Occupancy", ">f8")])
    occ["Index"] = c
    occ["Count"] = counts
    occ["Occupancy"] = counts / rows
    cards = [
        card("XTENSION", "BINTABLE", "binary table extension"),
        card("BITPIX", 8, "8-bit bytes"),
        card("NAXIS", 2, "2-dimensional binary table"),
        card("NAXIS1", occ.itemsize, "width of table in bytes"),
        card("NAXIS2", chans, "number of rows in table"),
        card("PCOUNT", 0, "size of special data area"),
        card("GCOUNT", 1, "one data group (required keyword)"),
        card("TFIELDS", 3, "number of fields in each row"),
        card("TTYPE1", "Index"), card("TFORM1", "1J"),
        card("TTYPE2", "Count"), card("TFORM2", "1K"),
        card("TTYPE3", "Occupancy"), card("TFORM3", "1D"),
        card("EXTNAME", "OCCUPANCY", "name of this binary table extension"),
    ]
    out.write(header(cards))
    out.write(occ.tobytes())
    out.write(pad(occ.nbytes))


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("kind", choices=["uvfits", "mwaf"])
    p.add_argument("out", help="output path, or - for stdout")
    p.add_argument("--timesteps", type=int, help="default 8 (uvfits) or 2720 (mwaf)")
    p.add_argument("--chans", type=int, default=768)
    a = p.parse_args()
    out = Out(a.out)
    if a.kind == "uvfits":
        uvfits(out, a.timesteps or 8, a.chans)
    else:
        mwaf(out, a.timesteps or 2720, a.chans)
    out.close()


if __name__ == "__main__":
    main()
