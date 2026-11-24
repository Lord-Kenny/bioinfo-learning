#!/usr/bin/env python3
"""fasta_stats.py: report the length and GC % of every sequence in a FASTA file."""
import argparse
import gzip


def read_fasta(path):
    """Read a FASTA file (.fasta or .fasta.gz) and return a dictionary: name -> sequence."""
    opener = gzip.open if path.endswith(".gz") else open
    pieces = {}      # name -> list of sequence lines
    name = None
    with opener(path, "rt") as handle:
        for line in handle:
            line = line.strip()              # remove the newline (and any Windows \r)
            if not line:                     # skip empty lines
                continue
            if line.startswith(">"):         # a header starts a new record
                name = line[1:].split()[0]   # name = first word after ">"
                pieces[name] = []
            else:                            # a sequence line: add it to the current record
                pieces[name].append(line.upper())
    # glue the lines of each record into one sequence
    sequences = {}
    for name, parts in pieces.items():
        sequences[name] = "".join(parts)
    return sequences


def gc_percent(seq):
    """Return the GC content of seq as a percentage."""
    return 100 * (seq.count("G") + seq.count("C")) / len(seq)


def main():
    parser = argparse.ArgumentParser(description="Report the length and GC% of each sequence in a FASTA file.")
    parser.add_argument("fasta", help="input FASTA file (.fasta or .fasta.gz)")
    parser.add_argument("--min-length", type=int, default=0,
                        help="only report sequences at least this long (default: 0)")
    args = parser.parse_args()

    records = read_fasta(args.fasta)
    print("name\tlength\tgc_pct")
    for name, seq in records.items():
        if len(seq) >= args.min_length:
            print(f"{name}\t{len(seq)}\t{gc_percent(seq):.2f}")


if __name__ == "__main__":
    main()
