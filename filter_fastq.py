#!/usr/bin/env python3
"""filter_fastq.py: keep reads whose mean Phred quality is at least a threshold."""
import argparse
import gzip
from Bio import SeqIO


def mean_quality(record):
    """Return the mean Phred quality of one FASTQ record."""
    qualities = record.letter_annotations["phred_quality"]   # list of numbers, e.g. [40, 39, ...]
    return sum(qualities) / len(qualities)


def main():
    parser = argparse.ArgumentParser(description="Keep FASTQ reads with mean quality at or above a threshold.")
    parser.add_argument("fastq", help="input FASTQ file (.fastq.gz)")
    parser.add_argument("output", help="output FASTQ file (plain text)")
    parser.add_argument("--min-mean-q", type=float, default=30,
                        help="minimum mean Phred quality (default: 30)")
    args = parser.parse_args()

    total = 0
    kept = []
    with gzip.open(args.fastq, "rt") as handle:
        for record in SeqIO.parse(handle, "fastq"):
            total += 1
            if mean_quality(record) >= args.min_mean_q:
                kept.append(record)
    SeqIO.write(kept, args.output, "fastq")
    print(f"kept {len(kept)} of {total} reads ({100 * len(kept) / total:.2f} %)")


if __name__ == "__main__":
    main()
