# Astro_UIT.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html), original file `samples/UITfuv2582gc.fits` (538,560 bytes). This copy was taken from the fitsrs test-file tarball (https://alasky.cds.unistra.fr/Aladin-Lite-test-files/fits-rs-test-files.tar, `samples/fits.gsfc.nasa.gov/Astro_UIT.fits`) and is byte-identical to that copy, which is corrupted (see below).

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

## Known Defect: Corrupted by Text Transcoding

This file is not a faithful copy of the GSFC original. Compared byte for byte with `UITfuv2582gc.fits`, every byte >= 0x80 has been replaced by the 3-byte UTF-8 replacement character `EF BF BD` (163,125 bytes), and every carriage-return byte (0x0D, 80 of them) has been replaced by a line feed (0x0A). The 11,520-byte header (4 blocks) is unaffected, so the header and keyword values above are correct. The data unit is not: the first replaced byte is at file offset 12,050, and 240,092 of the 262,144 pixels decode to values that differ from the original. The extra bytes push the file 326,250 bytes past the end of the declared data unit, so the file length is not a multiple of 2880 and astropy reports the trailing bytes as an invalid extra HDU. Use this file only as a malformed-file or trailing-garbage case; fetch the GSFC original for real pixel data.

**File size**: 864,810 bytes (845 KB); the GSFC original is 538,560 bytes
