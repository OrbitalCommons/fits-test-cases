# iter_c.fit

**Source**: HEASARC cfitsio test suite (https://github.com/HEASARC/cfitsio, `iter_c.fit` at the repo root; read by the `iter_c.c` and `iter_c.f` example programs)

**Description**: Iterator test file for cfitsio's iterator API. Contains a ROSAT
PSPC X-ray event list with spatial coordinates, energy, and timing columns.
Used to test iterator processing on real-world X-ray astronomy event data;
`iter_c.c` bins the X and Y columns into a 2D histogram image.

**HDU structure**:
- HDU 0: Primary (BITPIX=32, NAXIS=0, empty)
- HDU 1: BINTABLE "EVENTS" -- 5 columns (X/1I, Y/1I, PHA/1I, TIME/1D, DY/1I), 5000 rows

**FITS features exercised**:
- Mixed integer and double-precision columns
- Full WCS keywords (CTYPE, CRVAL, CDELT, CRPIX, CROTA2)
- ROSAT PSPC observation metadata (TELESCOP, INSTRUME)
- TLMIN/TLMAX column range keywords (X and Y only, 1..15360)
- Extensive XS- mission-specific keywords (standard 8-character keywords containing a hyphen, e.g. XS-OBSID, XS-LIVTI; not HIERARCH)
- EXTVER extension versioning
- Non-standard header layout: EXTNAME/EXTVER come before the TFORMn/TTYPEn cards, and TFORMn precedes TTYPEn
- Legacy DD/MM/YY date strings (DATE-OBS = '08/03/93', DATE-END = '11/03/93')
- QPOE axis keywords (NAXLEN, AXLEN1, AXLEN2)
- TDISP4 = 'I12' (integer display format) on the double-precision TIME column

**File size**: 92160 bytes (90.0 KB)
