# hyper.fits

**Source**: rust-fitsio test suite (https://github.com/simonrw/rust-fitsio, `testdata/hyper.fits`; byte-identical to the upstream copy)

**Description**: Minimal 4D hypercube image used to test reading higher-dimensional
image data beyond the typical 2D/3D cases.

**HDU structure**:
- HDU 0: Primary image (BITPIX=64, NAXIS1 × NAXIS2 × NAXIS3 × NAXIS4 = 2 × 3 × 3 × 2 = 36 pixels; values 0..35 in file order)

**FITS features exercised**:
- 4D image (NAXIS=4) for hypercube data access
- 64-bit integer pixel type (BITPIX=64)
- Small dimensions suitable for exact value verification in tests
- Tests NAXIS > 3 handling which many readers may not support
- Single-HDU file with minimal header

**File size**: 5760 bytes (5.6 KB)
