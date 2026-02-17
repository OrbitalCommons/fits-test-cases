# iter_c.fit

**Source**: HEASARC cfitsio test suite (https://github.com/HEASARC/cfitsio)

**Description**: Iterator test file for cfitsio's iterator API. Contains a ROSAT
PSPC X-ray event list with spatial coordinates, energy, and timing columns.
Used to test iterator processing on real-world X-ray astronomy event data.

**HDU structure**:
- HDU 0: Primary (BITPIX=32, NAXIS=0, empty)
- HDU 1: BINTABLE "EVENTS" -- 5 columns (X/1I, Y/1I, PHA/1I, TIME/1D, DY/1I), 5000 rows

**FITS features exercised**:
- Mixed integer and double-precision columns
- Full WCS keywords (CTYPE, CRVAL, CDELT, CRPIX, CROTA2)
- ROSAT PSPC observation metadata (TELESCOP, INSTRUME)
- TLMIN/TLMAX column range keywords
- Extensive HIERARCH-style XS- mission-specific keywords
- EXTVER extension versioning

**File size**: 92160 bytes (90.0 KB)
