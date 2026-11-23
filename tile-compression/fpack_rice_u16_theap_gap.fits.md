# fpack_rice_u16_theap_gap.fits

**Source**: Made for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure)#204 by `make_theap_gap_fixture.py` in this directory, from [`fpack_rice_u16.fits`](fpack_rice_u16.fits.md) (written by the reference `fpack` from CFITSIO 4.6.4). No standard writer leaves a gap before the heap; the FITS standard allows one. Synthetic data.

**License**: Apache-2.0, as fitsio-pure.

**Description**: `fpack_rice_u16.fits` with 100 bytes of junk (`0xFF`) inserted between the compressed table's rows and its heap: `THEAP = 612` (512 bytes of rows plus the gap) and `PCOUNT` 100 larger (6,341), as FITS 4.0 Sect. 7.3.5 counts the gap in it. The table HDU's `CHECKSUM` and `DATASUM` cards are dropped, since its bytes change. A reader that ignores `THEAP` and takes the heap to start right after the rows reads every tile from the wrong bytes.

`fpack_rice_u16_theap_gap.expected` is identical to `fpack_rice_u16.expected`: cfitsio 4.6.4 (by `fpack_expected.c`) and astropy 8.0.3 both decode this file to the original image. The gap is small enough that `THEAP + PCOUNT` stays inside the padded data unit, so readers that take `PCOUNT` as the heap's size from `THEAP` (astropy 8.0.3, fitsverify 4.6.4) read it too; fitsverify reports it OK.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 1 col x 64 rows | COMPRESSED_IMAGE | `RICE_1` tile-compressed image, decompressed 64 x 64, heap after a gap |

## FITS Features Exercised

- `THEAP` past the end of a tile-compressed table's rows: a gap before the heap
- `RICE_1`, `ZBITPIX = 16`, unsigned 16-bit by `BZERO = 32768`
- Tiles `64 × 1`: 64 tiles (one row each)

**File size**: 14,400 bytes; `.expected` 32,768 bytes
