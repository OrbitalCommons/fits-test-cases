# IUElwp25637mxlo.fits

## Source

IUE (International Ultraviolet Explorer) merged extracted low-dispersion
spectrum of NGC 4151. LWP camera, image 25637, large aperture, observed
1993-05-31. Processed with NEWSIPS pipeline v2.4.3 at GSFC. 660-second
exposure, point source extraction.

## HDU Structure

| HDU | Type     | EXTNAME | Dimensions       | Data Size  |
|-----|----------|---------|------------------|------------|
| 0   | Primary  | --      | (empty)          | 0 B        |
| 1   | BINTABLE | MELO    | 9 cols x 1 row   | 11,535 B   |

2 HDUs total. Primary header contains extensive IUE VICAR header block
embedded in COMMENT cards. BINTABLE holds the extracted spectrum.

## FITS Features Exercised

- Binary table with vector columns (640E arrays for NET, BACKGROUND, SIGMA,
  FLUX; 640I for QUALITY flags)
- Single-row table encoding a full spectrum as array columns
- Very large primary header (~360 cards) with embedded VICAR heritage header
- Character (5A), integer (1I), float (1E), and vector float/int column types
- IUE-specific keywords: CAMERA, DISPERSN, APERTURE, orbital elements
- Wavelength calibration metadata (LEXPTIME, dispersion constants)
- Extensive HISTORY cards documenting full processing pipeline

## File Size

59,553 bytes (58 KB)
