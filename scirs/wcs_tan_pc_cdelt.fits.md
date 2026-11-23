# wcs_tan_pc_cdelt.fits

**Source**: Generated for the port of [cool-japan/scirs](https://github.com/cool-japan/scirs)'s FITS module (`scirs2-io`) onto [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure), as regression fixtures, where it checked a TAN implementation; also a truth set for any reader's WCS, whatever fitsio-pure decides on WCS (fitsio-pure#202). Written by astropy 8.0.3 with `make_wcs_fixtures.py` in this directory. Synthetic.

**License**: Apache-2.0, as fitsio-pure.

**Description**: A header-only primary HDU (`NAXIS = 0`, `WCSAXES = 2`) holding `RA---TAN`/`DEC--TAN` with `PCi_j` and `CDELTi`, near the south pole (Dec -75) so RA wraps through 0.

`wcs_tan_pc_cdelt.wcs.json` holds astropy.wcs's truth for it: 3 points, each a FITS 1-based `pixel` (as `CRPIXn` counts), astropy 8.0.3's `all_pix2world` `world` (RA, Dec in degrees), and `all_world2pix` of that back (`pixel_back`, within 3e-10 of `pixel`). The world values equal those astropy 8.0.1 gave in the scirs port's tests exactly. astropy warns that the WCS has more axes than the (empty) image; that is expected here.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | WCS keywords only |

## FITS Features Exercised

- Celestial WCS, `TAN` (gnomonic) projection
- `PCi_j` with `CDELTi`, RA wrapping through 0
- `WCSAXES` on a header with `NAXIS = 0`

**File size**: 2,880 bytes; `.wcs.json` 599 bytes. **SHA-256**: `504b784fd9e2692ed6da0de70358b67daf6c22929ee79078704ae4fb58431c52`
