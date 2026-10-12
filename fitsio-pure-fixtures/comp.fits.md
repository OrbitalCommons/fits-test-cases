# comp.fits

## Source

Tile-compressed FITS test file holding a synthetic 16-bit image, written with
astropy. The image is a smooth pattern of integer values from 900 to 1099
(every row starts at 1000). The header carries no OBJECT, telescope or WCS
keywords. One comment is inherited from astropy's own `comp.fits` test file
(`ZPCOUNT` / "My special PCOUNT comment"), but the pixel data differ from that
file and none of its NGC 1316 metadata is present.

## HDU Structure

| HDU | Type     | EXTNAME          | Dimensions     | Data Size  |
|-----|----------|------------------|----------------|------------|
| 0   | Primary  | --               | (empty)        | 0 B        |
| 1   | BINTABLE | COMPRESSED_IMAGE | 1 col x 300 rows | 2,400 B + 42,114 B heap |

2 HDUs total. The BINTABLE stores a tile-compressed image using the FITS
tiled image compression convention.

## FITS Features Exercised

- FITS tile-compressed image (ZIMAGE=T)
- RICE_1 compression algorithm (ZCMPTYPE), with BLOCKSIZE=32 and BYTEPIX=2 (ZNAMEn/ZVALn)
- Variable-length array column (TFORM1="1PB(176)") with heap area
- Compressed 16-bit integer image (ZBITPIX=16, ZNAXIS1 × ZNAXIS2 = 440 columns × 300 rows)
- Tile size: 440 x 1 (row-by-row compression)
- PCOUNT > 0 (heap storage for variable-length compressed data, PCOUNT=42114)
- Z-prefixed keywords: ZTENSION, ZBITPIX, ZNAXIS, ZPCOUNT, ZGCOUNT
- Tests decompression path and variable-length array handling

## File Size

51,840 bytes (51 KB)
