# wcs_pc_cdelt.fits

**Source**: Generated for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure)'s WCS keyword layer (`wcs::WcsKeys`) by `make_wcs_keyword_fixtures.py` in this directory, with astropy 8.0.1, which also writes `<name>.wcs.json`. Synthetic data, not from an instrument.

**License**: Apache-2.0, as fitsio-pure.

**Description**: 37 x 23 `uint8` image (`NAXIS1 x NAXIS2`). The primary WCS is `RA---TAN`/`DEC--TAN` with a rotated and skewed `PCi_j` and unequal `CDELTi`, `RADESYS = 'ICRS'`. Alternate WCS `A` (`WCSNAMEA = 'DETECTOR'`) puts linear `DETX`/`DETY` axes in millimetres in `CDi_jA` form.

`wcs_pc_cdelt.wcs.json` holds astropy.wcs's parse of each WCS in the header: `ctype`, `cunit`, `crpix`, `crval`, `cdelt`, `pc`, `cd` (astropy's pixel scale matrix: the linear part as one CD matrix, whichever form the header used), `has_cd`/`has_pc`/`has_crota`, the celestial (`lng`, `lat`) and spectral (`spec`) axis indices (0-based, -1 for none), `lonpole`, `latpole`, `radesys`, `equinox`, the SIP matrices (`a[p][q]` is `A_p_q`), and truth points: FITS 1-based `pixel` and astropy's `all_pix2world` `world`. This file has 2 WCS (primary, A) and 10 truth points.

Non-degenerate on purpose: non-square images, non-unit and non-diagonal linear parts, and a non-zero rotation.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | 37 x 23 | | `BITPIX = 8` image with the WCS cards |

## FITS Features Exercised

- `PCi_j` x `CDELTi` (non-unit, rotated, skewed)
- An alternate WCS (`A`) in `CDi_jA` form, on linear axes
- `CUNITi`, `WCSNAMEa`, `WCSAXES`

**File size**: 5,760 bytes; `.wcs.json` 2,645 bytes. **SHA-256**: `87fc8f2cda7dd07df0f86b34e93a132afe912781952eb748981109a627f5b496`
