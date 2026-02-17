# HST_NICMOS.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html)

**Instrument/Mission**: Hubble Space Telescope (HST), Near Infrared Camera and Multi-Object Spectrometer (NICMOS). NICMOS provided infrared imaging and spectroscopy from 0.8-2.5 microns using three cameras with HgCdTe detector arrays. This is a Camera 2 mosaic observation using the F222M filter (2.2 micron) in MULTIACCUM readout mode, produced by the CALNICB pipeline.

**Object**: NGC 4151, observed 1998-05-22.

## HDU Structure

| HDU | Type  | Dimensions  | EXTNAME | Description                       |
|-----|-------|-------------|---------|-----------------------------------|
| 0   | Primary | (empty)   |         | Global metadata only              |
| 1   | IMAGE | 270 x 263   | SCI     | Science image (BITPIX = -32)      |
| 2   | IMAGE | 270 x 263   | ERR     | Error array (BITPIX = -32)        |
| 3   | IMAGE | 270 x 263   | DQ      | Data quality flags (BITPIX = 16)  |
| 4   | IMAGE | 270 x 263   | SAMP    | Number of samples (BITPIX = 16)   |
| 5   | IMAGE | 270 x 263   | TIME    | Integration time map (BITPIX = -32) |

## FITS Features Exercised

- Empty primary HDU with rich metadata
- Multiple IMAGE extensions with EXTNAME/EXTVER (SCI, ERR, DQ, SAMP, TIME)
- INHERIT = true (extensions inherit primary header)
- Mixed BITPIX across extensions (-32 and 16)
- WCS with CD matrix in each extension
- CALNICA/CALNICB calibration pipeline keywords

**File size**: 1,198,080 bytes (1.1 MB)
