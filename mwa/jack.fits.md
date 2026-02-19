# jack.fits

**Source**: MWATelescope/mwa_hyperdrive test suite (https://github.com/MWATelescope/mwa_hyperdrive)

**License**: MPL-2.0

**Description**: Sky model catalog with extended source components ("lobes"). Contains two binary table extensions: the first lists source components with position, flux, and shape parameters; the second maps components to their parent sources. Used by hyperdrive to test multi-component source model parsing.

**Instrument/Mission**: Murchison Widefield Array (MWA)

## HDU Structure

| HDU | Type     | Dimensions         | EXTNAME | Description                              |
|-----|----------|--------------------|---------|------------------------------------------|
| 0   | Primary  | (empty)            |         | Minimal primary header                   |
| 1   | BINTABLE | 17 cols x 8 rows   |         | Source components (RA, Dec, flux, shape parameters) |
| 2   | BINTABLE | 4 cols x 4 rows    |         | Source-to-component mapping              |

## FITS Features Exercised

- Multi-extension file with two binary tables
- Empty primary HDU
- Wide binary table rows (17 columns, 131 bytes/row)
- Mixed column types: double, float, integer, string
- Hierarchical data model (sources referencing components)

**File size**: 17,280 bytes (16.9 KB)
