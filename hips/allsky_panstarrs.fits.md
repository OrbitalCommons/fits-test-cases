# allsky_panstarrs.fits

## Source

HiPS `Allsky.fits` preview image of a Pan-STARRS DR1 HiPS, not a hips2fits cutout. The
image is the standard HiPS all-sky mosaic of all 768 order-3 tiles at 64 x 64 pixels,
packed 27 tiles per row: 27 x 64 = 1728 columns and ceil(768 / 27) = 29 rows of tiles,
29 x 64 = 1856 rows. The header names no survey or band. The current CDS files
https://alasky.cds.unistra.fr/Pan-STARRS/DR1/{r,i,z}/Norder3/Allsky.fits have the same
size, header layout and pixel layout (pixel correlation with this file 0.98 to 0.99) but
different BZERO/BSCALE, so the exact band and HiPS release could not be identified.
This file is byte-identical to `samples/hips2fits/allsky_panstarrs.fits` in the Rust
[fitsrs](https://github.com/cds-astro/fitsrs) crate's test samples (in the repository
until 2025-01-29, e.g. at commit
[87c6ca6](https://github.com/cds-astro/fitsrs/tree/87c6ca698eeb2d045acc587eaee6cc7d342567c8/samples/hips2fits);
now in https://alasky.cds.unistra.fr/Aladin-Lite-test-files/fits-rs-test-files.tar).

## HDU Structure

| HDU | Type    | Dimensions    | BITPIX |
|-----|---------|---------------|--------|
| 0   | Primary | 1728 x 1856   | 16     |

Single-HDU file with a 16-bit integer image (6,414,336 bytes of pixel data).
Dimensions are NAXIS1 x NAXIS2 = 1728 columns x 1856 rows.

## FITS Features Exercised

- **BLANK keyword** for integer null values, written as a floating-point value
  (`BLANK = -32768.0`), which the standard does not allow (BLANK must be an integer)
- **BZERO / BSCALE** linear scaling (`BZERO = 3.413579702377`, `BSCALE = 2.062367094166E-4`)
  encoding floating-point data in 16-bit integers
- Minimal header of 8 cards plus END, no comments (no WCS, no EXTEND)
- **No data padding**: the file ends right after the 6,414,336 data bytes, 2,304 bytes
  short of a 2880-byte boundary (file size is not a multiple of 2880)

## File Size

6,417,216 bytes (6.1 MiB)
