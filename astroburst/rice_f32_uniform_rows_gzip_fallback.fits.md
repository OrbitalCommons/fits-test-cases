# rice_f32_uniform_rows_gzip_fallback.fits

**Source**: [AstroBurst](https://github.com/samuelkriegerbonini-dev/AstroBurst) test fixtures, `src-tauri/tests/fixtures/fits_compressed/rice_f32_uniform_rows_gzip_fallback.fits`, added in commit [`b11aa9a`](https://github.com/samuelkriegerbonini-dev/AstroBurst/commit/b11aa9a3c853334f4b8732a5f75542922dd228cb) (2026-07-05) with the tile-compressed reader contributed by Jae-Joon Lee ([@leejjoon](https://github.com/leejjoon)). Written with astropy.

**License**: AGPL-3.0-or-later, as AstroBurst. Copyright Samuel Krieger Bonini and AstroBurst contributors.

**Description**: RICE_1 float image whose rows are each constant, so no tile can be quantized and every tile falls back to lossless GZIP. The image is a synthetic 37 × 23 test pattern (decoded -1581.25 to 1443.75).

`rice_f32_uniform_rows_gzip_fallback.expected` holds astropy 8.0.1's decode of the image as little-endian `float64`, row-major (23 rows of 37), so a reader can be checked without astropy.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 4 cols x 23 rows | COMPRESSED_IMAGE | `RICE_1` tile-compressed image, decompressed 37 x 23, `ZBITPIX = -32` |

Columns: `COMPRESSED_DATA` (1PB(0)), `GZIP_COMPRESSED_DATA` (1PB(27)), `ZSCALE` (1D), `ZZERO` (1D).

## FITS Features Exercised

- Quantization fallback: every one of the 23 tiles has an empty `COMPRESSED_DATA` cell and its pixels stored losslessly in `GZIP_COMPRESSED_DATA`
- A reader must take each tile from whichever column is non-empty, and must not apply `ZSCALE`/`ZZERO` to a fallback tile
- `ZQUANTIZ = 'NO_DITHER'`, `NOISEBIT` (`ZNAME3`/`ZVAL3 = 16.0`)

**File size**: 8,640 bytes (8.4 KB); `.expected` 6,808 bytes
