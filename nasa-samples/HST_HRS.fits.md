# HST_HRS.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html), original file `samples/HRSz0yd020fm_c2f.fits`. This copy is byte-identical to the GSFC file (SHA-256 checked 2026-10-11).

**Instrument/Mission**: Hubble Space Telescope (HST), Goddard High Resolution Spectrograph (HRS/GHRS). The HRS was a UV spectrograph operational 1990-1997 that provided spectral resolutions up to R~80,000 over 1100-3200 angstroms using Digicon detectors. This observation used Detector 2 with the G160M grating and large science aperture (LSA) in accumulation mode with four-position FP-SPLIT.

**Object**: NGC 4151, observed 1992-07-04.

## HDU Structure

| HDU | Type  | Dimensions       | EXTNAME             | Description                           |
|-----|-------|------------------|---------------------|---------------------------------------|
| 0   | Primary | 2000 x 4       |                     | 32-bit float error spectra (4 groups, FILETYPE = 'ERR') |
| 1   | TABLE | 25 cols x 4 rows | z0yd020fm.c2h.tab  | ASCII table with per-group params     |

Image dimensions are given as NAXIS1 x NAXIS2 (columns x rows).

## FITS Features Exercised

- Multi-group spectral data (SDASMGNU = 4 original GEIS groups stored as NAXIS2 = 4). The groups are the four FP-SPLIT readouts: the table gives CARPOS = 50684 to 50687 and BINID = 2 for every row, so they are not separate substep bins (NBINS = 6)
- ASCII TABLE extension with 25 columns
- GEIS-to-FITS converted file
- Extensive calibration switches (DQI_CORR through VAC_CORR)
- Wavelength range 1530-1565 angstroms
- EQUINOX as string ("J2000") rather than float

**File size**: 69,120 bytes (68 KB)
