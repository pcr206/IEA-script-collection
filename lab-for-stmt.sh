#!/bin/bash


# To check the filename provided at runtime

#if [[ $# -lt 2 ]]; then
#	echo "Need two or more filename with space to check in directory!"
#       	exit 1
#fi

[[ $# -lt 2 ]] && { echo "Need more than 2 file" >&2; exit 1; }

# Check file status in current directory

for filename in $*; do
	if [[ ! -f  ${filename} ]]; then
        	echo "File: ${filename} doesn't exist in current directory."
	else 
		size=`du -sk $filename | cut -f1`
		if [[ $size -eq 0 ]];  then 
			echo "$filename is empty and going to remove"
			rm -rf $filename
		else
			echo "Inspected by  `whoami | cut -f2 -d '\'` on `date`" >> $filename
		fi
	fi
done

exit 0
