# wcs_crota2.fits

**Source**: Generated for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure)'s WCS keyword layer (`wcs::WcsKeys`) by `make_wcs_keyword_fixtures.py` in this directory, with astropy 8.0.1, which also writes `<name>.wcs.json`. Synthetic data, not from an instrument.

**License**: Apache-2.0, as fitsio-pure.

**Description**: 41 x 29 `uint8` image. `RA---TAN`/`DEC--TAN` in the deprecated `CDELTi` + `CROTA2` form (`CROTA2 = 23.5`, unequal `CDELTi`), `RADESYS = 'FK5'`, `EQUINOX = 2000.0`, `LONPOLE = 180.0`. No `CUNITi`: astropy reports `deg` for them.

`wcs_crota2.wcs.json` holds astropy.wcs's parse of each WCS in the header: `ctype`, `cunit`, `crpix`, `crval`, `cdelt`, `pc`, `cd` (astropy's pixel scale matrix: the linear part as one CD matrix, whichever form the header used), `has_cd`/`has_pc`/`has_crota`, the celestial (`lng`, `lat`) and spectral (`spec`) axis indices (0-based, -1 for none), `lonpole`, `latpole`, `radesys`, `equinox`, the SIP matrices (`a[p][q]` is `A_p_q`), and truth points: FITS 1-based `pixel` and astropy's `all_pix2world` `world`. This file has 1 WCS (primary) and 5 truth points.

Non-degenerate on purpose: non-square images, non-unit and non-diagonal linear parts, and a non-zero rotation.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | 41 x 29 | | `BITPIX = 8` image with the WCS cards |

## FITS Features Exercised

- `CDELTi` + `CROTA2` (Paper II eq. 189, the latitude axis's rotation)
- `RADESYS`/`EQUINOX` (FK5 J2000), `LONPOLE`
- Celestial axes without `CUNITi`

**File size**: 5,760 bytes; `.wcs.json` 1,492 bytes. **SHA-256**: `44afbccd1175a3e0213064e85ea3290542e935b18a434d5a666dec2c5bd2dc17`
