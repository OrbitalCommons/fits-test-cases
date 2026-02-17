# IUE_LWP.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html)

**Instrument/Mission**: International Ultraviolet Explorer (IUE), Long Wavelength Prime (LWP) camera. IUE was a UV space telescope operational 1978-1996, the longest-lived astronomical satellite at the time. The LWP camera covered 1850-3350 angstroms using a SEC Vidicon detector with low-dispersion spectroscopy. This is a NEWSIPS (New Spectral Image Processing System) extracted spectrum.

**Object**: NGC 4151, observed 1993-05-31, LWP image 25637.

## HDU Structure

| HDU | Type     | Dimensions       | EXTNAME | Description                                 |
|-----|----------|------------------|---------|---------------------------------------------|
| 0   | Primary  | (empty)          |         | Extensive header with IUE VICAR history      |
| 1   | BINTABLE | 9 cols x 1 row   | MELO    | Merged extracted low-dispersion spectrum     |

## FITS Features Exercised

- Empty primary HDU with very large header (IUE VICAR header embedded in COMMENT cards)
- Binary table with fixed-length array columns (640E, 640I for spectral arrays)
- Mixed scalar and array columns in one table row
- Spectral data columns: NET, BACKGROUND, SIGMA, QUALITY, FLUX
- Legacy date format (dd/mm/yy) and B1950 equinox

**File size**: 48,960 bytes (48 KB)
