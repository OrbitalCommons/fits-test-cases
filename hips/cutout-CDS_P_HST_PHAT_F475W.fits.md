# cutout-CDS_P_HST_PHAT_F475W.fits

## Source

HST PHAT survey cutout in the F475W filter (ACS/WFC) from the CDS hips2fits service
(https://alasky.cds.unistra.fr/hips-image-services/hips2fits).
HiPS created by CDS (Thomas Boch) from the PHAT team data. The HISTORY cards name the
HiPS `CDS/P/HST/PHAT/F475W`. The cutout is a 3000 x 3000 pixel TAN image centred on
RA = 11.048766666667, Dec = 41.625611111111 (CRVAL1/2, in M31) with 6.0000049e-5 deg
(0.216 arcsec) pixels, a 0.18 deg field. This file is byte-identical to
`samples/hips2fits/cutout-CDS_P_HST_PHAT_F475W.fits` in the Rust
[fitsrs](https://github.com/cds-astro/fitsrs) crate's test samples (in the repository
until 2025-01-29, e.g. at commit
[87c6ca6](https://github.com/cds-astro/fitsrs/tree/87c6ca698eeb2d045acc587eaee6cc7d342567c8/samples/hips2fits);
now in https://alasky.cds.unistra.fr/Aladin-Lite-test-files/fits-rs-test-files.tar).

## HDU Structure

| HDU | Type    | Dimensions  | BITPIX |
|-----|---------|-------------|--------|
| 0   | Primary | 3000 x 3000 | -32    |

Single-HDU file with a 32-bit floating-point image (36,000,000 bytes of pixel data).
2.6% of the pixels are NaN (no data).

## FITS Features Exercised

- **Full WCS** with TAN projection (`CTYPE1 = RA---TAN`, `CTYPE2 = DEC--TAN`)
- **CDELT / CRPIX / CRVAL** WCS keywords (no CD matrix)
- **RADESYS = ICRS** coordinate system declaration
- **CPYRIGHT** and **HISTORY** cards with multi-line provenance. The CPYRIGHT URL
  (`http://www.astro.washington.edu/groups/phat/Home.html`) now returns 404, and the
  HISTORY cards point to the old `alasky.u-strasbg.fr` host
- **NaN** pixels for no-data areas (no BLANK keyword, as BITPIX is -32)
- Large single-HDU float image

## File Size

36,002,880 bytes (34 MiB)
