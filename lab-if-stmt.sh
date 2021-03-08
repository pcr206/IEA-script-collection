#!/bin/bash

# To check the filename provided at runtime

if [ ! $1 ]; then
        echo "Need filename to check in directory!"
        exit 1
fi

# [[ $1 -lt 1 ]] && { echo "Need one or more file" >&2; exit 1; }

# Get the filename at command level to verify

filename="$1"

# Check file status in current directory

if [[ ! -f  ${filename} ]]; then
        echo "File: ${filename} doesn't exist in current directory."
        exit 1
fi

exit 0
