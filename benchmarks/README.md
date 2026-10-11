# benchmarks

Seven 6248 × 4176 (26 MP) images for timing FITS readers and writers against each other. They are too large to keep in the repository (337 MB in all), so they are attached to the [`benchmarks-v1` release](https://github.com/OrbitalCommons/fits-test-cases/releases/tag/benchmarks-v1).

Fetch them, with checksums verified, into `benchmarks/data/` (ignored by git):

```bash
scripts/fetch_benchmarks.sh                     # all seven
scripts/fetch_benchmarks.sh /tmp/bench rice_i16.fits plain_u16.fits
```

**Source**: Generated with astropy 8.0.1 by [`make_benchmarks.py`](make_benchmarks.py) on 2026-10-09. Re-running it reproduces every image pixel for pixel, and the plain and RICE_1 files byte for byte. The GZIP files' compressed bytes change from run to run, so use the published files when byte-exact inputs matter.

**License**: Synthetic data, no restrictions.

**Content**: A sky of 1000 + 50 σ Gaussian noise (`numpy` seed 1) with 300 bright 16 × 16 squares (+500 to +20,000) at random positions. The integer files clip it to 0..32767. The two plain files use their own random images (seeds 2 and 3). These files were used to time fitsio-pure against AstroBurst's reader in October 2026; both decoded every file to identical pixels.

| File | Download | Size | Compression | Pixels | Notes |
|---|---|---|---|---|---|
| `rice_i16.fits` | [link](https://github.com/OrbitalCommons/fits-test-cases/releases/download/benchmarks-v1/rice_i16.fits) | 27.6 MB | `RICE_1`, one-row tiles | `int16` | Lossless |
| `rice_f32_q16.fits` | [link](https://github.com/OrbitalCommons/fits-test-cases/releases/download/benchmarks-v1/rice_f32_q16.fits) | 22.5 MB | `RICE_1`, one-row tiles | `float32` | Quantized, `NOISEBIT = 16`, `NO_DITHER`; max error 1.66 against the source |
| `rice_f32_q4_2dtiles.fits` | [link](https://github.com/OrbitalCommons/fits-test-cases/releases/download/benchmarks-v1/rice_f32_q4_2dtiles.fits) | 16.1 MB | `RICE_1`, 64 × 64 tiles | `float32` | Quantized, `NOISEBIT = 4`, `NO_DITHER` |
| `gzip2_f32_lossless.fits` | [link](https://github.com/OrbitalCommons/fits-test-cases/releases/download/benchmarks-v1/gzip2_f32_lossless.fits) | 75.8 MB | `GZIP_2`, one-row tiles | `float32` | Bitwise lossless. astropy still writes `ZQUANTIZ = 'NO_DITHER'` (with `NOISEBIT = 0` and no `ZSCALE`/`ZZERO` columns), so a reader must not dequantize it |
| `gzip1_i32.fits` | [link](https://github.com/OrbitalCommons/fits-test-cases/releases/download/benchmarks-v1/gzip1_i32.fits) | 38.7 MB | `GZIP_1`, one-row tiles | `int32` | Lossless |
| `plain_f32.fits` | [link](https://github.com/OrbitalCommons/fits-test-cases/releases/download/benchmarks-v1/plain_f32.fits) | 104.4 MB | none | `float32` | Primary image, `1000 + 50 σ` noise |
| `plain_u16.fits` | [link](https://github.com/OrbitalCommons/fits-test-cases/releases/download/benchmarks-v1/plain_u16.fits) | 52.2 MB | none | `uint16` | Primary image, `BZERO = 32768`, uniform 0..59999 |

[`SHA256SUMS`](https://github.com/OrbitalCommons/fits-test-cases/releases/download/benchmarks-v1/SHA256SUMS):

```
45a761df164ece75d1e844755999f9235d3e2c14d4be96d201c6b2f1a5403c10  rice_f32_q16.fits
3f6df3de9c894d88b92c4c732a558fbc4209bd58cf2c866d55fa446811f0e7af  rice_i16.fits
5c8eccdf7b8fd23881d7fd6526e6c2e65ce7f2d4b3d51d18bb7b1e1cdce8b70a  gzip2_f32_lossless.fits
7a254487a306fc305ac5ecd2419d661429e64474ed5a6194d13330d988d1fe2a  gzip1_i32.fits
4220939053970a78b226b66597cf79106fb90ca8e5464d0932ff22c5c722a9c1  rice_f32_q4_2dtiles.fits
1386050c650ff579fc984ed8afb537ce649815c6b1b89199245bf9f5fcd71f97  plain_f32.fits
e19db7949c6caad6a1093a3140ab4e69db86352005ba21b98fb82fc9c00b5603  plain_u16.fits
```

The real-instrument tile-compressed frames in [`../solar-orbiter/`](../solar-orbiter/) (3040 × 3072) are a smaller benchmark kept in the repository.
