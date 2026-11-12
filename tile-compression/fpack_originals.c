/* Uncompressed 64 x 64 frames with saturated stars, for fpack. */
#include <fitsio.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define W 64
#define H 64

/* Background plus noise plus stars whose peaks are far above `max`, clipped
   to [min, max]: flat-topped saturated cores, as in real frames. */
static void frame(double *out, double bg, double noise, double peak, double min, double max) {
    const double stars[][3] = {{14, 18, 2.5}, {40, 22, 3.5}, {25, 47, 2.0}, {52, 52, 4.0}, {8, 56, 1.5}};
    srand(7);
    for (int y = 0; y < H; y++)
        for (int x = 0; x < W; x++) {
            double v = bg + noise * ((rand() / (double)RAND_MAX) - 0.5) * 2;
            for (int s = 0; s < 5; s++) {
                double dx = x - stars[s][0], dy = y - stars[s][1], r = stars[s][2];
                v += peak * exp(-(dx * dx + dy * dy) / (2 * r * r));
            }
            out[y * W + x] = fmin(fmax(round(v), min), max);
        }
}

static void write(const char *name, int bitpix, int datatype, void *pixels) {
    fitsfile *f;
    int status = 0;
    long naxes[2] = {W, H};
    char path[256];
    snprintf(path, sizeof path, "!%s", name);
    fits_create_file(&f, path, &status);
    fits_create_img(f, bitpix, 2, naxes, &status);
    fits_write_img(f, datatype, 1, W * H, pixels, &status);
    fits_close_file(f, &status);
    if (status) { fits_report_error(stderr, status); exit(1); }
}

int main(void) {
    static double v[W * H];
    static unsigned short u16[W * H];
    static short i16[W * H];
    static unsigned char u8[W * H];
    frame(v, 1000, 40, 400000, 0, 65535);
    for (int i = 0; i < W * H; i++) u16[i] = (unsigned short)v[i];
    write("u16_stars.fits", USHORT_IMG, TUSHORT, u16);
    frame(v, -2000, 40, 300000, -32768, 32767);
    for (int i = 0; i < W * H; i++) i16[i] = (short)v[i];
    write("i16_stars.fits", SHORT_IMG, TSHORT, i16);
    frame(v, 1000, 40, 300000, 0, 32767);
    for (int i = 0; i < W * H; i++) i16[i] = (short)v[i];
    write("i16_nonneg_stars.fits", SHORT_IMG, TSHORT, i16);
    frame(v, 20, 6, 2000, 0, 255);
    for (int i = 0; i < W * H; i++) u8[i] = (unsigned char)v[i];
    write("u8_stars.fits", BYTE_IMG, TBYTE, u8);
    return 0;
}
