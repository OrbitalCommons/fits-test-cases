# glg_poshist_all_200524_v01.fit

**Source**: Fermi GBM daily data at HEASARC (https://heasarc.gsfc.nasa.gov/FTP/fermi/data/gbm/daily/2020/05/24/current/)

**License**: NASA mission data, publicly released with no usage restrictions.

**Instrument/Mission**: Fermi Gamma-ray Space Telescope (GLAST), Gamma-ray Burst Monitor.

**Description**: Spacecraft position and attitude history for 2020-05-24 (23:59:00 the previous day to 00:00:59 the next), one row per second: clock time, attitude quaternion, angular velocity, orbital position and velocity, geographic latitude and longitude, solar array angles and status flags. It is the companion to the TTE file in this directory and is what the [blink](https://github.com/hx-guo/blink) pipeline reads in `blink_fermi_gbm/src/io/poshist.rs`: `SCLK_UTC`, `QSJ_1`..`QSJ_3` (`f64`), `SC_LAT`/`SC_LON` and `POS_X`..`POS_Z` (`f32`) and `FLAGS` (`i16`).

## HDU Structure

| HDU | Type     | Dimensions            | EXTNAME        | Description                          |
|-----|----------|-----------------------|----------------|--------------------------------------|
| 0   | Primary  | (empty)               |                | Observation metadata                 |
| 1   | BINTABLE | 19 cols x 86,520 rows | GLAST POS HIST | Per-second position and attitude     |

Columns: `SCLK_UTC` (1D, s), `QSJ_1`..`QSJ_4` (1D), `WSJ_1`..`WSJ_3` (1D, rad/s), `POS_X`..`POS_Z` (1E, m), `VEL_X`..`VEL_Z` (1E, m/s), `SC_LAT`, `SC_LON` (1E, deg), `SADA_PY`, `SADA_NY` (1E, deg), `FLAGS` (1I).

## FITS Features Exercised

- Unsigned 16-bit column by the `TZERO` convention: `FLAGS` is `1I` with `TZERO19 = 32768`, `TSCAL19 = 1`
- Wide rows (106 bytes, 19 columns) mixing `D`, `E` and `I` types
- An `EXTNAME` containing spaces (`GLAST POS HIST`)
- Empty primary HDU

**File size**: 9,187,200 bytes (8.8 MB)
