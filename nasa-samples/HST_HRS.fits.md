# HST_HRS.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html)

**Instrument/Mission**: Hubble Space Telescope (HST), Goddard High Resolution Spectrograph (HRS/GHRS). The HRS was a UV spectrograph operational 1990-1997 that provided spectral resolutions up to R~80,000 over 1100-3200 angstroms using Digicon detectors. This observation used Detector 2 with the G160M grating and large science aperture (LSA) in accumulation mode with four-position FP-SPLIT.

**Object**: NGC 4151, observed 1992-07-04.

## HDU Structure

| HDU | Type  | Dimensions       | EXTNAME             | Description                           |
|-----|-------|------------------|---------------------|---------------------------------------|
| 0   | Primary | 2000 x 4       |                     | 32-bit float error spectra (4 groups) |
| 1   | TABLE | 25 cols x 4 rows | z0yd020fm.c2h.tab  | ASCII table with per-group params     |

## FITS Features Exercised

- Multi-group spectral data (4 substep bins stored as NAXIS2 = 4)
- ASCII TABLE extension with 25 columns
- GEIS-to-FITS converted file
- Extensive calibration switches (DQI_CORR through VAC_CORR)
- Wavelength range 1530-1565 angstroms
- EQUINOX as string ("J2000") rather than float

**File size**: 69,120 bytes (68 KB)
