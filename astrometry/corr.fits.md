# corr.fits

## Source

Astrometry.net plate solving output (https://astrometry.net/). This is a correspondence
table matching detected sources in an image to reference catalog stars.

## HDU Structure

| HDU | Type     | Details                   | BITPIX |
|-----|----------|---------------------------|--------|
| 0   | Primary  | Empty (NAXIS=0)           | 8      |
| 1   | BINTABLE | 28 columns x 52 rows      | 8      |

Row width is 158 bytes (8,216 bytes of table data).

## FITS Features Exercised

- **Empty primary HDU** with `NAXIS = 0` and `EXTEND = T`
- **Binary table** with a wide variety of column types: `1D` (float64), `1J` (int32),
  `1K` (int64), `1E` (float32), `2A` (2-char string)
- **28 columns** including positional matches (field_x/y, index_x/y, field_ra/dec,
  index_ra/dec), catalog cross-references (ref_cat, ref_id), proper motions (pmra, pmdec),
  parallax, photometry (mag, FLUX, BACKGROUND, phot_bp/rp_mean_mag)
- **TUNIT** keywords with physical units on most columns
- Written by ESO-QFITS

## File Size

20 KB
