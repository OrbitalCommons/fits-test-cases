# square_array.fits

**Source**: rust-fitsio test suite (https://github.com/simonrw/rust-fitsio)

**Description**: Small 2D square integer image used to test basic image reading
with 32-bit integer pixels.

**HDU structure**:
- HDU 0: Primary image (BITPIX=32, 5x5 = 25 pixels)

**FITS features exercised**:
- Square 2D image (equal NAXIS1 and NAXIS2)
- 32-bit integer pixel type (BITPIX=32)
- Small dimensions for exact pixel value verification
- Single-HDU file with standard header

**File size**: 5760 bytes (5.6 KB)
