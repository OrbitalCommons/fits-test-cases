# cfitsio_keys_and_unsigned.fits

**Source**: Generated on 2026-10-29 by [`make_cfitsio_fixture.c`](make_cfitsio_fixture.c) in this directory, linked against cfitsio 4.3.1 (Ubuntu `libcfitsio10t64` 4.3.1-1.1build2):

```bash
gcc -O2 -o make_cfitsio_fixture make_cfitsio_fixture.c -lcfitsio
./make_cfitsio_fixture cfitsio_keys_and_unsigned.fits
```

cfitsio writes no `DATE` or `CHECKSUM` here, so with the same cfitsio version the program reproduces the file byte for byte (two runs compared equal). Synthetic: every value comes from the program.

**SHA-256**: `2be34e24aa92b4d06089978c3f4ebd290644b739a63af69ad646646289b3950f`

**License**: Synthetic data, no restrictions.

**Description**: The reference for header and column cases that the MWA chain (mwalib, Marlu, Birli, mwa_hyperdrive) writes or reads through cfitsio but that no MWA test file contains, written by cfitsio's own routines so that a writer can be compared with it card for card. It was made for the fitsio-pure issues from porting that chain off cfitsio.

The program writes text of a given length as `<n>:` followed by `abc…xyz0…9 ` repeated, so the split points are visible.

Cards in the primary header, in order:

| Cards | Routine | What it shows |
|---|---|---|
| `INTKEY`, `EXPKEY`, `FIXKEY`, `DBLKEY`, `FLTKEY`, `LOGKEY`, `NULLKEY`, `EMPTYSTR` | `ffukyj`, `ffukyd` (decimals -5, -15), `ffukfd`, `ffukye`, `ffukyl`, `ffukyu`, `ffukys` | The literal text a numeric card holds: `1458492896`, `1.5E+08`, `154.24`, `215680000.`, `0.5`, `T`, no value, and an empty string, which cfitsio pads to `'        '` |
| `LONGSTRN` + 4 `COMMENT` | `ffplsw` | `LONGSTRN = 'OGIP 1.0'` and the four standard comment cards |
| `SHORTSTR` | `ffpkls` | A long-string call whose value fits one card |
| `STR67`, `STR68` | `ffpkls` with a comment | With a comment, even 67 characters end in `&` and an empty `CONTINUE ''` that carries the comment; 68 continue with `'1'` |
| `STR67NC`, `STR68NC`, `STR69NC` | `ffpkls`, no comment | Without a comment, 68 characters fit one card (the closing quote in column 80) and 69 need a `CONTINUE` |
| `STR200` | `ffpkls` | Three `CONTINUE` cards, the last empty with the comment |
| `QUOTES` | `ffpkls` | Embedded quotes doubled (`it''s`), a split between them |
| `HIERARCH STARTTIME` | `ffukyj` | cfitsio writes a 9-character name as `HIERARCH` by itself |
| `HIERARCH ESO DET NDIT`, `HIERARCH ESO OBS NAME` | `ffukyj`, `ffukys` | Explicit `HIERARCH` names with spaces; note `=     42`, not right-justified to column 30 |
| `HIERARCH ESO OBS LONGSTR` | `ffpkls` | A `HIERARCH` long string: `= '` after the name, then three `CONTINUE` cards |
| `COMMENT` / `HISTORY` of 10, 72, 73 and 300 characters | `ffpcom`, `ffphis` | cfitsio puts 72 characters on each card: 72 fit one card, 73 give a second card holding `6`, 300 give five cards |

The `UNSIGNED` table has five rows:

| Column | Requested `TFORM` | Written as | Values (rows 1–5) |
|---|---|---|---|
| `U16` | `1U` | `1I`, `TZERO = 32768` | 0, 1, 32767, 32768, 65535 |
| `U32` | `1V` | `1J`, `TZERO = 2147483648` | 0, 1, 2147483647, 2147483648, 4294967295 |
| `U64` | `1W` | `1K`, `TZERO = 9223372036854775808` | 0, 1, 2^63 − 1, 2^63, 2^64 − 1 |
| `I8` | `1S` | `1B`, `TZERO = -128` | -128, -1, 0, 1, 127 |
| `U16VEC` | `3U` | `3I`, `TZERO = 32768` | [0, 32768, 65535], [1, 2, 3], [65534, 32767, 4], [5, 6, 7], [100, 200, 300] |
| `FLAG` | `1X` | `1X` | 0, 1, 0, 1, 1 (row 1 written alone, then rows 2–5 one call each at a row offset, as Birli does with `ffpclx`) |
| `BITS` | `11X` | `11X` | bit b of row r (both from 0) set when `(r + 1)(b + 3)` is a multiple of 3: rows 0, 1, 3, 4 are `10010010010`, row 2 is all ones |

cfitsio also writes `TSCALn = 1` for each offset column. astropy 8.0.1 reads `U16`, `U32`, `U64` and `U16VEC` as unsigned integers with these values, and `I8` as `float64` with the right values. Bits are packed most significant first: row 1's `BITS` cell is bytes `92 40`.

## HDU Structure

| HDU | Type     | Dimensions | EXTNAME | Description |
|-----|----------|------------|---------|-------------|
| 0   | Primary  | (empty)    |         | 60 cards of keyword cases |
| 1   | BINTABLE | 7 cols × 5 rows, 24 bytes per row | UNSIGNED | Unsigned, signed-byte and bit columns |

## FITS Features Exercised

- `read_key::<String>` on integer, E-format, fixed-format, logical and null-valued cards must return the card's text ([fitsio-pure#143](https://github.com/OrbitalCommons/fitsio-pure/issues/143))
- `COMMENT` and `HISTORY` writers splitting at 72 characters, and `LONGSTRN` with its comments, byte-identical to `ffpcom`/`ffphis`/`ffplsw` ([fitsio-pure#149](https://github.com/OrbitalCommons/fitsio-pure/issues/149): strings of 10, 72, 73 and 300 characters)
- `ffpkls` long strings at the card boundary, with and without comments, and with embedded quotes ([fitsio-pure#149](https://github.com/OrbitalCommons/fitsio-pure/issues/149))
- `HIERARCH` keywords: implicit for a 9-character name, explicit with spaces, and a `HIERARCH` long string with `CONTINUE` ([fitsio-pure#102](https://github.com/OrbitalCommons/fitsio-pure/issues/102))
- Unsigned 16-, 32- and 64-bit and signed 8-bit table columns stored with `TZERO`, including a vector column, and the full range of each ([fitsio-pure#91](https://github.com/OrbitalCommons/fitsio-pure/issues/91), [#98](https://github.com/OrbitalCommons/fitsio-pure/issues/98): `ColumnDataType` with unsigned types)
- Bit (`X`) columns of 1 and 11 bits, one written row by row at an offset ([fitsio-pure#150](https://github.com/OrbitalCommons/fitsio-pure/issues/150))
- fitsverify: 0 errors, 1 warning (`NULLKEY` has a null value, as intended)

**File size**: 11,520 bytes (11.3 KB)
