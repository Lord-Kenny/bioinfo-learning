#!/usr/bin/env bash

#fastq_stats.sh: outputs the statistics of a (un)zipped fastq file

# --- check 1: was a file given? ---
if [ -z "$1" ]; then
  echo "Usage: $0 reads .fastq & .fastq.gz" >&2
  exit 1
fi

file="$1"

# --- check 2: does the file exist? ---

if [ ! -f "$file" ]; then
  echo "no .fastq file found" >&2
  exit 1
fi

# --- calculations (each one reads the file with zcat -f "$file") ---
lines=$(zcat -f "$file" | wc -l)

reads=$((lines/4))

bases=$(zcat -f "$file" | awk 'NR%4==2' | tr -d '\n' | wc -c)

gcc=$(zcat -f "$file" | awk 'NR%4==2' | tr -cd 'GgCc' | wc -c)

length=$(awk -v b="$bases" -v r="$reads" 'BEGIN{printf "%.1f", b/r}')

gc_p=$(awk -v b="$gcc" -v r="$bases" 'BEGIN{printf "%.2f", 100*b/r}')

# --- output: one tab-separated line ---
printf "%s\t%s\t%s\t%s\t%s\n" "$file" "$reads" "$bases" "$length" "$gc_p"



