# cube.fits

**Source**: rust-fitsio test suite (https://github.com/simonrw/rust-fitsio, `testdata/cube.fits`; byte-identical to the upstream copy)

**Description**: Minimal 3D image cube used to test reading multi-dimensional
image data. Contains a small 64-bit integer data cube with three axes.

**HDU structure**:
- HDU 0: Primary image (BITPIX=64, NAXIS1 × NAXIS2 × NAXIS3 = 6 × 3 × 2 = 36 pixels; values 0..35 in file order)

**FITS features exercised**:
- 3D image (NAXIS=3) for cube/volume data access
- 64-bit integer pixel type (BITPIX=64)
- Small dimensions suitable for exact value verification in tests
- Single-HDU file with minimal header

**File size**: 5760 bytes (5.6 KB)
