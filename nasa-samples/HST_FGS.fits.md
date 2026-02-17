# HST_FGS.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html)

**Instrument/Mission**: Hubble Space Telescope (HST), Fine Guidance Sensor 1 (FGS). The FGS instruments are white-light interferometers used for both guiding HST and high-precision astrometry. This file contains a Transfer mode observation with PMT photon counts and star selector encoder data.

**Object**: NGC 4151, observed 2000-10-29.

## HDU Structure

| HDU | Type  | Dimensions     | EXTNAME                | Description                             |
|-----|-------|----------------|------------------------|-----------------------------------------|
| 0   | Primary | 89688 x 7   |                        | 32-bit integer image (7 data groups)    |
| 1   | TABLE | 6 cols x 7 rows | f64y0106m_cvt.a1h.tab | ASCII table with per-group WCS metadata |

## FITS Features Exercised

- Large primary array (89688 x 7, BITPIX = 32)
- ASCII TABLE extension (XTENSION = TABLE with TBCOL/TFORM keywords)
- Converted GEIS (Generic Edited Information Set) format to FITS
- Rich header with K-factor calibration constants and temperature sensors

**File size**: 2,540,160 bytes (2.4 MB)
