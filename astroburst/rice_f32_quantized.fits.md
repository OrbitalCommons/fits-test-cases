# rice_f32_quantized.fits

**Source**: [AstroBurst](https://github.com/samuelkriegerbonini-dev/AstroBurst) test fixtures, `src-tauri/tests/fixtures/fits_compressed/rice_f32_quantized.fits`, added in commit [`b11aa9a`](https://github.com/samuelkriegerbonini-dev/AstroBurst/commit/b11aa9a3c853334f4b8732a5f75542922dd228cb) (2026-07-05) with the tile-compressed reader contributed by Jae-Joon Lee ([@leejjoon](https://github.com/leejjoon)). Written with astropy.

**License**: AGPL-3.0-or-later, as AstroBurst. Copyright Samuel Krieger Bonini and AstroBurst contributors.

**Description**: RICE_1, 32-bit float quantized to integers per tile with `NO_DITHER`. The image is a synthetic 37 × 23 test pattern (decoded -1000.49 to 996.948).

`rice_f32_quantized.expected` holds astropy 8.0.1's decode of the image as little-endian `float64`, row-major (23 rows of 37), so a reader can be checked without astropy.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 4 cols x 23 rows | COMPRESSED_IMAGE | `RICE_1` tile-compressed image, decompressed 37 x 23, `ZBITPIX = -32` |

Columns: `COMPRESSED_DATA` (1PB(59)), `GZIP_COMPRESSED_DATA` (1PB(0)), `ZSCALE` (1D), `ZZERO` (1D).

## FITS Features Exercised

- `RICE_1` on quantized floats (`ZBITPIX = -32`, `BYTEPIX = 4`)
- `ZQUANTIZ = 'NO_DITHER'`: values are `ZZERO + ZSCALE * q`, no dither
- Per-tile `ZSCALE` and `ZZERO` columns (`1D`)
- An empty `GZIP_COMPRESSED_DATA` column alongside `COMPRESSED_DATA`, as cfitsio writes it; no tile uses it

**File size**: 8,640 bytes (8.4 KB); `.expected` 6,808 bytes
