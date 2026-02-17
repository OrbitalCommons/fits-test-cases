# HST_WFPC_II_bis.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html)

**Instrument/Mission**: Hubble Space Telescope (HST), Wide Field and Planetary Camera 2 (WFPC2). WFPC2 was HST's workhorse optical imager (1993-2009), consisting of four 800x800 CCD detectors (one Planetary Camera and three Wide Field chips). This file contains a single-chip (WF4, detector 4) 100x100 pixel cutout using the FR533P15 linear ramp filter, from a 2-exposure mosaic.

**Object**: NGC 4151, observed 1999-02-20.

## HDU Structure

| HDU | Type    | Dimensions | Description                        |
|-----|---------|------------|------------------------------------|
| 0   | Primary | 100 x 100  | 32-bit float image (BITPIX = -32)  |

## FITS Features Exercised

- Single primary image (no extensions)
- 32-bit floating point data
- Linear ramp filter (LRFWAVE = 4877.0 angstroms)
- WCS with CD matrix
- HISTORY cards documenting CALWP2 calibration pipeline
- Photometry keywords (PHOTFLAM, PHOTZPT, PHOTPLAM, PHOTBW)

**File size**: 63,360 bytes (62 KB)
