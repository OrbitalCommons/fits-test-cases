# HST_FOS.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html)

**Instrument/Mission**: Hubble Space Telescope (HST), Faint Object Spectrograph (FOS). The FOS was a low-to-medium resolution UV/optical spectrograph operational 1990-1997. It used Digicon detectors (photon-counting linear arrays) to cover 1150-8500 angstroms. This observation used the AMBER detector with the H57 grating and B-2 aperture in spectroscopy mode.

**Object**: NGC4151-CLOUD2, observed 1993-04-22.

## HDU Structure

| HDU | Type  | Dimensions       | EXTNAME             | Description                          |
|-----|-------|------------------|---------------------|--------------------------------------|
| 0   | Primary | 2064 x 2       |                     | 32-bit float error spectra           |
| 1   | TABLE | 19 cols x 2 rows | y19g0309t.c2h.tab  | ASCII table with per-group params    |

## FITS Features Exercised

- Multi-group spectral data (2 integrations stored as NAXIS2 = 2)
- ASCII TABLE extension with mixed column formats (D25.16, E15.7, I11, A)
- GEIS-to-FITS converted file
- Calibration switch keywords (CNT_CORR, PPC_CORR, FLT_CORR, etc.)
- BUNIT = ERGS/CM**2/S/A

**File size**: 43,200 bytes (42 KB)
