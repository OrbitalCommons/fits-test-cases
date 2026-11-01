# 1370752512_metafits_deripple_os.fits

**Source**: MWATelescope/mwalib test suite (https://github.com/MWATelescope/mwalib), `test_files/metafits_tests/1370752512_metafits_deripple_os.fits` at tag `v3.0.2` (commit `07f5e85724a5b1e45d54e5035b25810747627d4d`). Byte-identical to the file at `https://raw.githubusercontent.com/MWATelescope/mwalib/07f5e85724a5b1e45d54e5035b25810747627d4d/test_files/metafits_tests/1370752512_metafits_deripple_os.fits`, fetched 2026-11-01. Added to mwalib on 2023-08-02 (commit `42b4084`, "Added oversampling flag and deripple. Fixes #60,#61") and last changed on 2023-08-03 (commit `6fb3b4e`).

**SHA-256**: `aee2d5b0be1334aed76f9bdd0033faef4bf8acd3b23bf875224373758e5ed8cc`

**License**: MPL-2.0

**Description**: Metafits for MWAX correlator observation 1370752512 (`MODE = 'MWAX_CORRELATOR'`, `FILENAME = 'Oversamp+deripple_Sun_Ch121'`, 2023-06-14T04:34:54, 32 s, project `C001`), a commissioning test with oversampling and deripple both on. 16 long-baseline tiles (`NINPUTS = 32`, `LBF1`–`LBF8` and `LBG1`–`LBG8`), metafits version 2.2. It has only TILEDATA: no CALIBDATA and no SIGCHAINDATA, which two mwalib tests check.

Deripple is set by the older key, not by `DERIPPLE` (later metafits call `DR_FLAG` deprecated): the header has `DERIPPLE = 0`, `DR_FLAG = 1 / MWAX deripple flag: 0=OFF, 1=ON` and `DR_PARAM= 'deripplev1'` with no comment. mwalib treats deripple as on when either `DR_FLAG` or `DERIPPLE` is 1, and reports `DR_PARAM`.

**Instrument/Mission**: Murchison Widefield Array (MWA), MWAX correlator

## HDU Structure

| HDU | Type     | Dimensions        | EXTNAME  | Description |
|-----|----------|-------------------|----------|-------------|
| 0   | Primary  | (empty)           |          | Observation metadata, 73 cards; `OVERSAMP = 1`, `DR_FLAG = 1`, `DR_PARAM`; `CHANNELS` is a long string |
| 1   | BINTABLE | 19 cols × 32 rows, 243 bytes per row | TILEDATA | Inputs: the 17 older columns plus `Calib_Delay` and `Calib_Gains` (24E) |

## mwalib tests that use it (v3.0.2)

- `src/metafits_context/test.rs`: `test_deripple_on_in_metafits`, `test_oversampling_on_in_metafits`, `test_calibration_hdu_not_in_metafits`, `test_signal_chain_corrections_hdu_not_in_metafits`

## FITS Features Exercised

- Looking up HDUs by name that are not there (`CALIBDATA`, `SIGCHAINDATA`): the reader must report a missing HDU cleanly, not fail the file
- A string card with no comment (`DR_PARAM`), and an older key (`DR_FLAG = 1`) that disagrees with its replacement (`DERIPPLE = 0`)
- Numeric and logical cards read as strings ([fitsio-pure#143](https://github.com/OrbitalCommons/fitsio-pure/issues/143)): `DR_FLAG`, `OVERSAMP`, `FINECHAN = 10.0`
- NUL-padded string cells in every `TileName`, `Length` and `Flavors` cell ([fitsio-pure#144](https://github.com/OrbitalCommons/fitsio-pure/issues/144))
- CONTINUE long strings without `LONGSTRN` (`CHANNELS`)

**File size**: 23,040 bytes (22.5 KB)
