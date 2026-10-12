# HST_WFPC_II_bis.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html), original file `samples/WFPC2ASSNu5780205bx.fits`. This copy is byte-identical to the GSFC file (SHA-256 checked 2026-10-11).

**Instrument/Mission**: Hubble Space Telescope (HST), Wide Field and Planetary Camera 2 (WFPC2). WFPC2 was HST's workhorse optical imager (1993-2009), consisting of four 800x800 CCD detectors (one Planetary Camera and three Wide Field chips). This file is a WMOSAIC product (HISTORY: "Ran task WMOSAIC, version 2.1"), which the GSFC page describes as a 1600 x 1600 mosaic of the 4 chips trimmed to 100 x 100 pixels. It uses the FR533P15 linear ramp filter. The header still carries DETECTOR = 4 and NCOMBINE = 2 (two exposures combined).

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
- HISTORY cards (39) documenting calibration reference files, throughput tables, and the WARMPIX and WMOSAIC tasks (CALWP2 is named only in the comment of the blank CAL_VER keyword)
- Photometry keywords (PHOTFLAM, PHOTZPT, PHOTPLAM, PHOTBW)

**File size**: 63,360 bytes (62 KB)
