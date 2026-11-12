#!/bin/sh
# Write the fpack_* fixtures with the reference fpack (CFITSIO 4.6.4), and
# cfitsio's decode of each as little-endian f64 (`<name>.expected`).
# Usage: make_fpack_fixtures.sh <cfitsio-4.6.4 build dir> <cfitsio install prefix>
set -e
SRC=$1
PREFIX=$2
cc -O2 -I"$PREFIX/include" fpack_originals.c -L"$PREFIX/lib" -Wl,-rpath,"$PREFIX/lib" -lcfitsio -lm -o fpack_originals
cc -O2 -I"$PREFIX/include" fpack_expected.c -L"$PREFIX/lib" -Wl,-rpath,"$PREFIX/lib" -lcfitsio -lm -o fpack_expected
./fpack_originals
make() {
    name=$1 original=$2
    shift 2
    rm -f "$name.fits"
    "$SRC/fpack" "$@" -O "$name.fits" "$original.fits"
    ./fpack_expected "$name.fits[1]" "$original.fits" "$name.expected"
}
make fpack_hc_u16_s4 u16_stars -h -s 4
make fpack_hc_i16_s16 i16_stars -h -s 16
make fpack_hc_u8_s16 u8_stars -h -s 16
make fpack_plio_u16 u16_stars -p
make fpack_rice_u16 u16_stars -r
make fpack_plio_i16 i16_nonneg_stars -p
rm -f fpack_originals fpack_expected u16_stars.fits i16_stars.fits i16_nonneg_stars.fits u8_stars.fits
