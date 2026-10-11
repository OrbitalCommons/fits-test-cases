#!/usr/bin/env bash
# Download the 26 MP benchmark images from the benchmarks-v1 release and
# verify them against the release's SHA256SUMS.
#
#   scripts/fetch_benchmarks.sh [DEST] [FILE...]
#
# DEST defaults to benchmarks/data (ignored by git). With FILE arguments, only
# those files are fetched, e.g.
#   scripts/fetch_benchmarks.sh benchmarks/data rice_i16.fits plain_u16.fits
# Files already present with the right checksum are not downloaded again.
set -euo pipefail

RELEASE="${FITS_BENCH_RELEASE:-benchmarks-v1}"
BASE="https://github.com/OrbitalCommons/fits-test-cases/releases/download/${RELEASE}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:-$ROOT/benchmarks/data}"
shift || true

if command -v sha256sum >/dev/null; then
    sha256() { sha256sum "$1" | cut -d' ' -f1; }
elif command -v shasum >/dev/null; then
    sha256() { shasum -a 256 "$1" | cut -d' ' -f1; }
else
    echo "need sha256sum or shasum" >&2
    exit 1
fi

mkdir -p "$DEST"
sums="$DEST/SHA256SUMS"
curl -fsSL "$BASE/SHA256SUMS" -o "$sums"

if [ "$#" -gt 0 ]; then
    wanted=("$@")
else
    mapfile -t wanted < <(awk '{print $2}' "$sums")
fi

status=0
for name in "${wanted[@]}"; do
    want=$(awk -v f="$name" '$2 == f {print $1}' "$sums")
    if [ -z "$want" ]; then
        echo "$name: not in $RELEASE" >&2
        status=1
        continue
    fi
    path="$DEST/$name"
    if [ -f "$path" ] && [ "$(sha256 "$path")" = "$want" ]; then
        echo "$name: present"
        continue
    fi
    echo "$name: downloading"
    curl -fL --progress-bar "$BASE/$name" -o "$path.part"
    if [ "$(sha256 "$path.part")" != "$want" ]; then
        echo "$name: checksum mismatch" >&2
        rm -f "$path.part"
        status=1
        continue
    fi
    mv "$path.part" "$path"
done
exit "$status"
