# u16_none.fits.gz

**Source**: `gzip -9n` of [`refimage/u16_none.fits`](../refimage/u16_none.fits.md) (written by refimage 1.0.0-pre6), made for the port of [cool-japan/scirs](https://github.com/cool-japan/scirs)'s FITS module onto [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure). It decompresses to `refimage/u16_none.fits` byte for byte (SHA-256 `f4f613df66919d3ee3c5faf475f6a4fb897954024e9ef81bfe16521ec8a25cbb`). `-n` leaves the name and timestamp out, so it is reproducible.

**License**: MIT OR Apache-2.0, as refimage.

**Description**: A gzip-compressed whole FITS file (`.fits.gz`), as cfitsio opens transparently: the `uint16` 57 x 23 ramp of `refimage/u16_none.fits`, stored as `int16` with `BZERO = 32768`. `refimage/u16_none.expected` holds its decode.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | 57 x 23 | | `BITPIX = 16` image with refimage metadata cards |

## FITS Features Exercised

- A gzip-compressed file (not tile compression)
- Unsigned 16-bit by `BZERO = 32768`

**File size**: 3,069 bytes (5,760 uncompressed). **SHA-256**: `ae21a15f4136f9f9fad4b9a72ec775aa95787c49311cd9017efa7e7548bc9b4f`
