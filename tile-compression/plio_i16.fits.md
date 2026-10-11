# plio_i16.fits

**Source**: Generated for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure)'s HCOMPRESS/PLIO decoder parity tests ([PR #130](https://github.com/OrbitalCommons/fitsio-pure/pull/130), `crates/compat-parity/tests/fixtures/hcompress/`) by `make_fixtures.py` in this directory, with astropy 8.0.1. Synthetic data, not from an instrument.

**License**: Apache-2.0, as fitsio-pure.

**Description**: `int16` (smooth image − 600, clipped at 0), 57 × 23, decoded range 80 to 718. The source image is `1000 + 300 sin(x/9) cos(y/6)` plus Gaussian noise (σ = 12, seed 7). Written by:

```python
write("plio_i16", (smooth_img - 600).clip(0).astype(np.int16), compression_type="PLIO_1")
```

`plio_i16.expected` holds astropy's decode of the image as little-endian `float64`, row-major (23 rows of 57). fitsio-pure's tests also check that cfitsio decodes it identically.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 1 col x 23 rows | COMPRESSED_IMAGE | `PLIO_1` tile-compressed image, decompressed 57 x 23 |

## FITS Features Exercised

- `PLIO_1` (IRAF pixel-list run-length encoding), lossless, for non-negative integers below 2^24
- Tiles `57 × 1`: 23 tiles (one row each)
- `ZBITPIX = 16`

**File size**: 11,520 bytes; `.expected` 10,488 bytes
