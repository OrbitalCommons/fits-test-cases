"""Write theap_gap.fits byte by byte: an empty primary HDU and a one-row
BINTABLE with a `1PJ` column whose heap starts 100 bytes after the row
(THEAP = 108; PCOUNT = 112, the 100-byte gap plus the 12-byte heap). The
cell holds [7, 8, 9]. No standard writer leaves such a gap; the FITS standard
allows one (FITS 4.0 Sect. 7.3.5). Standard library only.
Usage: make_theap_gap_table.py <output>"""
import struct, sys

def header(cards):
    text = "".join(c.ljust(80) for c in cards + ["END"])
    return (text + " " * (-len(text) % 2880)).encode()

def card(key, value):
    return f"{key:<8}= {value:>20}"

primary = header([card("SIMPLE", "T"), card("BITPIX", 8), card("NAXIS", 0)])
table = header([
    "XTENSION= 'BINTABLE'", card("BITPIX", 8), card("NAXIS", 2),
    card("NAXIS1", 8), card("NAXIS2", 1), card("PCOUNT", 112), card("GCOUNT", 1),
    card("TFIELDS", 1), "TTYPE1  = 'V'", "TFORM1  = 'PJ(3)'", card("THEAP", 108),
])
data = struct.pack(">ii", 3, 0) + bytes(100) + struct.pack(">iii", 7, 8, 9)
data += bytes(-len(data) % 2880)
open(sys.argv[1], "wb").write(primary + table + data)
