#!/usr/bin/env python3
"""gc.py: report length, base counts, GC % and reverse complement of a DNA sequence."""
import sys

VALID = "ACGTN"   # the letters we accept


def base_counts(seq):
    """Return a dictionary: letter -> how many times it occurs in seq."""
    counts = {"A": 0, "C": 0, "G": 0, "T": 0, "N": 0}
    for base in seq:
        counts[base] += 1
    return counts


def gc_percent(seq):
    """Return the GC content of seq as a percentage."""
    gc = seq.count("G") + seq.count("C")
    return 100 * gc / len(seq)


def reverse_complement(seq):
    """Return the reverse complement of seq (N stays N)."""
    return seq.translate(str.maketrans("ACGTN", "TGCAN"))[::-1]


# --- check 1: exactly one sequence given? ---
if len(sys.argv) != 2:
    print("Usage: python gc.py SEQUENCE", file=sys.stderr)
    sys.exit(1)

seq = sys.argv[1].upper()

# --- check 2: only DNA letters? ---
for base in seq:
    if base not in VALID:
        print(f"Error: '{base}' is not a DNA letter (allowed: {VALID})", file=sys.stderr)
        sys.exit(1)

# --- results: one tab-separated line per value ---
counts = base_counts(seq)
print(f"length\t{len(seq)}")
for base in "ACGTN":
    print(f"{base}\t{counts[base]}")
print(f"gc_pct\t{gc_percent(seq):.2f}")
print(f"revcomp\t{reverse_complement(seq)}")
