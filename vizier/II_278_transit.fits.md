# II_278_transit.fits

## Source

VizieR astronomical catalog service (https://vizier.cds.unistra.fr/). Catalog II/278:
transits observed in OGLE 2001-2003 (Udalski+, 2002-2004). Exported via the VizieR
binary FITS table interface.

## HDU Structure

| HDU | Type     | Details                          | BITPIX |
|-----|----------|----------------------------------|--------|
| 0   | Primary  | Empty (NAXIS=0)                  | 8      |
| 1   | BINTABLE | 11 columns x 177 rows (EXTNAME: II_278_transit) | 8 |

Row width is 64 bytes (11,328 bytes of table data).

## FITS Features Exercised

- **LONGSTRN / CONTINUE** long string convention (`LONGSTRN = 'OGIP 1.0'`)
- **Multiple INFO keywords** with VizieR metadata (IVOID, bibcode, publisher, rights)
- **UCD keywords** (Unified Content Descriptors) on every column (e.g. `UCD__1 = 'meta.id;meta.main'`)
- **TDISP** display format keywords alongside TFORM
- **Mixed column types**: strings (`11A`, `3A`), doubles (`D`), floats (`E`), short int (`I`), 32-bit int (`J`)
- **CDS-CAT / CDS-NAME / EXTNAME** VizieR-specific table identification

## File Size

23 KB
