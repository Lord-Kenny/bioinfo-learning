#!/usr/bin/env python3
"""gc.py: report the length, GC % and reverse complement of a DNA sequence given on the command line."""
import sys

# the sequence is the first argument after the script name (like $1 in bash)
seq = sys.argv[1].upper()

# GC content: count G and C, divide by the length, times 100
gc = seq.count("G") + seq.count("C")
gc_pct = 100 * gc / len(seq)

# reverse complement: swap each letter, then reverse the order
complement = seq.translate(str.maketrans("ACGT", "TGCA"))
revcomp = complement[::-1]

# print three tab-separated lines
print(f"length\t{len(seq)}")
print(f"gc_pct\t{gc_pct:.2f}")
print(f"revcomp\t{revcomp}")
