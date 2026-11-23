# theap_gap.fits

**Source**: Generated for the port of [cool-japan/scirs](https://github.com/cool-japan/scirs)'s FITS module (`scirs2-io`) onto [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure), as regression fixtures. Written byte by byte by `make_theap_gap_table.py` in this directory, which reproduces it exactly. No standard writer leaves a gap before the heap; the FITS standard allows one. Synthetic data.

**License**: Apache-2.0, as fitsio-pure.

**Description**: An empty primary HDU and a one-row `BINTABLE` with a `1PJ` column. The row's descriptor is `(3, 0)`; the heap starts 100 zero bytes after the 8-byte row (`THEAP = 108`), and `PCOUNT = 112` counts the gap and the 12-byte heap, as FITS 4.0 Sect. 7.3.5 has it. The cell holds `[7, 8, 9]` (astropy 8.0.3 reads the same).

It is the regression file for fitsio-pure#199: a reader that bounds-checks the heap as `THEAP + PCOUNT` (counting the gap twice) fails on the table's data unit alone (120 bytes), though the whole file's padding hides it. astropy 8.0.3 and fitsverify 4.6.4 also take `PCOUNT` as the heap's size from `THEAP`; here the padding covers it.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | `SIMPLE`, `BITPIX = 8`, `NAXIS = 0` only |
| 1   | BINTABLE | 1 col x 1 row | | `TTYPE1 = 'V'`, `TFORM1 = 'PJ(3)'`, `THEAP = 108`, `PCOUNT = 112` |

## FITS Features Exercised

- Variable-length array (`P` descriptor) column
- `THEAP` past the end of the rows: a gap before the heap
- `PCOUNT` counting the gap and the heap
- Minimal headers with no comments

**File size**: 8,640 bytes. **SHA-256**: `949dc83f3a186942c4a59c05d29dd6832229c6052121a5529bf3d5198621943f`
