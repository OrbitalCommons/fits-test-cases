# image.fits

**Source**: rust-fitsio test suite (https://github.com/simonrw/rust-fitsio)

**Description**: Basic 2D image file used as the simplest image test case. Contains
a small square 64-bit integer image with no extensions or special keywords.

**HDU structure**:
- HDU 0: Primary image (BITPIX=64, 6x6 = 36 pixels)

**FITS features exercised**:
- Minimal 2D image (NAXIS=2)
- 64-bit integer pixel type (BITPIX=64)
- Bare-minimum header (SIMPLE, BITPIX, NAXIS, NAXIS1/2, EXTEND)
- Small dimensions for straightforward value validation
- Single-HDU file

**File size**: 5760 bytes (5.6 KB)
