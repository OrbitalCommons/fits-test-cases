# plio_i32_mask.fits

**Source**: Generated for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure)'s HCOMPRESS/PLIO decoder parity tests ([PR #130](https://github.com/OrbitalCommons/fitsio-pure/pull/130), `crates/compat-parity/tests/fixtures/hcompress/`) by `make_fixtures.py` in this directory, with astropy 8.0.1. Synthetic data, not from an instrument.

**License**: Apache-2.0, as fitsio-pure.

**Description**: `int32` blocky mask with a diagonal line, 57 × 23, decoded range 0 to 3001. Written by:

```python
write("plio_i32_mask", ((x // 5 + y // 3) % 4 * 1000 + (x == y)).astype(np.int32), compression_type="PLIO_1")
```

`plio_i32_mask.expected` holds astropy's decode of the image as little-endian `float64`, row-major (23 rows of 57). fitsio-pure's tests also check that cfitsio decodes it identically.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 1 col x 23 rows | COMPRESSED_IMAGE | `PLIO_1` tile-compressed image, decompressed 57 x 23 |

## FITS Features Exercised

- `PLIO_1` (IRAF pixel-list run-length encoding), lossless, for non-negative integers below 2^24
- Tiles `57 × 1`: 23 tiles (one row each)
- `ZBITPIX = 32`

**File size**: 8,640 bytes; `.expected` 10,488 bytes
