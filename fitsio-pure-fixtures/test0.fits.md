# test0.fits

## Source

Basic HST WFPC2 test image. Contains a small 40x40 pixel cutout from an
observation of a moving target (MTFLAG=T), taken 1994-05-19 with the F673N
filter. Originally from STScI calibration pipeline output (rootname U2EQ0201T).
This is astropy's test file `test0.fits`
(https://github.com/astropy/astropy/blob/main/astropy/io/fits/tests/data/test0.fits),
byte-identical.

## History

Until 2026-10-11 this corpus held a corrupted copy (57,612 bytes): a text round
trip had turned the bytes >= 0x80 into the four ASCII characters `\xNN`,
altering the HDU 1 pixels and pushing HDUs 2-4 off their block boundaries. It
was replaced with astropy's original, which reproduces the corrupted copy
exactly under that round trip.

## HDU Structure

| HDU | Type    | EXTNAME | Dimensions | Data Size |
|-----|---------|---------|------------|-----------|
| 0   | Primary | --      | (empty)    | 0 B       |
| 1   | IMAGE   | SCI     | 40 x 40   | 3,200 B   |
| 2-4 | IMAGE   | SCI     | 40 x 40   | 3,200 B each |

5 HDUs total (NEXTEND=4). Primary header is data-less. HDUs 1-4 are 16-bit
integer image extensions, all with EXTNAME SCI and EXTVER 1 to 4.

## FITS Features Exercised

- Empty primary HDU with GROUPS=F and BSCALE/BZERO (unsigned 16-bit convention)
- IMAGE extensions with EXTNAME/EXTVER
- INHERIT=T (extension inherits primary header)
- Full WFPC2 calibration keyword suite (MASKCORR, ATODCORR, BIASCORR, etc.)
- WCS with CD matrix (CD1_1, CD1_2, CD2_1, CD2_2)
- CTYPE1="UNITLESS", CTYPE2="LINE" (non-celestial coordinate types) in HDU 1; HDUs 2-4 use RA---TAN/DEC--TAN
- Multiple NEXTEND extensions

## File Size

57,600 bytes (56 KB)
