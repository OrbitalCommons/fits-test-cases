# tb.fits

## Source

Minimal binary table test file created by STScI STSDAS/TABLES (1999-09-07).
A small synthetic test fixture with 2 rows and 4 columns.

## HDU Structure

| HDU | Type     | Dimensions     | Data Size |
|-----|----------|----------------|-----------|
| 0   | Primary  | (empty)        | 0 B       |
| 1   | BINTABLE | 4 cols x 2 rows | 24 B     |

2 HDUs total.

## Binary Table Columns

| Column | TTYPE | TFORM | Type               |
|--------|-------|-------|--------------------|
| 1      | c1    | 1J    | 32-bit integer     |
| 2      | c2    | 3A    | 3-char string      |
| 3      | c3    | 1E    | 32-bit float       |
| 4      | c4    | 1L    | logical            |

## FITS Features Exercised

- Minimal binary table with mixed column types (integer, string, float, logical)
- TSCAL3/TZERO3 scaling on a float column (TSCAL=3, TZERO=0.4)
- TNULL1 for integer null value (-2147483647)
- TDISP keywords for display formatting (I11, A3, G15.7, L6)
- Very small data payload (24 bytes) -- good for basic read validation

## File Size

8,640 bytes (8 KB)
