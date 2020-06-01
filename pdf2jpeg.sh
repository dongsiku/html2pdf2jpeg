#!/bin/bash

FILENAME=$1
WITHOUT_FILE_EXTENSION="${FILENAME%.*}"
# sudo apt install xpdf
pdftoppm -jpeg -r 600 $FILENAME $WITHOUT_FILE_EXTENSION
