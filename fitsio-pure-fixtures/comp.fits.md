# comp.fits

## Source

Compressed FITS test file containing an image of NGC 1316 (Fornax A).
Optical observation, equinox 1950. Origin: AIPS/Gorilla (NRAO) 1994.

## HDU Structure

| HDU | Type     | EXTNAME          | Dimensions     | Data Size  |
|-----|----------|------------------|----------------|------------|
| 0   | Primary  | --               | (empty)        | 0 B        |
| 1   | BINTABLE | COMPRESSED_IMAGE | 1 col x 300 rows | 2,400 B + 66,896 B heap |

2 HDUs total. The BINTABLE stores a tile-compressed image using the FITS
tiled image compression convention.

## FITS Features Exercised

- FITS tile-compressed image (ZIMAGE=T)
- RICE_1 compression algorithm (ZCMPTYPE)
- Variable-length array column (TFORM1="1PB") with heap area
- Compressed 16-bit integer image (ZBITPIX=16, 440 x 300 pixels)
- Tile size: 440 x 1 (row-by-row compression)
- PCOUNT > 0 (heap storage for variable-length compressed data)
- Z-prefixed keywords: ZTENSION, ZBITPIX, ZNAXIS, ZPCOUNT, ZGCOUNT
- WCS in compressed image header (RA---SIN / DEC--SIN projection)
- Tests decompression path and variable-length array handling

## File Size

155,553 bytes (152 KB)
