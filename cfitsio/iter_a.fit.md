# iter_a.fit

**Source**: HEASARC cfitsio test suite (https://github.com/HEASARC/cfitsio)

**Description**: Iterator test file for cfitsio's iterator API. Contains a merged
rate table built from multiple FMERGE operations on X-ray event rate data. Used
to test cfitsio's iterator-based row-by-row table processing.

**HDU structure**:
- HDU 0: Primary (BITPIX=16, NAXIS=0, empty)
- HDU 1: BINTABLE "rate" -- 3 columns (Counts/J, Time/E, Rate/E), 10000 rows

**FITS features exercised**:
- Binary table with integer and float columns
- HISTORY cards recording FMERGE provenance chain
- DEADTIME/LIVETIME observation metadata keywords
- Large row count (10000) for iterator throughput testing

**File size**: 129600 bytes (126.6 KB)
