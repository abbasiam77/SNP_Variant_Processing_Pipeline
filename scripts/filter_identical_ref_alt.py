from Bio import SeqIO

# Path to the combined REF and ALT file
combined_file = "path_to_Combined_REF_ALT_marked.fa"

# Write the filtered file
with open("path_to_Filtered_Combined_REF_ALT_marked.fa", "w") as output:
    for record in SeqIO.parse(combined_file, "fasta"):
        # Check if REF and ALT differ at the SNP position
        if "_REF" in record.id:
            ref_seq = str(record.seq)
            alt_seq = str(next(SeqIO.parse(combined_file, "fasta")).seq)
            if ref_seq != alt_seq:
                output.write(f">{record.id}\n{ref_seq}\n")
                output.write(f">{record.id.replace('_REF', '_ALT')}\n{alt_seq}\n")
