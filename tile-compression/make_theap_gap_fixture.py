"""Write fpack_rice_u16_theap_gap.fits from fpack_rice_u16.fits: the same
RICE_1 image with a 100-byte gap of junk (0xFF) between the table's rows and
its heap, which `THEAP` skips (PCOUNT grows by the gap). No standard writer
leaves such a gap; the FITS standard allows one. The table HDU's CHECKSUM and
DATASUM cards are dropped, since its bytes change. The gap is small enough
that THEAP + PCOUNT stays within the padded data unit, so readers that take
PCOUNT as the heap size from THEAP (astropy 8.0.3, fitsverify 4.6.4) still
read it; FITS 4.0 Sect. 7.3.5 counts the gap in PCOUNT. Standard library only.

With `heap-only`, PCOUNT is left as the heap's size, as astropy and fitsverify
read it, rather than grown by the gap as the standard has it: that writes
fpack_rice_u16_theap_gap_heap_pcount.fits, whose heap ends 100 bytes past the
data unit the standard computes, in its block padding.

Usage: make_theap_gap_fixture.py <fpack_rice_u16.fits> <output> [heap-only]"""
import sys

BLOCK, CARD, GAP = 2880, 80, 100
src = open(sys.argv[1], "rb").read()
heap_only = sys.argv[3:] == ["heap-only"]

def header_end(start):
    i = start
    while not src[i:i + CARD].startswith(b"END" + b" " * 5):
        i += CARD
    return start + -(-(i + CARD - start) // BLOCK) * BLOCK

def value(cards, key):
    return int(next(c for c in cards if c[:8].rstrip() == key)[10:30])

primary_end = header_end(0)
data_start = header_end(primary_end)
cards = [src[i:i + CARD] for i in range(primary_end, data_start, CARD)]
cards = [c for c in cards if c.strip()]
naxis1, naxis2, pcount = value(cards, b"NAXIS1"), value(cards, b"NAXIS2"), value(cards, b"PCOUNT")
rows = naxis1 * naxis2

def card(key, v, comment):
    return f"{key:<8}= {v:>20} / {comment}".ljust(CARD).encode()

out = []
for c in cards:
    key = c[:8].rstrip()
    if key in (b"CHECKSUM", b"DATASUM"):
        continue
    if key == b"PCOUNT" and not heap_only:
        c = card("PCOUNT", pcount + GAP, "size of special data area")
    out.append(c)
    if key == b"TFORM1":
        out.append(card("THEAP", rows + GAP, "heap starts after a gap past the rows"))
header = b"".join(out)
header += b" " * (-len(header) % BLOCK)

data = src[data_start:data_start + rows + pcount]
data = data[:rows] + b"\xff" * GAP + data[rows:]
data += b"\0" * (-len(data) % BLOCK)
open(sys.argv[2], "wb").write(src[:primary_end] + header + data)
