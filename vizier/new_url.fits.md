# new_url.fits

## Source

VizieR astronomical catalog service (https://vizier.cds.unistra.fr/). This is an ISO
(Infrared Space Observatory) ISOCAM raster observation of the ISOGAL survey, retrieved
through VizieR. The observation uses the LW3 filter at 14.5 microns.

## HDU Structure

| HDU | Type    | Dimensions | BITPIX |
|-----|---------|------------|--------|
| 0   | Primary | 121 x 346  | -32    |

Single-HDU file with a 32-bit floating-point image (167,464 bytes of pixel data).

## FITS Features Exercised

- **CROTA2 keyword** for image rotation (47.68 degrees) -- legacy WCS convention
- **CD matrix** also present (`CD1_1`, `CD1_2`, `CD2_1`, `CD2_2`) alongside CDELT/CROTA
- **Extensive HISTORY cards** documenting a full data reduction pipeline (dark correction,
  deglitching, stabilization, flat fielding, flux conversion)
- **Legacy DATE format** (`DATE = '16/12/98'`) using old DD/MM/YY convention
- **Non-square image** dimensions (121 x 346)
- Written by IDL (29-May-2001)

## File Size

175 KB
