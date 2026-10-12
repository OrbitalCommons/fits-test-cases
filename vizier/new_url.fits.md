# new_url.fits

## Source

VizieR astronomical catalog service (https://vizier.cds.unistra.fr/). This is an ISO
(Infrared Space Observatory) ISOCAM raster observation (TARGET = 'LN2225E', observed
1996-02-12), retrieved through VizieR. The observation uses the LW3 filter at 14.5
microns. The header does not name a survey; the processing HISTORY references an
`isogal` pipeline directory (ISOGAL survey). The file downloads byte-identically from
VizieR's associated-data service at
https://cdsarc.cds.unistra.fr/saadavizier/download?oid=864973475310206978 (served as
`new.08700544.fits`) and is identical to `samples/vizier/new_url.fits` in the test-file
archive of the Rust [fitsrs](https://github.com/cds-astro/fitsrs) crate
(https://alasky.cds.unistra.fr/Aladin-Lite-test-files/fits-rs-test-files.tar).

## HDU Structure

| HDU | Type    | Dimensions | BITPIX |
|-----|---------|------------|--------|
| 0   | Primary | 121 x 346  | -32    |

Single-HDU file with a 32-bit floating-point image (167,464 bytes of pixel data).
Dimensions are NAXIS1 x NAXIS2 = 121 columns x 346 rows.

## FITS Features Exercised

- **CROTA2 keyword** for image rotation (47.68 degrees) -- legacy WCS convention
- **CD matrix** also present (`CD1_1`, `CD1_2`, `CD2_1`, `CD2_2`) alongside CDELT/CROTA.
  The two descriptions disagree: the CD matrix is the exact negative of the matrix
  implied by `CDELT1 = 0.00166667`, `CDELT2 = -0.00166667` and `CROTA2`, a 180 degree
  rotation about the reference pixel. The last HISTORY cards record that the image was
  reversed about both axes (`HREVERSE`). Readers that prefer CD (as WCSLIB does) and
  readers that use CDELT/CROTA put pixel (1, 1) at opposite corners of the field.
- **Extensive HISTORY cards** documenting a full data reduction pipeline (dark correction,
  deglitching, stabilization, flat fielding, flux conversion)
- **Legacy DATE format** (`DATE = '16/12/98'`) using old DD/MM/YY convention
- **Non-square image** dimensions (121 x 346)
- Written by IDL (29-May-2001); on 20 of the 35 value cards the comment text starts
  directly after the `/` (e.g. BITPIX's comment `/No. of bits per pixel`)

## File Size

178,560 bytes (175 KB)
