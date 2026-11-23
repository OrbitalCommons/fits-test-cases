# fpack_rice_u16_theap_gap_heap_pcount.fits

**Source**: Made for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure) by `make_theap_gap_fixture.py <fpack_rice_u16.fits> <output> heap-only` in this directory, from [`fpack_rice_u16.fits`](fpack_rice_u16.fits.md) (written by the reference `fpack` from CFITSIO 4.6.4). Synthetic data.

**License**: Apache-2.0, as fitsio-pure.

**Description**: [`fpack_rice_u16_theap_gap.fits`](fpack_rice_u16_theap_gap.fits.md) written the way astropy and fitsverify read `PCOUNT`, not the way the standard defines it. Both files put 100 bytes of junk (`0xFF`) between the compressed table's rows and its heap (`THEAP = 612`), and drop the table HDU's `CHECKSUM` and `DATASUM` cards. They differ only in `PCOUNT`:

| file | `PCOUNT` | meaning | data unit by the standard (`NAXIS1 x NAXIS2 + PCOUNT`) | heap ends at |
|---|---|---|---|---|
| `fpack_rice_u16_theap_gap` | 6,341 | gap + heap, as FITS 4.0 Sect. 7.3.5 defines it | 6,853 | 6,853 |
| this file | 6,241 | the heap alone, as astropy 8.0.3 and fitsverify 4.6.4 read it | 6,753 | 6,853 |

**The discrepancy:** FITS 4.0 Sect. 7.3.5 says `PCOUNT` "gives the total number of bytes from the end of the main data table to the end of the heap", gap included, and works an example. astropy 8.0.3 and fitsverify 4.6.4 instead read `PCOUNT` bytes of heap starting at `THEAP`, past the data unit's standard end when there is a gap. A file written to their reading, like this one, has a heap that runs 100 bytes past the data unit the standard computes, into its block padding. A reader that follows the standard and keeps strictly to the data unit fails on it; one that reads the padding (or the whole file) decodes it. The gap is small enough that the heap stays inside the padding, so the next block, and the file's length, are what the standard computes.

cfitsio 4.6.4 (by `fpack_expected.c`) and astropy 8.0.3 both decode it to the original image, so `fpack_rice_u16_theap_gap_heap_pcount.expected` equals `fpack_rice_u16.expected`. fitsverify reports it OK.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | Minimal header |
| 1   | BINTABLE | 1 col x 64 rows | COMPRESSED_IMAGE | `RICE_1` tile-compressed image, decompressed 64 x 64, heap after a gap and running into the padding |

## FITS Features Exercised

- `THEAP` past the end of a tile-compressed table's rows: a gap before the heap
- `PCOUNT` as the heap's size alone, against the standard's gap + heap
- A heap that ends in the data unit's block padding
- `RICE_1`, `ZBITPIX = 16`, unsigned 16-bit by `BZERO = 32768`

**File size**: 14,400 bytes; `.expected` 32,768 bytes. **SHA-256**: `436adc8ae9adcf43a3d76daae726734e2e5fbe3af3c2117a5121a534af03d29e`
