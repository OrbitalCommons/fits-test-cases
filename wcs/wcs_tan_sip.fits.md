# wcs_tan_sip.fits

**Source**: Generated for [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure)'s WCS keyword layer (`wcs::WcsKeys`) by `make_wcs_keyword_fixtures.py` in this directory, with astropy 8.0.1, which also writes `<name>.wcs.json`. Synthetic data, not from an instrument.

**License**: Apache-2.0, as fitsio-pure.

**Description**: 47 x 31 `uint8` image. `RA---TAN-SIP`/`DEC--TAN-SIP` with a rotated `CDi_j`, and SIP distortion: `A_ORDER = B_ORDER = AP_ORDER = BP_ORDER = 3` with **every** coefficient `p + q <= 3`, the low-order ones (`A_0_0`, `A_1_0`, `A_0_1`, …) included: some readers drop those. The coefficients are random (seeded), not a fitted distortion, so `AP`/`BP` are not the inverse of `A`/`B`.

`wcs_tan_sip.wcs.json` holds astropy.wcs's parse of each WCS in the header: `ctype`, `cunit`, `crpix`, `crval`, `cdelt`, `pc`, `cd` (astropy's pixel scale matrix: the linear part as one CD matrix, whichever form the header used), `has_cd`/`has_pc`/`has_crota`, the celestial (`lng`, `lat`) and spectral (`spec`) axis indices (0-based, -1 for none), `lonpole`, `latpole`, `radesys`, `equinox`, the SIP matrices (`a[p][q]` is `A_p_q`), and truth points: FITS 1-based `pixel` and astropy's `all_pix2world` `world`. This file has 1 WCS (primary) and 5 truth points.

Non-degenerate on purpose: non-square images, non-unit and non-diagonal linear parts, and a non-zero rotation.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | 47 x 31 | | `BITPIX = 8` image with the WCS cards |

## FITS Features Exercised

- SIP `A_p_q`/`B_p_q`/`AP_p_q`/`BP_p_q`, all terms to order 3 including `p + q < 2`
- `-SIP` CTYPE suffix
- `CDi_j` (rotated)

**File size**: 8,640 bytes; `.wcs.json` 2,871 bytes. **SHA-256**: `042eecc9d1f65dc2e6d36ba5055f5200a91be6f707a1b47b76729813be3f9019`
