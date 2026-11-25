#!/usr/bin/env python3
"""fasta_stats_bio.py: length and GC % of each FASTA record, using Biopython."""
import argparse
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


def main():
    parser = argparse.ArgumentParser(description="Report the length and GC% of each sequence in a FASTA file (Biopython version).")
    parser.add_argument("fasta", help="input FASTA file")
    args = parser.parse_args()

    print("name\tlength\tgc_pct")
    # SeqIO.parse gives one SeqRecord per sequence; gc_fraction returns 0-1, so x100 for %
    for record in SeqIO.parse(args.fasta, "fasta"):
        print(f"{record.id}\t{len(record.seq)}\t{100 * gc_fraction(record.seq):.2f}")


if __name__ == "__main__":
    main()
