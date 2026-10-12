# NICMOSn4hk12010_mos.fits

## Source

HST NICMOS Camera 2 mosaic of NGC 4151, observed 1998-05-22 with the F222M
filter (2.2 micron). MULTIACCUM readout mode, 64-second exposure. Mosaic of 6
dithered pointings in a spiral pattern (NIC-SPIRAL-DITH). Proposal 7215,
PI Rodger Thompson. Calibrated through CALNICB pipeline. This is the NASA FITS
sample `NICMOSn4hk12010_mos.fits`
(https://fits.gsfc.nasa.gov/samples/NICMOSn4hk12010_mos.fits), byte-identical,
and the same file as `nasa-samples/HST_NICMOS.fits`.

## History

Until 2026-10-11 this corpus held a corrupted copy (2,453,667 bytes): a text
round trip had turned most bytes >= 0x80 into the four ASCII characters `\xNN`,
changed CR LF to LF and dropped spaces and tabs before newlines, leaving garbage
SCI data and only 2 readable HDUs. It was replaced with the GSFC original,
which reproduces the corrupted copy exactly under those transformations.

## HDU Structure

| HDU | Type    | EXTNAME | Dimensions | Data Size  |
|-----|---------|---------|------------|------------|
| 0   | Primary | --      | (empty)    | 0 B        |
| 1   | IMAGE   | SCI     | 270 x 263  | 284,040 B  |
| 2   | IMAGE   | ERR     | 270 x 263  | 284,040 B  |
| 3   | IMAGE   | DQ      | 270 x 263  | 142,020 B  |
| 4   | IMAGE   | SAMP    | 270 x 263  | 142,020 B  |
| 5   | IMAGE   | TIME    | 270 x 263  | 284,040 B  |

6 HDUs total (NEXTEND=5). Dimensions are NAXIS1 x NAXIS2 (columns x rows).
Standard NICMOS multi-extension format with science, error, data quality,
samples, and time arrays. SCI, ERR and TIME are BITPIX=-32; DQ and SAMP are
BITPIX=16.

## FITS Features Exercised

- Multi-extension IMAGE file (5 extensions)
- Empty primary HDU (BITPIX=16, NAXIS=0) with rich instrument metadata (251 header cards)
- INHERIT=T on extensions
- EXTNAME + EXTVER extension naming
- Full WCS with CD matrix, RA---TAN/DEC--TAN
- Mixed pixel types: 32-bit float (BITPIX=-32) and 16-bit integer (BITPIX=16) extensions
- NICMOS calibration switches (BIASCORR, DARKCORR, FLATCORR, etc.)
- Photometry keywords (PHOTFLAM, PHOTFNU, PHOTZPT)
- Per-quadrant image statistics (QAMEAN, QBMEAN, etc.)

## File Size

1,198,080 bytes (1.1 MB)
