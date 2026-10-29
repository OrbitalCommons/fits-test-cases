# 1088284872_hyperdrive_solutions.fits

**Kept on the [`mwa-v1` release](https://github.com/OrbitalCommons/fits-test-cases/releases/tag/mwa-v1)**, not in the repository: `scripts/fetch_mwa_large.sh` downloads it into `mwa-large/data/`. See [README.md](README.md) for why.

**Source**: Generated with [mwa_hyperdrive](https://github.com/MWATelescope/mwa_hyperdrive) at tag `v0.8.2` (commit `4d3a7b505b91dfc4c513c85eda7ad9ee4b68fbdb`; the binary reports `mwa_hyperdrive 0.8.1`), built with `cargo build --release --locked --features hdf5-static` (rustc 1.99.0, x86_64) against system cfitsio 4.3.1, on 2026-10-29, by [`../mwa/make_hyperdrive_solutions.sh`](../mwa/make_hyperdrive_solutions.sh). It converts the RTS calibration solutions in hyperdrive's `test_files/1088284872/1088284872_rts_sols.tar.gz` (24 `BandpassCalibration_node*.dat` and 24 `DI_JonesMatrices_node*.dat` files, unpacked into `rts/`) with that commit's metafits. From the source tree:

```bash
mkdir rts
tar -xzf test_files/1088284872/1088284872_rts_sols.tar.gz -C rts
hyperdrive solutions-convert --no-progress-bars \
    -m test_files/1088284872/1088284872.metafits \
    rts 1088284872_hyperdrive_solutions.fits
```

Two runs gave identical bytes. `solutions-convert` writes no calibration parameters and no `MODELLER` card, so the output does not depend on the CPU.

**SHA-256**: `4dbe3415d7d30ebb59d45a59fc196806bb727af4c346ac6b00dd1981868245bb`

**License**: MPL-2.0, as mwa_hyperdrive and its test data

**Description**: A hyperdrive calibration-solutions file for observation 1088284872: 128 tiles × 768 chanblocks (24 coarse channels × 32) × 1 timeblock. Tiles 3, 112–119 and 123 are flagged in TILES. 174,720 of the 786,432 Jones values are NaN. RTS solutions carry no chanblock frequencies, so every `Freq` is NaN.

As in [`../mwa/1090008640_hyperdrive_solutions.fits`](../mwa/1090008640_hyperdrive_solutions.fits.md), the CHANBLOCKS `Flag` column is `1X` written with integer values: 120 of the 768 cells hold the byte `0x01` (chanblocks 0, 1, 16, 30 and 31 of each coarse channel), which a bit read (`ffgcx`, astropy) sees as 0 and a byte read (`ffgcvb`) as 1. fitsverify reports "X vector 0x01 is not left justified".

The primary header has `LONGSTRN` and its comments, two `COMMENT` cards, `OBSID`, `SOFTWARE` and `CMDLINE` (a long string over three cards).

**Instrument/Mission**: Murchison Widefield Array (MWA), RTS calibration converted by mwa_hyperdrive

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | `LONGSTRN`, `OBSID`, `SOFTWARE`, `CMDLINE` |
| 1   | IMAGE    | 8 × 768 × 128 × 1, `float64` | SOLUTIONS | Jones matrices |
| 2   | BINTABLE | 3 cols × 128 rows | TILES | `Antenna` (1J), `Flag` (1I), `TileName` (8A: `Tile011`, …) |
| 3   | BINTABLE | 3 cols × 768 rows | CHANBLOCKS | `Index` (1J), `Flag` (1X, written as bytes 0/1), `Freq` (1D, all NaN) |

## FITS Features Exercised

- A numerically written `1X` column read as bits or bytes, over 768 rows ([fitsio-pure#150](https://github.com/OrbitalCommons/fitsio-pure/issues/150))
- `LONGSTRN`, `ffpcom` comments and an `ffpkls` long string ([fitsio-pure#149](https://github.com/OrbitalCommons/fitsio-pure/issues/149))
- A 6.3 MB `float64` image extension with NaNs, before the tables

**File size**: 6,318,720 bytes (6.0 MB)
