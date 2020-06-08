#!/bin/bash

FILENAME=$1
WITHOUT_FILE_EXTENSION="${FILENAME%.*}"
# sudo apt install xpdf
pdftoppm -jpeg -r $2 $FILENAME $WITHOUT_FILE_EXTENSION
