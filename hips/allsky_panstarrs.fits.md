# allsky_panstarrs.fits

## Source

Pan-STARRS all-sky survey tile from the CDS hips2fits service
(https://alasky.cds.unistra.fr/hips-image-services/hips2fits).

## HDU Structure

| HDU | Type    | Dimensions    | BITPIX |
|-----|---------|---------------|--------|
| 0   | Primary | 1728 x 1856   | 16     |

Single-HDU file with a 16-bit integer image (6,414,336 bytes of pixel data).

## FITS Features Exercised

- **BLANK keyword** for integer null values (`BLANK = -32768`)
- **BZERO / BSCALE** linear scaling (`BZERO = 3.4136`, `BSCALE = 0.000206`) encoding
  floating-point data in 16-bit integers
- Minimal header (no WCS, no EXTEND)

## File Size

6.2 MB
