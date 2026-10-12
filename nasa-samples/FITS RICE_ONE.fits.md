# FITS RICE_ONE.fits

**Source**: Not on the NASA GSFC FITS samples page (https://fits.gsfc.nasa.gov/fits_samples.html does not list it). This copy is byte-identical to `samples/fits.gsfc.nasa.gov/FITS RICE_ONE.fits` in the fitsrs test-file tarball (https://alasky.cds.unistra.fr/Aladin-Lite-test-files/fits-rs-test-files.tar). No earlier origin (such as the DECaPS release it was cut from) was found.

**Instrument/Mission**: DECam (Dark Energy Camera) on the CTIO 4.0-m Blanco telescope. Part of the DECam Plane Survey (DECaPS), a wide-field optical/NIR survey of the southern Galactic plane.

**Object**: DECaPS tile 1274m400 (brick centered at RA 8:29:44, Dec -40:00:00).

## HDU Structure

| HDU | Type     | Dimensions          | Description                                     |
|-----|----------|---------------------|-------------------------------------------------|
| 0   | Primary  | (empty)             | Survey metadata, WCS                             |
| 1   | BINTABLE | 3 cols x 1296 rows  | RICE_ONE compressed image (original: 3600 x 3600, BITPIX = -32) |

## FITS Features Exercised

- FITS tile compression with ZCMPTYPE = 'RICE_ONE', an alias for the registered name 'RICE_1'. cfitsio accepts both names (imcompress.c); a reader that matches only 'RICE_1' will not recognize this file
- Compressed floating-point image (ZBITPIX = -32) with SUBTRACTIVE_DITHER_2 quantization
- Variable-length array column (1PB) with heap storage (17.5 MB heap)
- ZSCALE/ZZERO per-tile scaling columns
- 100 x 100 pixel tile size (ZTILE1/ZTILE2)
- Filename with embedded space

**File size**: 17,573,760 bytes (16.8 MB)
