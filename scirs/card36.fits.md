# card36.fits

**Source**: Generated for the port of [cool-japan/scirs](https://github.com/cool-japan/scirs)'s FITS module (`scirs2-io`) onto [fitsio-pure](https://github.com/OrbitalCommons/fitsio-pure), as regression fixtures. Written by astropy 8.0.1 with `make_layout_card36.py` in this directory, which reproduces it byte for byte (also with astropy 8.0.3). Synthetic data.

**License**: Apache-2.0, as fitsio-pure.

**Description**: A 5 x 3 (`NAXIS1 x NAXIS2`) `BITPIX = 16` primary image whose header holds exactly 36 cards before `END`, so `END` opens a second header block and the data starts at byte 5760. Stored values are `raw[y, x] = (5 y + x) * 3 - 7`, scaled by `BSCALE = 0.5` and `BZERO = 100`: physical rows `[96.5, 98, 99.5, 101, 102.5]`, `[104, 105.5, 107, 108.5, 110]`, `[111.5, 113, 114.5, 116, 117.5]` (astropy 8.0.3). `OBSERVER = 'O''Brien / night 2'` has a doubled quote and a slash inside the string; the header is padded to 36 cards with `HISTORY padding card n`.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | 5 x 3      |         | `BITPIX = 16`, `BSCALE = 0.5`, `BZERO = 100`, 36 cards |

## FITS Features Exercised

- `END` as the first card of a second header block (exactly 36 cards before it)
- Non-trivial `BSCALE`/`BZERO` (neither 1/0 nor an unsigned-integer offset)
- A string value with a doubled quote and a `/`

**File size**: 8,640 bytes. **SHA-256**: `a7b4f1cfca8b7ba2f75eee716e097384e1355896e23f682bbc5fbdfe5d2dbe82`
