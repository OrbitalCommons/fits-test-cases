# Astro_UIT.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html)

**Instrument/Mission**: Astro-2 mission (1995), Ultraviolet Imaging Telescope (UIT). The UIT was a 38 cm Ritchey-Chretien telescope that flew on the Space Shuttle as part of the Astro observatory payload. It recorded far-UV images on photographic film using image-intensified cameras with cesium iodide (CsI) photocathodes.

**Object**: NGC 4151 (Seyfert galaxy), observed 1995-03-13 with the B1 filter (FUV band).

## HDU Structure

| HDU | Type    | Dimensions | Description                        |
|-----|---------|------------|------------------------------------|
| 0   | Primary | 512 x 512  | 16-bit integer image (BITPIX = 16) |

## FITS Features Exercised

- Single primary image HDU (no extensions)
- BSCALE/BZERO physical calibration (flux units ERGS/CM**2/S/ANGSTRM)
- WCS with TAN projection and CD matrix
- Rich HISTORY cards documenting astrometry pipeline
- RADECSYS = FK5, EQUINOX = 2000.0

**File size**: 864,810 bytes (845 KB)
