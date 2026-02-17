# iter_b.fit

**Source**: HEASARC cfitsio test suite (https://github.com/HEASARC/cfitsio)

**Description**: Iterator test file for cfitsio's iterator API. Contains a binary
table with mixed column types including a large array column, used to exercise
the iterator on wide rows with heterogeneous data types.

**HDU structure**:
- HDU 0: Primary (BITPIX=16, NAXIS=0, empty)
- HDU 1: BINTABLE "iter_test" -- 3 columns (Avalue/20A, Lvalue/1L, Evalue/1000E), 100 rows

**FITS features exercised**:
- Fixed-width ASCII string column (20A)
- Logical/boolean column (1L) with physical units (m**2)
- Large vector column (1000E floats per cell)
- Wide row width (4021 bytes/row)
- Physical unit annotations (TUNIT keywords)

**File size**: 408960 bytes (399.4 KB)
