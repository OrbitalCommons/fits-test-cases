# iter_image.fit

**Source**: HEASARC cfitsio test suite (https://github.com/HEASARC/cfitsio, `iter_image.fit` at the repo root; added in CFITSIO 4.6.4 for the `utilities/iter_image.c` example program)

**Description**: Iterator test file for cfitsio's iterator API. Contains a 2D
integer image from the LBT LUCI1 near-infrared instrument (FILENAME =
'luci1.20251028_0002.fits', DATE-OBS 2025-10-28), used to test
iterator-based pixel processing on image HDUs. `iter_image.c` opens the file
read-write and divides every pixel by 10 in place.

**HDU structure**:
- HDU 0: Primary image (BITPIX=32, NAXIS1 × NAXIS2 = 113 columns × 91 rows; pixel values 107..164)

**FITS features exercised**:
- Single-HDU 2D image (no extensions)
- BSCALE/BZERO scaling keywords (identity values BSCALE = 1., BZERO = 0.; written as reals, so astropy returns float64 rather than int32 unless scaling is disabled)
- BUNIT physical unit annotation ("adu")
- HIERARCH long keyword convention (LBTO LUCI detector parameters)
- WCS alternate frame keywords (CUNIT1A, CRVAL1A, CD matrix)
- CHECKSUM/DATASUM data integrity keywords (both verify)
- DETSEC/DETSIZE detector section keywords
- BLANK keyword (BLANK = 2147483647); no pixel in the file has that value, so it declares undefined pixels without exercising them
- A `COMMENT = 'no comment'` card: COMMENT followed by a value indicator, which the standard treats as commentary text, not a keyword value

**File size**: 54720 bytes (53.4 KB)
