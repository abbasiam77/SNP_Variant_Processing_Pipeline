# SNP Sequence Annotation and Filtering Pipeline

This repository provides a modular pipeline to process SNP BED data and generate FASTA sequences for both reference (REF) and alternate (ALT) alleles, with SNP positions annotated. The final output is a filtered FASTA file that includes only those SNPs where the REF and ALT alleles differ at the specified site.

## 🚀 Workflow Overview

1. **Start with a BED file** containing at least 5 columns:  
   `chr`, `start`, `end`, `snp_id`, and `alleles` (e.g., `A/G`, `T/C`, or `rsID-A`).

2. **Clean and sort** the BED file.

3. **Extract 270bp reference sequences** (±135bp around SNP position) using `bedtools getfasta`.

4. **Generate ALT sequences** by replacing the middle base with the risk allele.

5. **Mark the SNP position** with brackets (`[...]`) in both REF and ALT sequences.

6. **Combine** the REF and ALT sequences into one FASTA file, in alternating order.

7. **Filter out** SNPs where the REF and ALT sequences are identical at the SNP position.

---

## 🛠️ Requirements

- Python ≥ 3.6
- [Biopython](https://biopython.org/)
- [bedtools](https://bedtools.readthedocs.io/en/latest/)
- [samtools](http://www.htslib.org/)

### Genome Reference Files

You need the reference genome (e.g., `hg38.fa`) and its index (`hg38.fa.fai`). You can download and prepare them using:

```bash
wget http://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz
gunzip hg38.fa.gz
samtools faidx hg38.fa
