# gleam.fits

**Source**: MWATelescope/mwa_hyperdrive test suite (https://github.com/MWATelescope/mwa_hyperdrive)

**License**: MPL-2.0

**Description**: GLEAM (GaLactic and Extragalactic All-sky MWA) sky model catalog in FITS binary table format. Contains 4 source entries with position, flux, and spectral information. Used by hyperdrive for calibration sky model testing.

**Instrument/Mission**: Murchison Widefield Array (MWA), GLEAM survey

## HDU Structure

| HDU | Type     | Dimensions        | EXTNAME | Description                           |
|-----|----------|-------------------|---------|---------------------------------------|
| 0   | Primary  | (empty)           |         | Minimal primary header                |
| 1   | BINTABLE | 9 cols x 4 rows   |         | Source catalog (RA, Dec, flux, spectral index, etc.) |

## FITS Features Exercised

- Empty primary HDU
- Binary table with mixed column types (double, float, string)
- Astronomical catalog format

**File size**: 8,640 bytes (8.4 KB)
