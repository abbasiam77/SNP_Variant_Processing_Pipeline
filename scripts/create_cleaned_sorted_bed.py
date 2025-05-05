# This script generates a BED file with a 270bp window around SNPs.
# Modify the code to suit your sequence data.

from Bio import SeqIO

# Path to your input BED file
input_bed_file = "path_to_input_bed_file.bed"

# Output file for the 270bp sequence windows
output_bed_file = "path_to_output_bed_file_270bp.bed"

# Read input BED file and generate a new BED file with 270bp sequence windows
with open(input_bed_file, "r") as bed, open(output_bed_file, "w") as output:
    for line in bed:
        fields = line.strip().split('\t')
        chr_id, start, end, snp_id, risk_allele = fields[:5]
        # Add logic to fetch the relevant sequence from a genome file (e.g., hg38.fa)
        # Update the sequence windows to be 270bp
