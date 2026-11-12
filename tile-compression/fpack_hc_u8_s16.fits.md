# fpack_hc_u8_s16.fits

**Source**: Generated for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure)'s tile-decompression tests by `make_fpack_fixtures.sh` in this directory: `fpack_originals.c` writes `u8_stars.fits`, and the reference `fpack` from CFITSIO 4.6.4 compresses it with `fpack -h -s 16`. Synthetic data, not from an instrument.

**License**: Apache-2.0, as fitsio-pure.

**Description**: `uint8`, background 20 with saturated stars clipped at 255, 64 × 64. Five Gaussian stars with peaks far above the range give flat saturated cores, as in real frames.

Lossy decoding overshoots 255 next to the saturated cores, which cfitsio clips (`fffi4i1`, fitsio-pure#193).

`fpack_hc_u8_s16.expected` holds cfitsio 4.6.4's decode of the image as little-endian `float64`, row-major (64 rows of 64), written by `fpack_expected.c`. That is cfitsio's 32-bit decode clipped to the image type's range, as `fffi4i2`/`fffi4i1` clip it. Where `funpack` 4.6.4 can decode the file, its output is identical. (`funpack` fails on lossy `uint8`, and reading lossy `uint16`/`uint8` HCOMPRESS as `TUSHORT`/`TBYTE` fails with `NUM_OVERFLOW`: cfitsio only ignores the overflow for `TSHORT` reads.) The maximum |error| of the decode against the original is 47.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 1 col x 4 rows | COMPRESSED_IMAGE | `HCOMPRESS_1` with `SCALE = 16` (lossy) tile-compressed image, decompressed 64 x 64 |

## FITS Features Exercised

- `HCOMPRESS_1` with `SCALE = 16` (lossy), `ZBITPIX = 8`
- Tiles `64 × 16`: 4 tiles, fpack's default for HCOMPRESS
- Written by the reference `fpack`, not by the reader under test, so a bug symmetric in a writer and reader still shows

**File size**: 8,640 bytes; `.expected` 32,768 bytes
