# VAR.358.R.fits

## Source

VizieR astronomical catalog service (https://vizier.cds.unistra.fr/). Variable star
observation from the M35 + NGC 2158 variability survey (Nardiello et al.). This is a
small R-band finding chart / cutout image.

## HDU Structure

| HDU | Type    | Dimensions | BITPIX |
|-----|---------|------------|--------|
| 0   | Primary | 51 x 51    | -32    |

Single-HDU file with a 32-bit floating-point image (10,404 bytes of pixel data).

## FITS Features Exercised

- **Placeholder/blank keyword values**: multiple keywords have empty string or
  placeholder values (`DATE-OBS`, `TIME-OBS`, `EXPTIME`, `RA_TARG`, `DEC_TARG`,
  `PROPOSID`, `FILTER1`, `FILTER2`, `CCDGAIN` all empty)
- **Unquoted string value** (`ROOTNAME = M35 + NGC 2158 VAR N`) -- non-standard formatting
- **CD matrix** WCS with TAN projection
- **Very small image** (51 x 51 pixels)
- **DATATYPE keyword** (`REAL*4`) -- non-standard Fortran-style type declaration
- **Unusual DATE format** (`DATE = '00/00/00'`) -- invalid/placeholder date

## File Size

15 KB
