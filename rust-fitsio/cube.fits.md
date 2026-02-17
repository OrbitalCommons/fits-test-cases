# cube.fits

**Source**: rust-fitsio test suite (https://github.com/simonrw/rust-fitsio)

**Description**: Minimal 3D image cube used to test reading multi-dimensional
image data. Contains a small 64-bit integer data cube with three axes.

**HDU structure**:
- HDU 0: Primary image (BITPIX=64, 6x3x2 = 36 pixels)

**FITS features exercised**:
- 3D image (NAXIS=3) for cube/volume data access
- 64-bit integer pixel type (BITPIX=64)
- Small dimensions suitable for exact value verification in tests
- Single-HDU file with minimal header

**File size**: 5760 bytes (5.6 KB)
