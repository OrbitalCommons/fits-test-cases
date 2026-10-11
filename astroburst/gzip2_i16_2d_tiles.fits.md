# gzip2_i16_2d_tiles.fits

**Source**: [AstroBurst](https://github.com/samuelkriegerbonini-dev/AstroBurst) test fixtures, `src-tauri/tests/fixtures/fits_compressed/gzip2_i16_2d_tiles.fits`, added in commit [`b11aa9a`](https://github.com/samuelkriegerbonini-dev/AstroBurst/commit/b11aa9a3c853334f4b8732a5f75542922dd228cb) (2026-07-05) with the tile-compressed reader contributed by Jae-Joon Lee ([@leejjoon](https://github.com/leejjoon)). Written with astropy.

**License**: AGPL-3.0-or-later, as AstroBurst. Copyright Samuel Krieger Bonini and AstroBurst contributors.

**Description**: GZIP_2, 16-bit integers, 6×16 two-dimensional tiles. The image is a synthetic 37 × 23 test pattern (decoded 2 to 30000).

`gzip2_i16_2d_tiles.expected` holds astropy 8.0.1's decode of the image as little-endian `float64`, row-major (23 rows of 37), so a reader can be checked without astropy.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 1 col x 14 rows | COMPRESSED_IMAGE | `GZIP_2` tile-compressed image, decompressed 37 x 23, `ZBITPIX = 16` |

Columns: `COMPRESSED_DATA` (1PB(126)).

## FITS Features Exercised

- `GZIP_2` (bytes shuffled by significance before DEFLATE)
- Two-dimensional tiles (`ZTILE1 = 6`, `ZTILE2 = 16`) that do not divide the image: edge tiles are clipped, 14 tiles in all
- Lossless 16-bit integer image

**File size**: 8,640 bytes (8.4 KB); `.expected` 6,808 bytes
