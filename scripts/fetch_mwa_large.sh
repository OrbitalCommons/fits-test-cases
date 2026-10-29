#!/usr/bin/env bash
# Download the MWA files kept on the mwa-v1 release (see mwa-large/README.md)
# and verify them against the release's SHA256SUMS.
#
#   scripts/fetch_mwa_large.sh [DEST] [FILE...]
#
# DEST defaults to mwa-large/data (ignored by git). With FILE arguments, only
# those files are fetched.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:-$ROOT/mwa-large/data}"
shift || true
FITS_BENCH_RELEASE=mwa-v1 exec "$ROOT/scripts/fetch_benchmarks.sh" "$DEST" "$@"
