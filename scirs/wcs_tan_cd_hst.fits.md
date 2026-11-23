# wcs_tan_cd_hst.fits

**Source**: Generated for the port of [cool-japan/scirs](https://github.com/cool-japan/scirs)'s FITS module (`scirs2-io`) onto [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure), as regression fixtures, where it checked a TAN implementation; also a truth set for any reader's WCS, whatever fitsio-pure decides on WCS (fitsio-pure#202). Written by astropy 8.0.3 with `make_wcs_fixtures.py` in this directory. Synthetic.

**License**: Apache-2.0, as fitsio-pure.

**Description**: A header-only primary HDU (`NAXIS = 0`, `WCSAXES = 2`) holding the WCS of HDU 2 of astropy's `test0.fits` (an HST WFPC2 frame; astropy is BSD-3-Clause): `RA---TAN`/`DEC--TAN` with a rotated `CDi_j` matrix.

`wcs_tan_cd_hst.wcs.json` holds astropy.wcs's truth for it: 5 points, each a FITS 1-based `pixel` (as `CRPIXn` counts), astropy 8.0.3's `all_pix2world` `world` (RA, Dec in degrees), and `all_world2pix` of that back (`pixel_back`, within 3e-10 of `pixel`). The world values equal those astropy 8.0.1 gave in the scirs port's tests exactly. astropy warns that the WCS has more axes than the (empty) image; that is expected here.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | WCS keywords only |

## FITS Features Exercised

- Celestial WCS, `TAN` (gnomonic) projection
- `CDi_j` matrix (rotated, with skew)
- `WCSAXES` on a header with `NAXIS = 0`

**File size**: 2,880 bytes; `.wcs.json` 972 bytes. **SHA-256**: `a9043cc283e97fb071ffdcef28b183228e943f95f9ea86ffda7ef6ae15a55118`
