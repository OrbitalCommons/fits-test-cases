# test0.fits

## Source

Basic HST WFPC2 test image. Contains a small 40x40 pixel cutout from an
observation of a moving target (MTFLAG=T), taken 1994-05-19 with the F673N
filter. Originally from STScI calibration pipeline output (rootname U2EQ0201T).

## HDU Structure

| HDU | Type    | EXTNAME | Dimensions | Data Size |
|-----|---------|---------|------------|-----------|
| 0   | Primary | --      | (empty)    | 0 B       |
| 1   | IMAGE   | SCI     | 40 x 40   | 3,200 B   |
| 2-4 | IMAGE   | (ext)   | --         | --        |

5 HDUs total (NEXTEND=4). Primary header is data-less. HDU 1 is a 16-bit
integer image extension.

## FITS Features Exercised

- Empty primary HDU with GROUPS=F and BSCALE/BZERO (unsigned 16-bit convention)
- IMAGE extensions with EXTNAME/EXTVER
- INHERIT=T (extension inherits primary header)
- Full WFPC2 calibration keyword suite (MASKCORR, ATODCORR, BIASCORR, etc.)
- WCS with CD matrix (CD1_1, CD1_2, CD2_1, CD2_2)
- CTYPE1="UNITLESS", CTYPE2="LINE" (non-celestial coordinate types)
- Multiple NEXTEND extensions

## File Size

57,612 bytes (56 KB)
