# 1090008640_hyperdrive_solutions.fits

**Source**: Generated with [mwa_hyperdrive](https://github.com/MWATelescope/mwa_hyperdrive) at tag `v0.8.2` (commit `4d3a7b505b91dfc4c513c85eda7ad9ee4b68fbdb`; the binary reports `mwa_hyperdrive 0.8.1`), built with `cargo build --release --locked --features hdf5-static` (rustc 1.99.0, x86_64) against system cfitsio 4.3.1, from that commit's own test data, on 2026-10-29. [`make_hyperdrive_solutions.sh`](make_hyperdrive_solutions.sh) in this directory downloads, builds and runs it; two runs gave identical bytes. From the source tree:

```bash
hyperdrive di-calibrate \
    --data test_files/1090008640_WODEN/output_band01.uvfits test_files/1090008640_WODEN/1090008640.metafits \
    --source-list test_files/1090008640_WODEN/srclist_3x3_grid.txt \
    --no-beam \
    --fine-chan-flags 0 1 16 30 31 \
    --tile-flags 3 \
    --outputs 1090008640_hyperdrive_solutions.fits \
    --no-progress-bars
```

The inputs are the WODEN simulation of observation 1090008640 that hyperdrive's own `di_calibrate` integration test calibrates. The fine-channel and tile flags are there so that the `Flag` columns carry set values. `--no-beam` keeps the run independent of the 133 MB MWA FEE beam file.

**SHA-256**: `e599d802f7783f6620ccde182908f21a33797edd7792272cae1a5d85dbbac189`

**License**: MPL-2.0, as mwa_hyperdrive and its test data

**Description**: A hyperdrive calibration-solutions file ([format](https://mwatelescope.github.io/mwa_hyperdrive/defs/cal_sols_hyp.html)) for 128 tiles × 32 chanblocks × 1 timeblock. All 32 chanblocks converged; chanblocks 0, 1, 16, 30 and 31 are flagged and tile 3 is flagged, so their Jones matrices are NaN (5,336 of the 32,768 values).

The CHANBLOCKS `Flag` column is `1X`, but hyperdrive writes it with fitsio's numeric `write_col` of `i32` values (cfitsio `fits_write_col` with `TINT`), which stores the integer 1 in the cell's byte (`0x01`) rather than setting its most significant bit (`0x80`). A bit read (`ffgcx`, astropy) of this column therefore gives **0 for every row**, while a byte read (`ffgcvb`) gives 1 for chanblocks 0, 1, 16, 30, 31 (both checked with cfitsio 4.3.1). fitsverify reports "X vector 0x01 is not left justified". The bytes are what hyperdrive actually writes, and what fitsio-pure must reproduce for a numeric write to a `1X` column.

The primary header has hyperdrive's documented keys: `LONGSTRN` with its four `COMMENT` cards (`ffplsw`), two more `COMMENT` cards (`ffpcom`), the calibration parameters, and `CMDLINE` as a long string (`ffpkls`) over six cards. Two of the parameters have 9-character names, which cfitsio writes as `HIERARCH`:

```
HIERARCH UVW_MIN_L =       50.
UVW_MAX = 'inf     '
HIERARCH UVW_MAX_L = 'inf     '
```

The `MODELLER` card names the CPU path the run used (`'x86_64 CPU (AVX2 available)'`).

**Instrument/Mission**: Murchison Widefield Array (MWA), simulated (WODEN), calibrated by mwa_hyperdrive

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | `LONGSTRN`, `OBSID`, `MAXITER`, `S_THRESH`, `M_THRESH`, `UVW_MIN`, `HIERARCH UVW_MIN_L`, `UVW_MAX`, `HIERARCH UVW_MAX_L`, `BEAMTYPE`, `MODELLER`, `SOFTWARE`, `CMDLINE` |
| 1   | IMAGE    | 8 × 32 × 128 × 1, `float64` | SOLUTIONS | Jones matrices (4 complex as 8 reals) per chanblock, tile, timeblock |
| 2   | BINTABLE | 3 cols × 1 row | TIMEBLOCKS | `Start`, `End`, `Average` GPS times (all 1090008640.0) |
| 3   | BINTABLE | 3 cols × 128 rows | TILES | `Antenna` (1J), `Flag` (1I; row 3 is 1), `TileName` (8A: `00001`, …) |
| 4   | BINTABLE | 3 cols × 32 rows, 13 bytes per row | CHANBLOCKS | `Index` (1J), `Flag` (1X, written as bytes 0/1), `Freq` (1D, 167.035 MHz + 40 kHz steps) |
| 5   | IMAGE    | 32 × 1, `float64` | RESULTS | Final iteration difference per chanblock (NaN when flagged) |
| 6   | IMAGE    | 8128, `float64` | BASELINES | Baseline weights used (127 NaN: baselines with tile 3) |

## FITS Features Exercised

- A `1X` bit column written with numeric values, and reading it as bits or as bytes ([fitsio-pure#150](https://github.com/OrbitalCommons/fitsio-pure/issues/150): "the hyperdrive solutions `Flag` column reads and writes"; today it fails with "column 'Flag' is not numeric type")
- `LONGSTRN` and its standard comments, `ffpcom` comments and an `ffpkls` long string ending in an empty `CONTINUE ''` that carries the comment ([fitsio-pure#149](https://github.com/OrbitalCommons/fitsio-pure/issues/149))
- `HIERARCH` keywords written by cfitsio for a real program, one numeric and one string ([fitsio-pure#102](https://github.com/OrbitalCommons/fitsio-pure/issues/102))
- Numeric cards in several formats read as strings: `MAXITER = 50`, `S_THRESH = 1.0E-08`, `M_THRESH = 0.0001`, `UVW_MIN = 89.407550624795` ([fitsio-pure#143](https://github.com/OrbitalCommons/fitsio-pure/issues/143))
- Mixed-case column names (`Antenna`, `Flag`, `TileName`, `Index`, `Freq`) ([fitsio-pure#145](https://github.com/OrbitalCommons/fitsio-pure/issues/145))
- A 4-D `float64` image extension with NaNs, a 1-D image extension, and tables between images
- The API shapes hyperdrive uses to write these tables (`ColumnDescription` with `ColumnDataType::Bit`, `create_table`) ([fitsio-pure#91](https://github.com/OrbitalCommons/fitsio-pure/issues/91), [#98](https://github.com/OrbitalCommons/fitsio-pure/issues/98))

**File size**: 362,880 bytes (354.4 KB)
