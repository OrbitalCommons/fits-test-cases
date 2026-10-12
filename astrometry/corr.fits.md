# corr.fits

## Source

Astrometry.net plate solving output (https://astrometry.net/). This is a correspondence
table matching detected sources in an image to reference catalog stars. This file is
byte-identical to `samples/astrometry.net/corr.fits` in the test-file archive of the Rust
[fitsrs](https://github.com/cds-astro/fitsrs) crate (https://alasky.cds.unistra.fr/Aladin-Lite-test-files/fits-rs-test-files.tar). The header records only
ORIGIN = 'ESO-QFITS' and DATE = '2025-02-12T23:10:00'; it does not identify the solved image.

## HDU Structure

| HDU | Type     | Details                   | BITPIX |
|-----|----------|---------------------------|--------|
| 0   | Primary  | Empty (NAXIS=0)           | 8      |
| 1   | BINTABLE | 28 columns x 52 rows      | 8      |

Row width is 158 bytes (8,216 bytes of table data). The table has no EXTNAME.

## FITS Features Exercised

- **Empty primary HDU** with `NAXIS = 0` and `EXTEND = T`
- **Binary table** with a wide variety of column types: `1D` (float64), `1J` (int32),
  `1K` (int64), `1E` (float32), `2A` (2-char string)
- **28 columns** including positional matches (field_x/y, index_x/y, field_ra/dec,
  index_ra/dec), catalog cross-references (ref_cat, ref_id), proper motions (pmra, pmdec),
  parallax, photometry (mag, FLUX, BACKGROUND, phot_bp/rp_mean_mag)
- **TUNIT** keywords on the first 11 columns only (`pixels`, `degrees`, and `none` for
  index_id, field_id and match_weight); columns 12-28 have no TUNIT
- Written by ESO-QFITS

## File Size

20,160 bytes (20 KB)
