# VAR.358.R.fits

## Source

VizieR astronomical catalog service (https://vizier.cds.unistra.fr/). Variable star
observation from the M35 + NGC 2158 variability survey (Nardiello et al.). This is a
small R-band finding chart / cutout image for variable star 358 of VizieR catalogue
J/MNRAS/447/3536 (Nardiello et al., 2015, Asiago 67/92 cm Schmidt telescope), whose
`charts/` directory names files `VAR.NNN.A.fits` (star number, band). This file is
byte-identical to https://cdsarc.cds.unistra.fr/ftp/J/MNRAS/447/3536/charts/VAR.358.R.fits
(catalogue page: https://cdsarc.cds.unistra.fr/viz-bin/cat/J/MNRAS/447/3536) and to
`samples/vizier/VAR.358.R.fits` in the test-file archive of the Rust
[fitsrs](https://github.com/cds-astro/fitsrs) crate (https://alasky.cds.unistra.fr/Aladin-Lite-test-files/fits-rs-test-files.tar).

## HDU Structure

| HDU | Type    | Dimensions | BITPIX |
|-----|---------|------------|--------|
| 0   | Primary | 51 x 51    | -32    |

Single-HDU file with a 32-bit floating-point image (10,404 bytes of pixel data).
Dimensions are NAXIS1 x NAXIS2 = 51 columns x 51 rows.

## FITS Features Exercised

- **Placeholder/blank keyword values**: `DATE-OBS`, `TIME-OBS`, `EXPTIME`, `RA_TARG` and
  `DEC_TARG` hold blank strings; `PROPOSID`, `FILTER1`, `FILTER2` and `CCDGAIN` have no
  value at all (`=` followed only by spaces); `ORIENTAT = '2014-xx-xx'` and
  `PA_APER = 'xxx:xx:xx.xxx'` hold placeholder strings
- **Missing value-indicator space**: 12 cards write `=` directly followed by the value
  (`CTYPE1  ='RA---TAN'`, `ROOTNAME=M35 ...`). A card without `= ` in columns 9-10 has
  no value under the standard. astropy warns on each and returns the raw text as the
  value (`CTYPE1` reads `='RA---TAN'`), so astropy's WCS sees empty CTYPEs
- **Unquoted string value** (`ROOTNAME=M35 + NGC 2158 VAR N`) -- non-standard formatting
- **Unterminated string** (`TARGNAME='Nardiello et al. (` has no closing quote)
- **Free-format mandatory keywords**: `SIMPLE  = T` and `BITPIX  = -32` are not right-justified
  to column 30 as the standard requires; astropy warns that the SIMPLE card does not respect
  the standard
- **CD matrix** WCS with TAN projection (the TAN CTYPE cards are among the malformed ones above)
- **Very small image** (51 x 51 pixels)
- **DATATYPE keyword** (`REAL*4`) -- non-standard Fortran-style type declaration
- **Unusual DATE format** (`DATE = '00/00/00'`) -- invalid/placeholder date

## File Size

14,400 bytes (14 KB)
