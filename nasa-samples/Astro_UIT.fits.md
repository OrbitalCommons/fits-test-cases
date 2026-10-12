# Astro_UIT.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html), file `samples/UITfuv2582gc.fits` (https://fits.gsfc.nasa.gov/samples/UITfuv2582gc.fits), byte-identical.

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
- Five HISTORY cards documenting the astrometry steps
- RADECSYS = FK5, EQUINOX = 2000.0

## History

Until 2026-10-11 this corpus held a corrupted copy, taken from the fitsrs test-file archive (https://alasky.cds.unistra.fr/Aladin-Lite-test-files/fits-rs-test-files.tar), in which every byte >= 0x80 had been replaced by the UTF-8 replacement character `EF BF BD` and every carriage return by a line feed (864,810 bytes, 240,092 pixels wrong). It was replaced with the GSFC original, which reproduces the corrupted copy exactly under that mapping.

**File size**: 538,560 bytes (526 KB)
