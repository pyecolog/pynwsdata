#!/bin/sh

# Copyright: Please refer to the README in this source directory

ORIGIN="https://codes.wmo.int/common/unit?_format=csv&status=valid"
DEST="wmo.csv"

if ! [ -e "${DEST}" ]; then
    wget -O "${DEST}" "${ORIGIN}"
fi
