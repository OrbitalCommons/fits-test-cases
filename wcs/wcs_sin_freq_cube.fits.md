# wcs_sin_freq_cube.fits

**Source**: Generated for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure)'s WCS keyword layer (`wcs::WcsKeys`) by `make_wcs_keyword_fixtures.py` in this directory, with astropy 8.0.1, which also writes `<name>.wcs.json`. Synthetic data, not from an instrument.

**License**: Apache-2.0, as fitsio-pure.

**Description**: 7 x 5 x 3 `uint8` cube. `RA---SIN`/`DEC--SIN`/`FREQ` (`WCSAXES = 3`), a `PCi_j` that couples only the celestial axes, `CDELTi`, `CUNIT3 = 'Hz'`, `CRVAL3` at the HI line, `SPECSYS = 'LSRK'`.

`wcs_sin_freq_cube.wcs.json` holds astropy.wcs's parse of each WCS in the header: `ctype`, `cunit`, `crpix`, `crval`, `cdelt`, `pc`, `cd` (astropy's pixel scale matrix: the linear part as one CD matrix, whichever form the header used), `has_cd`/`has_pc`/`has_crota`, the celestial (`lng`, `lat`) and spectral (`spec`) axis indices (0-based, -1 for none), `lonpole`, `latpole`, `radesys`, `equinox`, the SIP matrices (`a[p][q]` is `A_p_q`), and truth points: FITS 1-based `pixel` and astropy's `all_pix2world` `world`. This file has 1 WCS (primary) and 4 truth points.

Non-degenerate on purpose: non-square images, non-unit and non-diagonal linear parts, and a non-zero rotation.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | 7 x 5 x 3 | | `BITPIX = 8` image with the WCS cards |

## FITS Features Exercised

- A spectral (non-celestial) axis, `FREQ`, in `Hz`
- Three WCS axes, `PCi_j` x `CDELTi`
- `SIN` projection

**File size**: 5,760 bytes; `.wcs.json` 1,592 bytes. **SHA-256**: `fc0fae6fc2efb28beb3c4ddeea29ae8dadf96f37dd1f42269f9b418a26f208a5`
