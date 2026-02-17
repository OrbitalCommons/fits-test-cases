# boolean_columns.fits

**Source**: rust-fitsio test suite (https://github.com/simonrw/rust-fitsio)

**Description**: MWA (Murchison Widefield Array) radio telescope metadata file
used to test reading binary tables with logical/boolean columns. Contains
tile configuration data including a Whitening_Filter boolean column.

**HDU structure**:
- HDU 0: Primary (BITPIX=8, NAXIS=0, empty, rich observation metadata)
- HDU 1: BINTABLE "TILEDATA" -- 21 columns, 256 rows (254 bytes/row)

**FITS features exercised**:
- Logical column type (L format) for Whitening_Filter
- Wide table with many column types (I, A, E, L)
- Vector columns (24I for Gains, 16I for Delays, 24E for Calib_Gains)
- CONTINUE long string convention for CHANNELS keyword
- Extensive primary header with astronomy metadata (WCS, timing, pointing)
- Real-world MWA radio astronomy observation metadata

**File size**: 77760 bytes (75.9 KB)
