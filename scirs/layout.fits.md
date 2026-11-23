# layout.fits

**Source**: Generated for the port of [cool-japan/scirs](https://github.com/cool-japan/scirs)'s FITS module (`scirs2-io`) onto [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure), as regression fixtures. Written by astropy 8.0.1 with `make_layout_card36.py` in this directory, which reproduces it byte for byte (also with astropy 8.0.3). Synthetic data.

**License**: Apache-2.0, as fitsio-pure.

**Description**: A layout and navigation case. An empty primary HDU; a `BINTABLE` whose one `PJ()` cell holds `0..749` (a 3000-byte heap), so its data unit runs into a second 2880-byte block; then an `IMAGE` extension that must be found after it. HDU offsets, as astropy reports them:

| HDU | Header at | Data at | Data span |
|-----|-----------|---------|-----------|
| 0 | 0 | 2880 | 0 |
| 1 | 2880 | 5760 | 5760 |
| 2 | 11520 | 14400 | 2880 |

The image is `int16`, 4 x 3 (`NAXIS1 x NAXIS2`), `data[y, x] = (4 y + x) * 7 - 20`: rows `[-20, -13, -6, 1]`, `[8, 15, 22, 29]`, `[36, 43, 50, 57]`.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 1 col x 1 row | HEAPTAB | `SAMPLES`, `PJ(750)`, `PCOUNT = 3000` |
| 2   | IMAGE    | 4 x 3      | AFTER   | `BITPIX = 16` |

## FITS Features Exercised

- A heap that pushes a table's data unit past one block
- Finding an HDU after a table with a heap (data size `NAXIS1 x NAXIS2 + PCOUNT`)
- Variable-length array column

**File size**: 17,280 bytes. **SHA-256**: `19ed072d4f38a5968b222d30d0c5cd8f27558e5b8a2ebc8d5b77034795712250`
