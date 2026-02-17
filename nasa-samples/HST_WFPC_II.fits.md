# HST_WFPC_II.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html)

**Instrument/Mission**: Hubble Space Telescope (HST), Wide Field and Planetary Camera 2 (WFPC2). WFPC2 was HST's primary optical imager from 1993 to 2009 with four 800x800 CCD detectors. This file contains all four chips as a 3D data cube (converted from GEIS format), using the FR533P15 linear ramp filter.

**Object**: NGC 4151, observed 1999-02-20.

## HDU Structure

| HDU | Type  | Dimensions         | EXTNAME                 | Description                                |
|-----|-------|--------------------|-------------------------|--------------------------------------------|
| 0   | Primary | 200 x 200 x 4   |                         | 3D float image cube (4 detector chips)     |
| 1   | TABLE | 49 cols x 4 rows   | u5780205r_cvt.c0h.tab  | ASCII table with per-chip group parameters |

## FITS Features Exercised

- 3-dimensional primary image (NAXIS = 3, with GROUP_NUMBER as third axis)
- ASCII TABLE extension with 49 columns (large table)
- GEIS-to-FITS converted file (4 original groups mapped to NAXIS3 = 4)
- CD3_3, CD3_1, etc. for third axis WCS
- Comprehensive WFPC2 calibration and photometry keywords

**File size**: 699,840 bytes (683 KB)
