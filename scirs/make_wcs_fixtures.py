"""Write the wcs_* fixtures: header-only FITS files (NAXIS = 0, WCSAXES = 2)
holding a celestial TAN WCS, and astropy.wcs's pixel <-> world truth for each
(`<name>.wcs.json`). Pixels are FITS 1-based (CRPIXn convention)."""
import json, sys
from astropy.io import fits
from astropy.wcs import WCS
import astropy

CASES = {
    # HDU 2 of astropy's test0.fits (HST WFPC2): a rotated CD matrix.
    "wcs_tan_cd_hst": (
        dict(CTYPE1="RA---TAN", CTYPE2="DEC--TAN", CRVAL1=215.584896839, CRVAL2=-12.7488294839,
             CRPIX1=212.0, CRPIX2=207.25, CD1_1=2.19546e-05, CD1_2=-5.0801e-05,
             CD2_1=-5.07551e-05, CD2_2=-2.19745e-05),
        [(1, 1), (40, 40), (20.5, 7.25), (-300, 450), (1500, -2000)],
    ),
    # A wide field, tens of degrees from the reference point, where the
    # gnomonic projection departs strongly from a linear mapping.
    "wcs_tan_cd_wide": (
        dict(CTYPE1="RA---TAN", CTYPE2="DEC--TAN", CRVAL1=150.0, CRVAL2=60.0,
             CRPIX1=512.5, CRPIX2=384.25, CD1_1=-0.01, CD1_2=0.002, CD2_1=0.0015, CD2_2=0.01),
        [(512.5, 384.25), (1, 1), (1024, 768), (2000, -900), (-1500, 1600)],
    ),
    # PCi_j with CDELTi, near the south pole, so RA wraps through 0.
    "wcs_tan_pc_cdelt": (
        dict(CTYPE1="RA---TAN", CTYPE2="DEC--TAN", CRVAL1=10.0, CRVAL2=-75.0,
             CRPIX1=100.0, CRPIX2=50.0, CDELT1=-0.02, CDELT2=0.03,
             PC1_1=0.8, PC1_2=-0.6, PC2_1=0.6, PC2_2=0.8),
        [(1, 1), (400, -300), (-250, 700)],
    ),
}

out = sys.argv[1]
for name, (cards, pixels) in CASES.items():
    hdu = fits.PrimaryHDU()
    hdu.header["WCSAXES"] = 2
    for k, v in cards.items():
        hdu.header[k] = v
    hdu.writeto(f"{out}/{name}.fits", overwrite=True)
    wcs = WCS(fits.getheader(f"{out}/{name}.fits"))
    points = []
    for px, py in pixels:
        (ra, dec), = wcs.all_pix2world([[px, py]], 1)
        (bx, by), = wcs.all_world2pix([[ra, dec]], 1)
        points.append({"pixel": [px, py], "world": [float(ra), float(dec)],
                       "pixel_back": [float(bx), float(by)]})
    with open(f"{out}/{name}.wcs.json", "w") as f:
        json.dump({"astropy": astropy.__version__, "origin": 1, "points": points}, f, indent=1)
        f.write("\n")
    print(name, len(points))
