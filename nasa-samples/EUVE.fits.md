# EUVE.fits

**Source**: NASA GSFC FITS sample files (https://fits.gsfc.nasa.gov/fits_samples.html)

**Instrument/Mission**: Extreme Ultraviolet Explorer (EUVE) satellite (1992-2001). EUVE carried four grazing-incidence telescopes that performed an all-sky survey and pointed spectroscopy in the 70-760 angstrom EUV band. This file contains Deep Survey imaging and short/medium/long wavelength spectrometer data.

**Object**: NGC 4151 (Seyfert galaxy), observed 1997-04-30 to 1997-05-07.

## HDU Structure

| HDU | Type     | Dimensions    | EXTNAME          | Description                         |
|-----|----------|---------------|------------------|-------------------------------------|
| 0   | Primary  | (empty)       |                  | Global metadata only                |
| 1   | IMAGE    | 512 x 512     | ds               | Deep Survey detector image          |
| 2   | IMAGE    | 2048 x 300    | sw_night         | Short Wavelength spectrometer       |
| 3   | IMAGE    | 2048 x 300    | mw               | Medium Wavelength spectrometer      |
| 4   | IMAGE    | 2048 x 300    | lw               | Long Wavelength spectrometer        |
| 5   | BINTABLE | 3 cols x 3    | ds_limits        | Filter limits for DS image          |
| 6   | BINTABLE | 3 cols x 2    | sw_night_limits  | Filter limits for SW image          |
| 7   | BINTABLE | 3 cols x 2    | mw_limits        | Filter limits for MW image          |
| 8   | BINTABLE | 3 cols x 2    | lw_limits        | Filter limits for LW image          |

## FITS Features Exercised

- Empty primary HDU (NAXIS = 0) with metadata only
- Multiple named IMAGE extensions (EXTNAME)
- Binary table extensions with mixed column types
- Mix of IMAGE and BINTABLE extension types in one file

**File size**: 4,291,200 bytes (4.1 MB)
