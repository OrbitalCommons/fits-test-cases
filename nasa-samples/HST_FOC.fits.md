# HST_FOC.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html)

**Instrument/Mission**: Hubble Space Telescope (HST), Faint Object Camera (FOC). The FOC was a photon-counting UV/optical imaging camera built by ESA, operational 1990-2002. It used an image intensifier tube to achieve the diffraction-limited resolution of HST. This observation uses the f/48 relay with COSTAR correction and F220W+F275W UV filters in zoom format.

**Object**: NGC 4151, observed 1996-07-02.

## HDU Structure

| HDU | Type  | Dimensions       | EXTNAME             | Description                          |
|-----|-------|------------------|---------------------|--------------------------------------|
| 0   | Primary | 1024 x 1024   |                     | 32-bit float image (BITPIX = -32)    |
| 1   | TABLE | 18 cols x 1 row  | x38i0101t.c0h.tab  | ASCII table with GEIS group params   |

## FITS Features Exercised

- 32-bit floating point primary image
- ASCII TABLE extension
- GEIS-to-FITS converted file (OPSIZE, SDASMGNU keywords)
- Photometry keywords (PHOTFLAM, PHOTZPT, PHOTPLAM, PHOTBW)
- WCS with CD matrix (non-aligned rotation)

**File size**: 4,219,200 bytes (4.0 MB)
