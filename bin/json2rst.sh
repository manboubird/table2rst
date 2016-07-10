#!/bin/bash

SCRIPT_DIR="$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)"
LIB_DIR="${SCRIPT_DIR}/../lib"
PY_SCRIPT="${LIB_DIR}/json-converter.py"
python "${PY_SCRIPT}"
