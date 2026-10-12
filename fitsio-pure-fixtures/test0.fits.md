# test0.fits

## Source

Basic HST WFPC2 test image. Contains a small 40x40 pixel cutout from an
observation of a moving target (MTFLAG=T), taken 1994-05-19 with the F673N
filter. Originally from STScI calibration pipeline output (rootname U2EQ0201T).
The original is astropy's test file `test0.fits`
(https://github.com/astropy/astropy/blob/main/astropy/io/fits/tests/data/test0.fits,
57,600 bytes).

## Known Defect: Corrupted Copy

This copy is damaged. It equals the astropy original after a text round trip:
the bytes were decoded as UTF-8 with backslash escapes for invalid sequences
and re-encoded, so most bytes >= 0x80 became the four ASCII characters `\xNN`.
The headers of HDU 0 and HDU 1 read correctly, but the HDU 1 pixel data is
altered, and the headers of HDUs 2-4 no longer start on 2880-byte boundaries,
so readers find only 2 HDUs. The file is 57,612 bytes, which is not a multiple
of 2880. The structure below describes the original.

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

57,612 bytes (56 KB) for this corrupted copy; the original is 57,600 bytes
