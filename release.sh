#!/bin/bash

set -euo pipefail

pipenv install --dev
rm -rf ./build ./dist
pipenv run python3 -mbuild
pipenv run python3 -mtwine upload ./dist/* -u __token__
