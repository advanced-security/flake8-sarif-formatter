#!/bin/bash

set -euo pipefail

rm -rf ./build ./dist
python3 -mbuild
twine upload ./dist/* -u __token__
