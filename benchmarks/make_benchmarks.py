"""Write the 26 MP (6248 x 4176) benchmark files into a directory.

The published files (see README.md) are the ones these parameters produced
on 2026-10-09 with astropy 8.0.1. Re-running it reproduces every image pixel
for pixel, and the plain and RICE_1 files byte for byte; the GZIP_1 and
GZIP_2 files differ in their compressed bytes from run to run. Fetch the
published files when byte-exact inputs matter.
"""
import os
import sys

import numpy as np
from astropy.io import fits

out = sys.argv[1]
os.makedirs(out, exist_ok=True)

rng = np.random.default_rng(1)
h, w = 4176, 6248
sky = (1000 + 50 * rng.standard_normal((h, w))).astype(np.float32)
for _ in range(300):
    cy, cx = rng.integers(0, h), rng.integers(0, w)
    sky[max(0, cy - 8):cy + 8, max(0, cx - 8):cx + 8] += rng.uniform(500, 20000)
i16 = np.clip(sky, 0, 32767).astype(np.int16)

for name, data, ctype, kw in [
    ("rice_f32_q16", sky, "RICE_1", dict(quantize_level=16)),
    ("rice_i16", i16, "RICE_1", {}),
    ("gzip2_f32_lossless", sky, "GZIP_2", dict(quantize_level=0)),
    ("gzip1_i32", i16.astype(np.int32), "GZIP_1", {}),
    ("rice_f32_q4_2dtiles", sky, "RICE_1", dict(quantize_level=4, tile_shape=(64, 64))),
]:
    hdu = fits.CompImageHDU(data, compression_type=ctype, **kw)
    fits.HDUList([fits.PrimaryHDU(), hdu]).writeto(os.path.join(out, name + ".fits"), overwrite=True)

plain_f32 = (np.random.default_rng(2).standard_normal((h, w)) * 50 + 1000).astype(np.float32)
fits.PrimaryHDU(plain_f32).writeto(os.path.join(out, "plain_f32.fits"), overwrite=True)
plain_u16 = np.random.default_rng(3).integers(0, 60000, (h, w)).astype(np.uint16)
fits.PrimaryHDU(plain_u16).writeto(os.path.join(out, "plain_u16.fits"), overwrite=True)
