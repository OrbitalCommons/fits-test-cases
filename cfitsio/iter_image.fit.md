# iter_image.fit

**Source**: HEASARC cfitsio test suite (https://github.com/HEASARC/cfitsio)

**Description**: Iterator test file for cfitsio's iterator API. Contains a 2D
integer image from the LBT LUCI1 near-infrared instrument, used to test
iterator-based pixel processing on image HDUs.

**HDU structure**:
- HDU 0: Primary image (BITPIX=32, 113x91 pixels)

**FITS features exercised**:
- Single-HDU 2D image (no extensions)
- BSCALE/BZERO scaling keywords
- BUNIT physical unit annotation ("adu")
- HIERARCH long keyword convention (LBTO LUCI detector parameters)
- WCS alternate frame keywords (CUNIT1A, CRVAL1A, CD matrix)
- CHECKSUM/DATASUM data integrity keywords
- DETSEC/DETSIZE detector section keywords
- BLANK keyword for undefined integer pixels

**File size**: 54720 bytes (53.4 KB)
