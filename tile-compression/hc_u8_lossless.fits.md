# hc_u8_lossless.fits

**Source**: Generated for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure)'s HCOMPRESS/PLIO decoder parity tests ([PR #130](https://github.com/OrbitalCommons/fitsio-pure/pull/130), `crates/compat-parity/tests/fixtures/hcompress/`) by `make_fixtures.py` in this directory, with astropy 8.0.1. Synthetic data, not from an instrument.

**License**: Apache-2.0, as fitsio-pure.

**Description**: `uint8` (smooth image / 8), 57 × 23, decoded range 85 to 164. The source image is `1000 + 300 sin(x/9) cos(y/6)` plus Gaussian noise (σ = 12, seed 7). Written by:

```python
write("hc_u8_lossless", (smooth_img / 8).astype(np.uint8), compression_type="HCOMPRESS_1")
```

`hc_u8_lossless.expected` holds astropy's decode of the image as little-endian `float64`, row-major (23 rows of 57). fitsio-pure's tests also check that cfitsio decodes it identically.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 1 col x 1 row | COMPRESSED_IMAGE | `HCOMPRESS_1` tile-compressed image, decompressed 57 x 23 |

## FITS Features Exercised

- `HCOMPRESS_1` (H-transform and quadtree coding), `SCALE = 0` (lossless)
- Tile shape `57 × 57` taller than the image (23 rows): one clipped tile
- `ZBITPIX = 8`

**File size**: 8,640 bytes; `.expected` 10,488 bytes
