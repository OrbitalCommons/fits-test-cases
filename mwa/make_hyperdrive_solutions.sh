#!/usr/bin/env bash
# Write the two mwa_hyperdrive calibration-solutions files with mwa_hyperdrive
# v0.8.2 (commit 4d3a7b5, which reports itself as 0.8.1), using only the test
# data in that commit:
#
#   1090008640_hyperdrive_solutions.fits   (kept in this directory)
#     hyperdrive di-calibrate on the WODEN-simulated 1090008640 uvfits
#   1088284872_hyperdrive_solutions.fits   (on the mwa-v1 release)
#     hyperdrive solutions-convert of the RTS solutions for 1088284872
#
#   mwa/make_hyperdrive_solutions.sh OUTDIR [WORKDIR]
#
# Downloads the source at that commit into WORKDIR (default: a new temporary
# directory), builds it (`cargo build --release --features hdf5-static`; needs
# a C compiler, cmake and cfitsio for the fitsio crate) and runs both commands
# from the source tree with relative paths, because hyperdrive records its own
# command line in the CMDLINE card. Set HYPERDRIVE_BIN to an existing build of
# that commit to skip the download and build; HYPERDRIVE_SRC then names the
# source tree to run in.
#
# On 2026-10-29 (rustc 1.99.0, x86_64 with AVX2) two runs gave identical bytes,
# matching the SHA-256 sums in the files' .md documents. The MODELLER card
# names the CPU path ('x86_64 CPU (AVX2 available)'), so a machine without
# AVX2, or a GPU build, writes a different file.
set -euo pipefail

COMMIT=4d3a7b505b91dfc4c513c85eda7ad9ee4b68fbdb
OUT=$(realpath -m "$1")
WORK=$(realpath -m "${2:-$(mktemp -d)}")
mkdir -p "$OUT" "$WORK"

if [ -z "${HYPERDRIVE_BIN:-}" ]; then
    SRC="$WORK/mwa_hyperdrive-$COMMIT"
    if [ ! -d "$SRC" ]; then
        curl -fsSL "https://github.com/MWATelescope/mwa_hyperdrive/archive/$COMMIT.tar.gz" | tar -xz -C "$WORK"
    fi
    CARGO_TARGET_DIR="$WORK/target" cargo build --release --locked --features hdf5-static \
        --bin hyperdrive --manifest-path "$SRC/Cargo.toml"
    HYPERDRIVE_BIN="$WORK/target/release/hyperdrive"
else
    SRC=$(realpath "${HYPERDRIVE_SRC:?set HYPERDRIVE_SRC to the source tree at $COMMIT}")
fi

# Put the binary on PATH as `hyperdrive`, so CMDLINE starts with that name.
mkdir -p "$WORK/bin"
ln -sf "$(realpath "$HYPERDRIVE_BIN")" "$WORK/bin/hyperdrive"
export PATH="$WORK/bin:$PATH"
hyperdrive --version

cd "$SRC"
rm -f 1090008640_hyperdrive_solutions.fits 1088284872_hyperdrive_solutions.fits

hyperdrive di-calibrate \
    --data test_files/1090008640_WODEN/output_band01.uvfits test_files/1090008640_WODEN/1090008640.metafits \
    --source-list test_files/1090008640_WODEN/srclist_3x3_grid.txt \
    --no-beam \
    --fine-chan-flags 0 1 16 30 31 \
    --tile-flags 3 \
    --outputs 1090008640_hyperdrive_solutions.fits \
    --no-progress-bars
mv 1090008640_hyperdrive_solutions.fits "$OUT/"

rm -rf rts
mkdir rts
tar -xzf test_files/1088284872/1088284872_rts_sols.tar.gz -C rts
hyperdrive solutions-convert --no-progress-bars \
    -m test_files/1088284872/1088284872.metafits \
    rts 1088284872_hyperdrive_solutions.fits
rm -rf rts
mv 1088284872_hyperdrive_solutions.fits "$OUT/"

cd "$OUT"
sha256sum 1090008640_hyperdrive_solutions.fits 1088284872_hyperdrive_solutions.fits
