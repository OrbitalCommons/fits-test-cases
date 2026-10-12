# ushort.fits

**Source**: rust-fitsio test suite (https://github.com/simonrw/rust-fitsio, `testdata/ushort.fits`; byte-identical to the upstream copy)

**Description**: 2D image using the BZERO=32768 convention to store unsigned
16-bit integer data in a signed 16-bit FITS image. Used to test correct handling
of the BZERO/BSCALE unsigned short encoding. Every stored value is -32768, so every
physical pixel is 0; rust-fitsio's `test_ushort.rs` only checks that the image
type is detected as unsigned short.

**HDU structure**:
- HDU 0: Primary image (BITPIX=16, 1024x1024 = 1048576 pixels)

**FITS features exercised**:
- Unsigned short encoding via BZERO=32768 and BSCALE=1.0
- Physical values require: real = BZERO + BSCALE * stored_value
- Constant data: the pixel values carry no test signal
- 16-bit integer pixel type (BITPIX=16)
- Single-HDU file

**File size**: 2102400 bytes (2.0 MB)
