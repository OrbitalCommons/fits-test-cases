# hc_i32_scale8_smooth.fits

**Source**: Generated for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure)'s HCOMPRESS/PLIO decoder parity tests ([PR #130](https://github.com/OrbitalCommons/fitsio-pure/pull/130), `crates/compat-parity/tests/fixtures/hcompress/`) by `make_fixtures.py` in this directory, with astropy 8.0.1. Synthetic data, not from an instrument.

**License**: Apache-2.0, as fitsio-pure.

**Description**: `int32` (smooth image × 1e5), 57 × 23, decoded range 6.80042e+07 to 1.31878e+08. The source image is `1000 + 300 sin(x/9) cos(y/6)` plus Gaussian noise (σ = 12, seed 7). Written by:

```python
write("hc_i32_scale8_smooth", (smooth_img * 1e5).astype(np.int32), compression_type="HCOMPRESS_1", hcomp_scale=8, hcomp_smooth=True)
```

`hc_i32_scale8_smooth.expected` holds astropy's decode of the image as little-endian `float64`, row-major (23 rows of 57). fitsio-pure's tests also check that cfitsio decodes it identically.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 1 col x 1 row | COMPRESSED_IMAGE | `HCOMPRESS_1` tile-compressed image, decompressed 57 x 23 |

## FITS Features Exercised

- `HCOMPRESS_1` (H-transform and quadtree coding), `SCALE = 8` (lossy: coefficients divided by the scale)
- `SMOOTH`, written by astropy as the logical `ZVAL2 = T` (cfitsio writes an integer 1); the decoder must smooth while reconstructing
- Tile shape `57 × 57` taller than the image (23 rows): one clipped tile
- `ZBITPIX = 32`

**File size**: 11,520 bytes; `.expected` 10,488 bytes
