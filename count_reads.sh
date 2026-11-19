#!/usr/bin/env bash

#count_reads.sh: count reads in a zipped FASTQ

file="$1"

lines=$(zcat "$file" | wc -l)

reads=$((lines/4))

echo "$file has $reads reads"
