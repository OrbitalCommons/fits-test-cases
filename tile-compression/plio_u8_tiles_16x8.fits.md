# plio_u8_tiles_16x8.fits

**Source**: Generated for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure)'s HCOMPRESS/PLIO decoder parity tests ([PR #130](https://github.com/OrbitalCommons/fitsio-pure/pull/130), `crates/compat-parity/tests/fixtures/hcompress/`) by `make_fixtures.py` in this directory, with astropy 8.0.1. Synthetic data, not from an instrument.

**License**: Apache-2.0, as fitsio-pure.

**Description**: `uint8` `(x * y) % 200` pattern, 57 × 23, decoded range 0 to 199. Written by:

```python
write("plio_u8_tiles_16x8", ((x * y) % 200).astype(np.uint8), compression_type="PLIO_1", tile_shape=(8, 16))
```

`plio_u8_tiles_16x8.expected` holds astropy's decode of the image as little-endian `float64`, row-major (23 rows of 57). fitsio-pure's tests also check that cfitsio decodes it identically.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 1 col x 12 rows | COMPRESSED_IMAGE | `PLIO_1` tile-compressed image, decompressed 57 x 23 |

## FITS Features Exercised

- `PLIO_1` (IRAF pixel-list run-length encoding), lossless, for non-negative integers below 2^24
- Tiles `16 × 8`: 12 tiles (two-dimensional, clipped at the edges)
- `ZBITPIX = 8`

**File size**: 8,640 bytes; `.expected` 10,488 bytes
