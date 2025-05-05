from Bio import SeqIO

# Load REF and ALT marked fasta files
ref_records = SeqIO.to_dict(SeqIO.parse("path_to_REF_270bp_marked.fa", "fasta"))
alt_records = SeqIO.to_dict(SeqIO.parse("path_to_ALT_270bp_marked.fa", "fasta"))

# Write the merged file
with open("path_to_Combined_REF_ALT_marked.fa", "w") as combined_out:
    for snp_id in ref_records:
        ref_record = ref_records[snp_id]
        alt_record = alt_records[snp_id]
        combined_out.write(f">{snp_id}_REF\n{ref_record.seq}\n")
        combined_out.write(f">{snp_id}_ALT\n{alt_record.seq}\n")
