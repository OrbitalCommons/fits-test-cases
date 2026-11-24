"""Write the wcs/ fixtures: small, non-square images whose headers hold a WCS
in each of the linear forms (PC x CDELT, CROTA2), a TAN-SIP distortion with
every coefficient including the low-order ones, and a spectral cube, plus
`<name>.wcs.json`: astropy.wcs's parse of each WCS in the header (the primary
and any alternates), and pixel <-> world truth points.

Usage: make_wcs_keyword_fixtures.py <output dir>   (astropy >= 8)"""
import json, sys, warnings
import numpy as np
import astropy
from astropy.io import fits
from astropy.wcs import WCS

warnings.simplefilter("ignore")
out = sys.argv[1]

def image(shape, seed):
    """A small uint8 image of `shape` (numpy order, slowest axis first)."""
    return (np.arange(np.prod(shape)).reshape(shape) * seed % 251).astype(np.uint8)

def sip_cards(prefix, order, seed):
    """Every coefficient p + q <= order, the low-order ones included."""
    rng = np.random.default_rng(seed)
    cards = [(f"{prefix}_ORDER", order)]
    for p in range(order + 1):
        for q in range(order + 1 - p):
            scale = [2e-1, 3e-3, 4e-6, 6e-9][p + q]
            cards.append((f"{prefix}_{p}_{q}", float(f"{rng.normal() * scale:.6e}")))
    return cards

CASES = {
    # PC x CDELT, rotated and skewed, with unequal CDELTs; alternate WCS `A`
    # in CD form on linear axes.
    "wcs_pc_cdelt": ((23, 37), [
        ("WCSAXES", 2), ("CTYPE1", "RA---TAN"), ("CTYPE2", "DEC--TAN"),
        ("CUNIT1", "deg"), ("CUNIT2", "deg"),
        ("CRPIX1", 18.25), ("CRPIX2", 11.5), ("CRVAL1", 83.633), ("CRVAL2", 22.0145),
        ("CDELT1", -2.7e-4), ("CDELT2", 3.1e-4),
        ("PC1_1", 0.9396926), ("PC1_2", -0.3830222), ("PC2_1", 0.3420201), ("PC2_2", 0.9238795),
        ("RADESYS", "ICRS"),
        ("WCSNAMEA", "DETECTOR"), ("CTYPE1A", "DETX"), ("CTYPE2A", "DETY"),
        ("CUNIT1A", "mm"), ("CUNIT2A", "mm"),
        ("CRPIX1A", 0.5), ("CRPIX2A", 0.5), ("CRVAL1A", -4.625), ("CRVAL2A", 2.875),
        ("CD1_1A", 0.015), ("CD1_2A", 0.0004), ("CD2_1A", -0.0003), ("CD2_2A", 0.0125),
    ], [(1, 1), (37, 23), (18.25, 11.5), (5.5, 20.75), (-40, 60)]),
    # CDELT + CROTA2 (deprecated, still common), FK5 J2000 with LONPOLE.
    "wcs_crota2": ((29, 41), [
        ("CTYPE1", "RA---TAN"), ("CTYPE2", "DEC--TAN"),
        ("CRPIX1", 20.5), ("CRPIX2", 14.75), ("CRVAL1", 201.365), ("CRVAL2", -43.0191),
        ("CDELT1", -1.25e-3), ("CDELT2", 1.75e-3), ("CROTA2", 23.5),
        ("RADESYS", "FK5"), ("EQUINOX", 2000.0), ("LONPOLE", 180.0),
    ], [(1, 1), (41, 29), (20.5, 14.75), (33.3, 2.2), (-100, 250)]),
    # TAN-SIP with a rotated CD and every A/B (order 3) and AP/BP (order 3)
    # coefficient, A_0_0, A_1_0 and A_0_1 included.
    "wcs_tan_sip": ((31, 47), [
        ("CTYPE1", "RA---TAN-SIP"), ("CTYPE2", "DEC--TAN-SIP"),
        ("CRPIX1", 24.0), ("CRPIX2", 15.5), ("CRVAL1", 150.1163), ("CRVAL2", 2.2058),
        ("CD1_1", -1.6e-4), ("CD1_2", 4.1e-5), ("CD2_1", 3.7e-5), ("CD2_2", 1.55e-4),
        ("RADESYS", "ICRS"),
        *sip_cards("A", 3, 1), *sip_cards("B", 3, 2),
        *sip_cards("AP", 3, 3), *sip_cards("BP", 3, 4),
    ], [(1, 1), (47, 31), (24, 15.5), (10.5, 28.25), (-20, 60)]),
    # A spectral cube: RA---SIN / DEC--SIN / FREQ with a 3x3 PC matrix
    # coupling only the celestial axes, CUNIT3 = Hz, SPECSYS.
    "wcs_sin_freq_cube": ((3, 5, 7), [
        ("WCSAXES", 3), ("CTYPE1", "RA---SIN"), ("CTYPE2", "DEC--SIN"), ("CTYPE3", "FREQ"),
        ("CUNIT1", "deg"), ("CUNIT2", "deg"), ("CUNIT3", "Hz"),
        ("CRPIX1", 4.5), ("CRPIX2", 2.25), ("CRPIX3", 1.0),
        ("CRVAL1", 266.4168), ("CRVAL2", -29.0078), ("CRVAL3", 1.420405752e9),
        ("CDELT1", -1.5e-3), ("CDELT2", 1.2e-3), ("CDELT3", 2.44140625e4),
        ("PC1_1", 0.98), ("PC1_2", -0.17), ("PC2_1", 0.19), ("PC2_2", 0.97),
        ("RADESYS", "ICRS"), ("SPECSYS", "LSRK"),
    ], [(1, 1, 1), (7, 5, 3), (4.5, 2.25, 1), (2.5, 4.75, 2.5)]),
}

def sip_json(sip):
    if sip is None:
        return None
    def m(a):
        return None if a is None else np.asarray(a).tolist()
    return {"a_order": int(sip.a_order), "b_order": int(sip.b_order),
            "ap_order": int(sip.ap_order), "bp_order": int(sip.bp_order),
            "a": m(sip.a), "b": m(sip.b), "ap": m(sip.ap), "bp": m(sip.bp),
            "crpix": list(map(float, sip.crpix))}

for name, (shape, cards, pixels) in CASES.items():
    hdu = fits.PrimaryHDU(image(shape, 7))
    for k, v in cards:
        hdu.header[k] = v
    path = f"{out}/{name}.fits"
    hdu.writeto(path, overwrite=True)
    header = fits.getheader(path)
    entries = []
    for alt in [" "] + [a for a in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if f"CTYPE1{a}" in header]:
        w = WCS(header, key=alt)
        c = w.wcs
        entry = {
            "alt": alt.strip(),
            "naxis": int(c.naxis),
            "ctype": list(c.ctype), "cunit": [str(u) for u in c.cunit],
            "crpix": c.crpix.tolist(), "crval": c.crval.tolist(),
            "has_cd": bool(c.has_cd()), "has_pc": bool(c.has_pc()), "has_crota": bool(c.has_crota()),
            "cdelt": c.cdelt.tolist(),
            "pc": c.get_pc().tolist(),
            "cd": w.pixel_scale_matrix.tolist() if c.naxis == 2 else (np.diag(c.cdelt) @ c.get_pc()).tolist(),
            "lng": int(c.lng), "lat": int(c.lat), "spec": int(c.spec),
            "lonpole": None if np.isnan(c.lonpole) else float(c.lonpole),
            "latpole": None if np.isnan(c.latpole) else float(c.latpole),
            "radesys": c.radesys, "equinox": None if np.isnan(c.equinox) else float(c.equinox),
            "sip": sip_json(w.sip),
            "points": [],
        }
        for p in pixels:
            world = w.all_pix2world([p], 1)[0]
            entry["points"].append({"pixel": list(map(float, p)), "world": world.tolist()})
        entries.append(entry)
    with open(f"{out}/{name}.wcs.json", "w") as f:
        json.dump({"astropy": astropy.__version__, "origin": 1, "wcs": entries}, f, indent=1)
        f.write("\n")
    print(name, shape, [e["alt"] or "primary" for e in entries])
