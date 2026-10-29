/* Write cfitsio_keys_and_unsigned.fits with cfitsio's own writing routines.
 *
 * The file is the reference for header and column cases that the MWA chain
 * (mwalib, Marlu, Birli, mwa_hyperdrive) writes or reads through cfitsio but
 * that no MWA test file contains: commentary text longer than one card,
 * LONGSTRN and CONTINUE long strings, HIERARCH keywords, numeric cards read
 * back as strings, unsigned and signed-byte table columns stored with TZERO,
 * and bit (X) columns.
 *
 *   gcc -O2 -o make_cfitsio_fixture make_cfitsio_fixture.c -lcfitsio
 *   ./make_cfitsio_fixture cfitsio_keys_and_unsigned.fits
 *
 * cfitsio writes no DATE or CHECKSUM here, so the output depends only on the
 * cfitsio version (4.3.1 for the committed file).
 */
#include <stdio.h>
#include <stdlib.h>
#include <fitsio.h>

static void check(int status, const char *what)
{
    if (status) {
        fprintf(stderr, "%s: ", what);
        fits_report_error(stderr, status);
        exit(1);
    }
}

/* Deterministic printable text of length n: "<n>:" then the alphabet,
 * digits and a space, repeating, so a split point is visible in the cards. */
static char *text(int n)
{
    static const char cycle[] = "abcdefghijklmnopqrstuvwxyz0123456789 ";
    char *s = malloc(n + 1);
    int k = snprintf(s, n + 1, "%d:", n);
    for (int i = k; i < n; i++)
        s[i] = cycle[(i - k) % (sizeof cycle - 1)];
    s[n] = '\0';
    return s;
}

int main(int argc, char **argv)
{
    if (argc != 2) {
        fprintf(stderr, "usage: %s OUT.fits\n", argv[0]);
        return 2;
    }
    fitsfile *f;
    int status = 0;
    char name[FLEN_FILENAME];
    snprintf(name, sizeof name, "!%s", argv[1]);
    fits_create_file(&f, name, &status);
    check(status, "create");

    /* HDU 0: empty primary carrying the keyword cases. */
    fits_create_img(f, BYTE_IMG, 0, NULL, &status);

    /* Numeric and logical cards, for read_key::<String> returning the
     * literal value text (ffgkys). */
    long ival = 1458492896;
    fits_update_key_lng(f, "INTKEY", ival, "integer", &status);
    fits_update_key_dbl(f, "EXPKEY", 1.5e8, -5, "%.5G format", &status);
    fits_update_key_fixdbl(f, "FIXKEY", 154.24, 2, "fixed format, 2 decimals", &status);
    fits_update_key_dbl(f, "DBLKEY", 2.1568e8, -15, "%.15G format", &status);
    fits_update_key_flt(f, "FLTKEY", 0.5f, -6, "%.6G format", &status);
    fits_update_key_log(f, "LOGKEY", 1, "logical", &status);
    fits_update_key_null(f, "NULLKEY", "a keyword with no value", &status);
    fits_update_key_str(f, "EMPTYSTR", "", "empty string", &status);
    check(status, "numeric keys");

    /* LONGSTRN and the four standard COMMENT cards (ffplsw). */
    fits_write_key_longwarn(f, &status);

    /* Long strings (ffpkls) at the one-card boundary, with and without a
     * comment, then several CONTINUE cards. Quotes inside the value are
     * doubled. */
    char *s67 = text(67), *s68 = text(68), *s69 = text(69), *s200 = text(200);
    fits_write_key_longstr(f, "SHORTSTR", "fits on one card", "short value", &status);
    fits_write_key_longstr(f, "STR67", s67, "67 characters", &status);
    fits_write_key_longstr(f, "STR68", s68, "68 characters", &status);
    fits_write_key_longstr(f, "STR67NC", s67, NULL, &status);
    fits_write_key_longstr(f, "STR68NC", s68, NULL, &status);
    fits_write_key_longstr(f, "STR69NC", s69, NULL, &status);
    fits_write_key_longstr(f, "STR200", s200, "200 characters", &status);
    fits_write_key_longstr(f, "QUOTES",
        "it's a value with 'quotes' placed so that one doubled quote falls near the split point of the card's text",
        "embedded quotes", &status);
    check(status, "long strings");

    /* HIERARCH keywords. cfitsio writes a name longer than 8 characters
     * as HIERARCH by itself; a name given with HIERARCH keeps its spaces. */
    fits_update_key_lng(f, "STARTTIME", ival, "9-character name, written as HIERARCH", &status);
    fits_update_key_lng(f, "HIERARCH ESO DET NDIT", 42, "explicit HIERARCH", &status);
    fits_update_key_str(f, "HIERARCH ESO OBS NAME", "short hierarch string", "HIERARCH string", &status);
    fits_write_key_longstr(f, "HIERARCH ESO OBS LONGSTR", s200, "HIERARCH long string", &status);
    check(status, "hierarch");

    /* COMMENT and HISTORY text of 10, 72, 73 and 300 characters (ffpcom,
     * ffphis). cfitsio puts 72 characters on each card. */
    int lens[] = {10, 72, 73, 300};
    for (int i = 0; i < 4; i++) {
        char *c = text(lens[i]);
        fits_write_comment(f, c, &status);
        fits_write_history(f, c, &status);
        free(c);
    }
    check(status, "commentary");

    /* HDU 1: binary table of unsigned, signed-byte and bit columns. cfitsio
     * stores U, V, W and S as I, J, K and B with TZERO. */
    char *ttype[] = {"U16", "U32", "U64", "I8", "U16VEC", "FLAG", "BITS"};
    char *tform[] = {"1U", "1V", "1W", "1S", "3U", "1X", "11X"};
    fits_create_tbl(f, BINARY_TBL, 0, 7, ttype, tform, NULL, "UNSIGNED", &status);
    check(status, "create table");

    unsigned short u16[] = {0, 1, 32767, 32768, 65535};
    unsigned int u32[] = {0u, 1u, 2147483647u, 2147483648u, 4294967295u};
    unsigned long long u64[] = {0ull, 1ull, 9223372036854775807ull, 9223372036854775808ull, 18446744073709551615ull};
    signed char i8[] = {-128, -1, 0, 1, 127};
    unsigned short u16vec[] = {0, 32768, 65535, 1, 2, 3, 65534, 32767, 4, 5, 6, 7, 100, 200, 300};
    char flag[] = {0, 1, 0, 1, 1};
    char bits[5 * 11];
    for (int r = 0; r < 5; r++)
        for (int b = 0; b < 11; b++)
            bits[r * 11 + b] = ((r + 1) * (b + 3)) % 3 == 0;

    fits_write_col(f, TUSHORT, 1, 1, 1, 5, u16, &status);
    fits_write_col(f, TUINT, 2, 1, 1, 5, u32, &status);
    fits_write_col(f, TULONGLONG, 3, 1, 1, 5, u64, &status);
    fits_write_col(f, TSBYTE, 4, 1, 1, 5, i8, &status);
    fits_write_col(f, TUSHORT, 5, 1, 1, 15, u16vec, &status);
    fits_write_col_bit(f, 6, 1, 1, 1, &flag[0], &status);
    /* Rows 2..5 of FLAG one row at a time at a row offset, as Birli's mwaf
     * writer does with ffpclx. */
    for (int r = 1; r < 5; r++)
        fits_write_col_bit(f, 6, r + 1, 1, 1, &flag[r], &status);
    for (int r = 0; r < 5; r++)
        fits_write_col_bit(f, 7, r + 1, 1, 11, &bits[r * 11], &status);
    check(status, "write columns");

    fits_close_file(f, &status);
    check(status, "close");
    free(s67);
    free(s68);
    free(s69);
    free(s200);
    return 0;
}
