# mwa-large

MWA files too large for the repository, for testing readers and writers that must seek rather than load whole files. There are two kinds:

- two files kept on the [`mwa-v1` release](https://github.com/OrbitalCommons/fits-test-cases/releases/tag/mwa-v1), 19 MB together;
- two files of more than 2 GB written on demand by [`scripts/make_large_mwa.py`](../scripts/make_large_mwa.py), which are not stored anywhere.

They were added for the [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure) issues found by porting the MWA chain (mwalib 2.0.5 → Marlu 0.19.0 → Birli 0.21.0 → mwa_hyperdrive 4d3a7b5) off cfitsio. The smaller MWA files for the same issues are in [`../mwa/`](../mwa/).

## Release files

Fetch them, with checksums verified, into `mwa-large/data/` (ignored by git):

```bash
scripts/fetch_mwa_large.sh                      # both
scripts/fetch_mwa_large.sh /tmp/mwa 1090008640.uvfits
```

| File | Download | Size | Source | Notes |
|---|---|---|---|---|
| [`1090008640.uvfits`](1090008640.uvfits.md) | [link](https://github.com/OrbitalCommons/fits-test-cases/releases/download/mwa-v1/1090008640.uvfits) | 12.9 MB | mwa_hyperdrive `test_files/1090008640/1090008640.uvfits` at `4d3a7b5`, byte-identical | Random-groups UVFITS written by Birli v0.5.0 (Marlu's writer); 8256 groups of 32 channels |
| [`1088284872_hyperdrive_solutions.fits`](1088284872_hyperdrive_solutions.fits.md) | [link](https://github.com/OrbitalCommons/fits-test-cases/releases/download/mwa-v1/1088284872_hyperdrive_solutions.fits) | 6.3 MB | Generated: `hyperdrive solutions-convert` of mwa_hyperdrive's RTS test solutions, by [`../mwa/make_hyperdrive_solutions.sh`](../mwa/make_hyperdrive_solutions.sh) | 128 tiles × 768 chanblocks; 120 chanblocks flagged in a numerically written `1X` column |

[`SHA256SUMS`](https://github.com/OrbitalCommons/fits-test-cases/releases/download/mwa-v1/SHA256SUMS):

```
9b6f9d28cc0f6fbdba17bf3da81f1615cee4624b06eba3c0d2c7b1b6c91ba0f4  1090008640.uvfits
4dbe3415d7d30ebb59d45a59fc196806bb727af4c346ac6b00dd1981868245bb  1088284872_hyperdrive_solutions.fits
```

**Why a release**: both files would add about 14 MB to every clone (they compress poorly: 9.0 and 4.7 MB gzipped) and repeat what files in [`../mwa/`](../mwa/) already test. [`1196175296.uvfits`](../mwa/1196175296.uvfits.md) is the random-groups reference in the repository, with the same five parameters and AIPS AN table, and [`1090008640_hyperdrive_solutions.fits`](../mwa/1090008640_hyperdrive_solutions.fits.md) is a smaller, more complete hyperdrive solutions file from the same program. The release copies give a second UVFITS writer (Birli's, through Marlu) and a full-size solutions file. The legacy gpubox file for [fitsio-pure#146](https://github.com/OrbitalCommons/fitsio-pure/issues/146), at 14 MB the largest of the new files, stays in the repository because it is the only real compressed image with `BSCALE ≠ 1`.

## Generated files (not stored)

[`scripts/make_large_mwa.py`](../scripts/make_large_mwa.py) writes them; it needs only Python 3 and numpy. Each value follows from its indices, so a reader can check any element without a reference copy. Output is deterministic: numpy 2.4.6 and 2.5.1 give the same bytes, and the checksums below are of the default outputs, written on 2026-10-29.

```bash
python3 scripts/make_large_mwa.py uvfits mwa-large/data/large.uvfits   # 2.4 GB, about 10 s
python3 scripts/make_large_mwa.py mwaf mwa-large/data/large.mwaf       # 2.2 GB, about 3 min
python3 scripts/make_large_mwa.py uvfits - | sha256sum                 # checksum without a disk copy
```

| Output | Size (bytes) | SHA-256 | Content |
|---|---|---|---|
| `uvfits` | 2,436,140,160 | `3a61205944b54cdd195d95532a0eae886987dbdd9cea14e7cee3673f5fbe0915` | 66,048 random groups, then an `AIPS AN` table at byte 2,436,122,880 |
| `mwaf` | 2,155,832,640 | `108ac44d30e56b489f8177f9fa912ffe06d0e9599d551ac254a5fead49b039f6` | 22,456,320 rows of a `768X` bit column, then an `OCCUPANCY` table at byte 2,155,812,480 |

Both put a table beyond byte 2³¹ (2,147,483,648), so 32-bit offsets fail on them. fitsverify 4.22 finds no errors in either; for the uvfits it gives the same four warnings as for cotter's and Birli's files (`EPOCH` deprecated, no `CTYPE1`/`CRVAL1`/`CRPIX1`). astropy 8.0.1 opens both and reads the values the formulas give.

`--timesteps` and `--chans` change the size, e.g. `--timesteps 1` for a 300 MB uvfits.

### uvfits

The layout cotter and Birli write (compare [`../mwa/1196175296.uvfits`](../mwa/1196175296.uvfits.md)): `BITPIX = -32`, `NAXIS = 6` with axes COMPLEX (3: re, im, weight) × STOKES (4) × FREQ (768, 40 kHz from 167.035 MHz) × RA × DEC, `PCOUNT = 5`, `GCOUNT = 66048`: 8 timesteps × 8256 baselines (128 tiles, autocorrelations included, `ant1 ≤ ant2`, `ant1` major). Each group is 36,884 bytes.

For group `g` (from 0) of timestep `t`, between antennas `a1 ≤ a2` (from 0), with `d = a2 − a1`, `c = 299792458` and channel `ch`, polarisation `p`:

| Value | Formula |
|---|---|
| `UU`, `VV`, `WW` | `10 d / c`, `−5 d / c`, `0.5 d / c` (no negative zeros) |
| `BASELINE` | `256 (a1 + 1) + (a2 + 1)` |
| `DATE` | stored `(t + 0.5) × 2 / 86400`, plus `PZERO5 = 2456860.5` |
| re | `g mod 65536 + p` |
| im | `ch` |
| weight | −1 when `ch mod 32` is 0 or 1, else 1 |

The `AIPS AN` table has 128 rows: `ANNAME = 'Tile000'`…`'Tile127'`, `STABXYZ = (10 i, −5 i, 0.5 i)`, `NOSTA = i + 1`, `POLTYA = 'X'`, `POLTYB = 'Y'`, all other values 0.

### mwaf

Birli's mwaf 2.0 layout (compare [`../mwa/1247842824_birli_flags_01_ts1.mwaf`](../mwa/1247842824_birli_flags_01_ts1.mwaf.md)): an empty primary with `VERSION = '2.0'`, `OBSID = 1090008640`, `NCHANS = 768`, `NANTENNA = 128`, `NSCANS = 2720`, then `FLAGS`, one `768X` column (96 bytes per row), one row per baseline per timestep, and `OCCUPANCY`, 768 rows of `Index` (1J), `Count` (1K) and `Occupancy` (1D).

Bit `c` of row `r` (both from 0) is set when `c mod 32` is 0, 1, 16, 30 or 31, or when `(31 r + 17 c) mod 101 = 0`, packed most significant bit first. `Count` is the number of rows with bit `c` set and `Occupancy` is `Count / 22456320`.

## Features exercised

- Seek-based table reads: the AN table and the OCCUPANCY table sit after more than 2 GB of data; reading them should not need memory in proportion to the file ([fitsio-pure#153](https://github.com/OrbitalCommons/fitsio-pure/issues/153): "peak RSS under ~20 MB above baseline")
- Seek-based random-groups reads, including reads spanning groups and groups beyond 2³¹ bytes ([fitsio-pure#152](https://github.com/OrbitalCommons/fitsio-pure/issues/152))
- In-place table writes: rewriting or appending rows of the `768X` column without copying the file ([fitsio-pure#151](https://github.com/OrbitalCommons/fitsio-pure/issues/151)); `--timesteps` gives a smaller file to append to
- Large random-groups writes, to compare with these bytes ([fitsio-pure#96](https://github.com/OrbitalCommons/fitsio-pure/issues/96), [#97](https://github.com/OrbitalCommons/fitsio-pure/issues/97))
- Bit columns at scale ([fitsio-pure#150](https://github.com/OrbitalCommons/fitsio-pure/issues/150))
