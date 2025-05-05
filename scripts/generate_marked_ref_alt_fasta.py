from Bio import SeqIO

# Load SNP BED info
snp_info = {}  # This will store SNP ID and associated risk allele
with open("path_to_cleaned_sorted_bed_270bp.bed") as bed:
    for line in bed:
        fields = line.strip().split('\t')
        snp_id = fields[3]
        risk_allele = fields[4].split('-')[-1]
        snp_info[snp_id] = risk_allele

# Read REF fasta and generate ALT fasta
ref_records = SeqIO.to_dict(SeqIO.parse("path_to_REF_270bp.fa", "fasta"))
with open("path_to_ALT_270bp.fa", "w") as alt_out:
    for snp_id, record in ref_records.items():
        seq = list(str(record.seq))
        if len(seq) != 270:
            continue
        seq[135] = snp_info.get(snp_id, 'N')  # Replace middle base with ALT
        alt_seq = ''.join(seq)
        alt_out.write(f">{snp_id}_ALT\n{alt_seq}\n")
