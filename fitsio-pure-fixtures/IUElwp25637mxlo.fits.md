# IUElwp25637mxlo.fits

## Source

IUE (International Ultraviolet Explorer) merged extracted low-dispersion
spectrum of NGC 4151. LWP camera, image 25637, large aperture, observed
1993-05-31. Processed with NEWSIPS pipeline v2.4.3 at GSFC. 660-second
exposure (LEXPTIME = 659.743), point source extraction. This is the NASA FITS
sample `IUElwp25637mxlo.fits`
(https://fits.gsfc.nasa.gov/samples/IUElwp25637mxlo.fits), byte-identical, and
the same file as `nasa-samples/IUE_LWP.fits`.

## History

Until 2026-10-11 this corpus held a corrupted copy: the bytes had been decoded
as UTF-8 with backslash escapes for invalid sequences and re-encoded, so most
bytes >= 0x80 became the four ASCII characters `\xNN` (59,553 bytes; NPOINTS
read 604 instead of 640). It was replaced with the GSFC original, which
reproduces the corrupted copy exactly under that round trip.

## HDU Structure

| HDU | Type     | EXTNAME | Dimensions       | Data Size  |
|-----|----------|---------|------------------|------------|
| 0   | Primary  | --      | (empty)          | 0 B        |
| 1   | BINTABLE | MELO    | 9 cols x 1 row   | 11,535 B   |

2 HDUs total. The primary header embeds the IUE VICAR header block between
`COMMENT IUE-VICAR HEADER START` and `COMMENT IUE-VICAR HEADER END`; the VICAR lines
themselves are cards with a blank keyword field. BINTABLE holds the extracted
spectrum.

## FITS Features Exercised

- Binary table with vector columns (640E arrays for NET, BACKGROUND, SIGMA,
  FLUX; 640I for QUALITY flags)
- Single-row table encoding a full spectrum as array columns
- Very large primary header (354 cards) with embedded VICAR heritage header
- Character (5A), integer (1I), float (1E), and vector float/int column types
- IUE-specific keywords: CAMERA, DISPERSN, APERTURE, orbital elements
- Exposure and calibration metadata (LEXPTIME keyword; dispersion constants in HISTORY)
- Extensive HISTORY cards documenting full processing pipeline

## File Size

48,960 bytes (48 KB)
