# NICMOSn4hk12010_mos.fits

## Source

HST NICMOS Camera 2 mosaic of NGC 4151, observed 1998-05-22 with the F222M
filter (2.2 micron). MULTIACCUM readout mode, 64-second exposure. Mosaic of 6
dithered pointings in a spiral pattern (NIC-SPIRAL-DITH). Proposal 7215,
PI Rodger Thompson. Calibrated through CALNICB pipeline.

## HDU Structure

| HDU | Type    | EXTNAME | Dimensions | Data Size  |
|-----|---------|---------|------------|------------|
| 0   | Primary | --      | (empty)    | 0 B        |
| 1   | IMAGE   | SCI     | 270 x 263  | 284,040 B  |
| 2   | IMAGE   | ERR     | 270 x 263  | --         |
| 3   | IMAGE   | DQ      | 270 x 263  | --         |
| 4   | IMAGE   | SAMP    | 270 x 263  | --         |
| 5   | IMAGE   | TIME    | 270 x 263  | --         |

6 HDUs total (NEXTEND=5). Standard NICMOS multi-extension format with
science, error, data quality, samples, and time arrays.

## FITS Features Exercised

- Multi-extension IMAGE file (5 extensions)
- Empty primary HDU with rich instrument metadata (~190 header cards)
- INHERIT=T on extensions
- EXTNAME + EXTVER extension naming
- Full WCS with CD matrix, RA---TAN/DEC--TAN
- 32-bit float pixel data (BITPIX=-32)
- NICMOS calibration switches (BIASCORR, DARKCORR, FLATCORR, etc.)
- Photometry keywords (PHOTFLAM, PHOTFNU, PHOTZPT)
- Per-quadrant image statistics (QAMEAN, QBMEAN, etc.)

## File Size

2,453,667 bytes (2.3 MB)
