# vari.fits

**Source**: HEASARC cfitsio test suite (https://github.com/HEASARC/cfitsio)

**Description**: Test file with a binary table named COMPRESSED_IMAGE that has
columns with single-letter and numeric names. Despite the EXTNAME, this is a
plain BINTABLE (not a tile-compressed image). Used to test column name handling
and table reading edge cases.

**HDU structure**:
- HDU 0: Primary (BITPIX=16, NAXIS=0, empty)
- HDU 1: BINTABLE "COMPRESSED_IMAGE" -- 7 columns (a/1E, 2/1E, c/1E, 4/1E, e/1E, COMPRESSED_DATA/1E, g/1E), 91 rows

**FITS features exercised**:
- Column names that are single characters or digits (a, 2, c, 4, e, g)
- Column named COMPRESSED_DATA alongside non-standard column names
- EXTNAME of COMPRESSED_IMAGE on a non-compressed binary table
- All float (1E) columns with uniform format

**File size**: 8640 bytes (8.4 KB)
