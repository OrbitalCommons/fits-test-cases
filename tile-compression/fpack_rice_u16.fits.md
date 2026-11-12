# fpack_rice_u16.fits

**Source**: Generated for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure)'s tile-decompression tests by `make_fpack_fixtures.sh` in this directory: `fpack_originals.c` writes `u16_stars.fits`, and the reference `fpack` from CFITSIO 4.6.4 compresses it with `fpack -r`. Synthetic data, not from an instrument.

**License**: Apache-2.0, as fitsio-pure.

**Description**: `uint16` (stored as `int16` with `BZERO = 32768`), background 1000 with saturated stars clipped at 65535, 64 × 64. Five Gaussian stars with peaks far above the range give flat saturated cores, as in real frames.

Control for the HCOMPRESS fixtures: RICE's 16-bit decoding relies on wrapping, so a clip must not reach it.

`fpack_rice_u16.expected` holds cfitsio 4.6.4's decode of the image as little-endian `float64`, row-major (64 rows of 64), written by `fpack_expected.c`. That is cfitsio's 32-bit decode clipped to the image type's range, as `fffi4i2`/`fffi4i1` clip it. Where `funpack` 4.6.4 can decode the file, its output is identical. (`funpack` fails on lossy `uint8`, and reading lossy `uint16`/`uint8` HCOMPRESS as `TUSHORT`/`TBYTE` fails with `NUM_OVERFLOW`: cfitsio only ignores the overflow for `TSHORT` reads.) The maximum |error| of the decode against the original is 0.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 1 col x 64 rows | COMPRESSED_IMAGE | `RICE_1` tile-compressed image, decompressed 64 x 64 |

## FITS Features Exercised

- `RICE_1`, lossless
- Tiles `64 × 1`: 64 tiles (one row each), fpack's default
- Written by the reference `fpack`, not by the reader under test, so a bug symmetric in a writer and reader still shows

**File size**: 14,400 bytes; `.expected` 32,768 bytes
