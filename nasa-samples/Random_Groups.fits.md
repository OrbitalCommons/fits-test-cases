# Random_Groups.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html)

**Instrument/Mission**: VLA (Very Large Array) radio interferometry. This is a visibility (UV) dataset from AIPS (Astronomical Image Processing System) containing L-band (1420 MHz) radio interferometric observations with 28 antennas. The random groups format is the traditional FITS encoding for radio interferometric visibility data.

**Object**: 3C161 (radio source), observed 1984-01-29.

## HDU Structure

| HDU | Type          | Axes / Dimensions   | Description                                   |
|-----|---------------|---------------------|-----------------------------------------------|
| 0   | Random Groups | [3, 4, 1, 1, 1] x 7956 groups, 6 params | Visibility data (COMPLEX, STOKES, FREQ, RA, DEC) |
| 1   | BINTABLE      | 12 cols x 28 rows   | AIPS AN (antenna) table                       |

## FITS Features Exercised

- **Random groups format** (GROUPS = T, NAXIS1 = 0, PCOUNT = 6, GCOUNT = 7956)
- Group parameters: UU, VV, WW (baseline coordinates), BASELINE, DATE (2-part)
- PSCAL/PZERO scaling on group parameters
- 6-dimensional data axes (NAXIS = 6, with NAXIS1 = 0)
- Binary table extension with antenna positions (STABXYZ in meters)
- AIPS HISTORY cards documenting data provenance

**File size**: 596,160 bytes (582 KB)
