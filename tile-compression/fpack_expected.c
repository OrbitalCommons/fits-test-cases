/* Decode image `fz` with cfitsio, write the pixels as little-endian f64 to
   `expected`, and print the max |error| against the uncompressed `orig`. */
#include <fitsio.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

static double *read_all(const char *path, long *n) {
    fitsfile *f;
    int status = 0, naxis, hdutype;
    long naxes[2];
    fits_open_image(&f, path, READONLY, &status);
    fits_get_img_dim(f, &naxis, &status);
    fits_get_img_size(f, 2, naxes, &status);
    *n = naxes[0] * naxes[1];
    double *v = malloc(*n * sizeof *v);
    int type;
    fits_get_img_equivtype(f, &type, &status);
    /* cfitsio's own decode in double, with no conversion to the image's
       type, then clipped to that type's range as cfitsio's fffi4i2 and
       fffi4i1 clip it. (Reading lossy HCOMPRESS u16/u8 as TUSHORT/TBYTE
       fails with NUM_OVERFLOW in cfitsio 4.6.4, which only ignores the
       overflow for TSHORT reads.) */
    fits_read_img(f, TDOUBLE, 1, *n, NULL, v, NULL, &status);
    double lo = -INFINITY, hi = INFINITY;
    if (type == USHORT_IMG) { lo = 0; hi = 65535; }
    if (type == SHORT_IMG) { lo = -32768; hi = 32767; }
    if (type == BYTE_IMG) { lo = 0; hi = 255; }
    for (long i = 0; i < *n; i++) v[i] = fmin(fmax(v[i], lo), hi);
    fits_close_file(f, &status);
    if (status) { fits_report_error(stderr, status); exit(1); }
    (void)hdutype;
    return v;
}

int main(int argc, char **argv) {
    long n, m;
    double *got = read_all(argv[1], &n), *orig = read_all(argv[2], &m), max = 0;
    long over = 0;
    for (long i = 0; i < n; i++) {
        double e = fabs(got[i] - orig[i]);
        if (e > max) max = e;
        if (e > 1000) over++;
    }
    FILE *out = fopen(argv[3], "wb");
    fwrite(got, sizeof *got, n, out); /* x86-64: little-endian */
    fclose(out);
    printf("%s: max |error| %g (%ld px > 1000)\n", argv[1], max, over);
    return 0;
}
