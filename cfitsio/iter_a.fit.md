# iter_a.fit

**Source**: HEASARC cfitsio test suite (https://github.com/HEASARC/cfitsio, `iter_a.fit` at the repo root; read by the `iter_a.c` and `iter_a.f` example programs)

**Description**: Iterator test file for cfitsio's iterator API. Contains a count
rate table whose HISTORY records a chain of FMERGE operations (1997) followed by an
ftabcopy (1998). `iter_a.c` computes the Rate column from the Counts and Time
columns. In this copy Rate already equals Counts / Time (e.g. 10 / 1 = 10,
11 / 2 = 5.5). Used
to test cfitsio's iterator-based row-by-row table processing.

**HDU structure**:
- HDU 0: Primary (BITPIX=16, NAXIS=0, empty)
- HDU 1: BINTABLE "rate" -- 3 columns (Counts/J, Time/E, Rate/E), 10000 rows

**FITS features exercised**:
- Binary table with integer and float columns
- HISTORY cards recording FMERGE provenance chain
- DEADTIME/LIVETIME observation metadata keywords (DEADTIME = 1.0, LIVETIME = 30554.5)
- Lower-case EXTNAME ('rate'); `iter_a.c` moves to it by the name "RATE", relying on case-insensitive EXTNAME matching
- Large row count (10000) for iterator throughput testing

**File size**: 129600 bytes (126.6 KB)
