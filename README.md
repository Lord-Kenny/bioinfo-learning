# bioinfo-learning
Scripts from my bioinformatics training.

## count_reads.sh
Counts the reads in a gzipped FASTQ file. Usage: ./count_reads.sh reads.fastq.gz

## fastq_stats.sh
fastq_stats.sh takes (un)zipped fastq file and outputs file name, number of reads, number of bases, mean length and GC p ercentage 
Usage: ./fastq_stats.sh reads.fastq.gz (works for .fastq and .fastq.gz)

Example output (results/fastq_stats.tsv):

| file | reads | bases | mean_len | gc_pct |
|---|---|---|---|---|
| sample_R1.fastq.gz | 25000 | 2500000 | 100.0 | 50.12 |
| sample_R2.fastq.gz | 25000 | 2500000 | 100.0 | 49.99 |
| test.fastq | 3 | 60 | 20.0 | 46.67 |

## gc.py
gc.py reports the length, GC % and reverse complement of a DNA sequence given on the command line

## fasta_stats.py
fasta_stats.py reports the length and GC % of every sequence in a FASTA file
