# Generates layout.fits and card36.fits (astropy; reproduces them byte for byte with astropy 8.0.1 and 8.0.3).
import numpy as np, sys
from astropy.io import fits
out = sys.argv[1]

# layout.fits: a BINTABLE whose heap (3000 B) pushes its data unit to a second
# 2880-byte block, followed by an IMAGE extension that must be found after it.
col = fits.Column(name="SAMPLES", format="PJ()", array=np.array([np.arange(750, dtype=np.int32)], dtype=object))
tab = fits.BinTableHDU.from_columns([col], name="HEAPTAB")
img = fits.ImageHDU(data=np.arange(12, dtype=np.int16).reshape(3, 4) * 7 - 20, name="AFTER")
fits.HDUList([fits.PrimaryHDU(), tab, img]).writeto(f"{out}/layout.fits", overwrite=True)

# card36.fits: a primary image whose header holds exactly 36 cards before END
# (so END opens a second header block), with non-trivial BSCALE and BZERO.
raw = (np.arange(15, dtype=np.int16).reshape(3, 5) * 3 - 7)
h = fits.PrimaryHDU(data=raw, do_not_scale_image_data=True)
h.header["BSCALE"] = 0.5
h.header["BZERO"] = 100.0
h.header["OBSERVER"] = ("O'Brien / night 2", "quote and slash inside the value")
n = len(h.header)
for i in range(36 - n):
    h.header.add_history(f"padding card {i}")
assert len(h.header) == 36, len(h.header)
h.writeto(f"{out}/card36.fits", overwrite=True)
