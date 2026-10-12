# NICMOSn4hk12010_mos.fits

## Source

HST NICMOS Camera 2 mosaic of NGC 4151, observed 1998-05-22 with the F222M
filter (2.2 micron). MULTIACCUM readout mode, 64-second exposure. Mosaic of 6
dithered pointings in a spiral pattern (NIC-SPIRAL-DITH). Proposal 7215,
PI Rodger Thompson. Calibrated through CALNICB pipeline. The original is the
NASA FITS sample `NICMOSn4hk12010_mos.fits`
(https://fits.gsfc.nasa.gov/samples/NICMOSn4hk12010_mos.fits, 1,198,080
bytes), which this corpus also holds intact as `nasa-samples/HST_NICMOS.fits`.

## Known Defect: Corrupted Copy

This copy is damaged. It matches the original after a text round trip: the
bytes were decoded as UTF-8 with backslash escapes for invalid sequences and
re-encoded (most bytes >= 0x80 became the four ASCII characters `\xNN`), and
spaces and tabs before newline bytes were also dropped. Only HDU 0 and the SCI
header are still at their correct offsets. The SCI data reads as garbage
(values up to 3.4e38, where the original spans -1.09 to 2731), and the ERR,
DQ, SAMP and TIME headers no longer start on 2880-byte boundaries, so readers
find only 2 HDUs. Use `nasa-samples/HST_NICMOS.fits` for a valid copy. The
structure below describes the original.

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

2,453,667 bytes (2.3 MB) for this corrupted copy; the original is 1,198,080 bytes
