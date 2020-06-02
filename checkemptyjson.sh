#!/bin/bash

for file in /home/madx/Documents/UbuntuWorkDir/python/transcripts-scraping/TVSerials/* 
#myvar = $( wc -w $file ) 
num=1
do 
	

	if [[ $( wc -w $file) -lt $num ]]
		then
			echo "${file}"
	fi

done

# do
# 	echo "${file}"

# done