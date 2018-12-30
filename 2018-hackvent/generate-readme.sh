#!/usr/bin/env bash

set -o errexit
set -o nounset

cat intro.md > README.md
echo >> README.md
cat flags.md >> README.md
echo >> README.md
cat teaser/solution.md >> README.md
for day in 01 02 03 04 05 06 07 08 09 11 12 14 17; do
  echo >> README.md
  cat $day/solution.md >> README.md
done
pandoc README.md -o README.pdf
