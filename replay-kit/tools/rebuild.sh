#!/bin/sh
# Rebuild both bundles, re-point every reference.
# usage: tools/rebuild.sh [siteRoot=..]   (assets dir = <siteRoot>/assets; dashboard page = <siteRoot>/users/index.html)
set -e
cd "$(dirname "$0")/.."
ROOT="${1:-..}"
node build.mjs all
NEW_R=$(cat dist-rpv.txt); NEW_C=$(cat dist-rec.txt)
node tools/inject-tag.mjs "$ROOT" "$NEW_C"
sed -i -E "s#/assets/rpv\.[0-9a-f]+\.js#/assets/$NEW_R#" "$ROOT/users/index.html"
echo "rec=$NEW_C rpv=$NEW_R"
