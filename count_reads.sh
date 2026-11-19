#!/usr/bin/env bash

#count_reads.sh: count reads in a zipped FASTQ

if [ -z "$1" ]; then
  echo "Usage: $0 reads.fastq.gz" >&2
  exit 1
fi

file="$1"

lines=$(zcat "$file" | wc -l)

reads=$((lines/4))

echo "$file has $reads reads"
