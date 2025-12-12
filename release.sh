#!/bin/bash

set -euo pipefail

pipenv install --dev
rm -rf ./build ./dist
python3 -mbuild
python3 -mtwine upload ./dist/* -u __token__
