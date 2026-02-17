# full_example.fits

**Source**: rust-fitsio test suite (https://github.com/simonrw/rust-fitsio)

**Description**: Multi-extension FITS file combining an image and a binary table,
used to test reading files with multiple HDU types and custom header keywords.

**HDU structure**:
- HDU 0: Primary image (BITPIX=32, 100x100 pixels)
- HDU 1: BINTABLE "TESTEXT" -- 4 columns (intcol/J, floatcol/E, doublecol/D, strcol/7A), 50 rows

**FITS features exercised**:
- Multi-extension file (image + binary table)
- Custom test keywords (TEST, INTTEST, DBLTEST) with string, integer, and float values
- Mixed column types in binary table: integer, float, double, and fixed-width string
- Named extension (EXTNAME) for HDU lookup by name
- 32-bit integer image data

**File size**: 48960 bytes (47.8 KB)
