#!/usr/bin/env python3
"""read_stats.py: one row per read (length, mean quality, GC %) for a pair of FASTQ files."""
import argparse
import gzip
import pandas as pd
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


def read_table(path, label):
    """Return a DataFrame with one row per read in a gzipped FASTQ file."""
    rows = []
    with gzip.open(path, "rt") as handle:
        for record in SeqIO.parse(handle, "fastq"):
            q = record.letter_annotations["phred_quality"]
            rows.append({"read": label,
                         "id": record.id,
                         "length": len(record.seq),
                         "mean_q": sum(q) / len(q),
                         "gc_pct": 100 * gc_fraction(record.seq)})
    return pd.DataFrame(rows)


def main():
    parser = argparse.ArgumentParser(description="Per-read statistics for paired FASTQ files.")
    parser.add_argument("r1", help="R1 FASTQ file (.fastq.gz)")
    parser.add_argument("r2", help="R2 FASTQ file (.fastq.gz)")
    parser.add_argument("-o", "--output", default="read_stats.csv", help="output CSV (default: read_stats.csv)")
    args = parser.parse_args()

    df = pd.concat([read_table(args.r1, "R1"), read_table(args.r2, "R2")], ignore_index=True)
    df.to_csv(args.output, index=False)

    summary = df.groupby("read").agg(reads=("id", "count"),
                                     bases=("length", "sum"),
                                     mean_q=("mean_q", "mean"),
                                     mean_gc=("gc_pct", "mean"))
    print(summary.round(2))
    print(f"wrote {len(df)} rows to {args.output}")


if __name__ == "__main__":
    main()
