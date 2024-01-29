# Documentation for SHEBA's BRCA project

We are searching for three mutations within BRCA1 and BRCA2:

| CHROM | GENE  | MUTATION | POS      |
|-------|-------|----------|----------|
| 17    | BRCA1 | 185delAG | 43124027 |
| 17    | BRCA1 | 5382insC | 43057062 |
| 13    | BRCA2 | 6174delT | 32340300 |


## Genotypes

### BRCA1_185delAG
* The genotype data was sourced from SHEBA_Freeze_Seven.17.NF.vcf.gz, focusing on the BRCA1 gene's location. We specifically identified the position - Chr17:43124027, referencing assembley GRCh38.
* By executing the command: `gunzip -c SHEBA_Freeze_Seven.17.NF.vcf.gz | grep 43124027`, The row containing the desired variant becomes apparent, reflecting the deletion of the C and T nucleotides (A, G):

  | CHROM | POS      | ID                    | REF | ALT |
  |-------|----------|-----------------------|-----|-----|
  | 17    | 43124027 | 17_43124027_ACT_A    | ACT | A   |

### BRCA1_5382insC
* The genotype data was sourced from SHEBA_Freeze_Seven.17.NF.vcf.gz, focusing on the BRCA1 gene's location. We specifically identified the position - Chr17:43057062, referencing the GRCh38.
* By executing the command: `gunzip -c SHEBA_Freeze_Seven.17.NF.vcf.gz | grep 43057062`, The row containing the desired variant becomes apparent, reflecting the insertion of the G  nucleotide:
  
   CHROM | POS      | ID                    | REF | ALT |
  |-------|----------|-------------------|-----|-----|
  | 17    | 43057062 | 17_43057062_T_TG    | T | TG   |

## Linking Women IDs to Variant Genotyping
Following that, our objective is to generate a CSV file associating the IDs identified in the VCF header (women ID) with the variant genotyping information.
It will be accomplished through a two-step process: first, writing the VCF's headers and genotyping data to a text file at the designated location, and then, on the local machine, converting it into an .xlsx file.
  ```
  gunzip -c SHEBA_Freeze_Seven.17.NF.vcf.gz | head -44 | tail -1 > ID_Var_Gen.txt
  ```
  ```
  gunzip -c SHEBA_Freeze_Seven.17.NF.vcf.gz | grep -e 43124027 >> ID_Var_Gen.txt
  ```
## Mutation Carriers Selection: Filtering Genotyping Data
After generating a file containing the IDs to be removed ('exc_185delAG.txt'), specifically those where the genotyping begins with "0/0" concerning the desired mutation, we use bcftools to apply a filter to the genotyping file. This process retains only those individuals who carry the mutation.
```
/specific/elkon/gonicohen/bcftools-1.14/bcftools view -S ^/specific/elkon/gonicohen/exc_185delAG.txt /specific/elkon/gonicohen/SHEBA/FREEZE_1-9/SHEBA_Freeze_Seven.17.NF.vcf.gz > /specific/elkon/gonicohen/SHEBA/FREEZE_1-9/filtered_185delAG.vcf --force-samples
```
## VEP
Next, we aim to execute VEP on the refined VCF dataset, employing the following command:
```
vep --vcf -i /specific/elkon/gonicohen/SHEBA/FREEZE_1-9/filtered_185delAG_280124.vcf -o /specific/elkon/gonicohen/SHEBA/FREEZE_1-9/185delAG_after_VEP_2901.vcf --cache --dir_cache /specific/elkon/gonicohen --fields "Allele,Consequence,IMPACT,SYMBOL,Gene,Feature_type,Feature,BIOTYPE,EXON,INTRON,Protein_position,Amino_acids,Codons,Existing_variation,DISTANCE,STRAND,FLAGS" &
```
