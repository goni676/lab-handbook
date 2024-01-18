# Documentation for SHEBA's BRCA project

## Genotypes

* The genotype data was sourced from SHEBA_Freeze_Seven.17.NF.vcf.gz, focusing on the BRCA1 gene's location. We specifically identified the position - Chr17:43124027, referencing the GRCh38.
By executing the command: `cat filtered_1705.vcf | grep 43124027`, The row containing the desired variant becomes apparent, reflecting the deletion of the C and T nucleotides (A, G):

  | CHROM | POS      | ID                    | REF | ALT |
  |-------|----------|-----------------------|-----|-----|
  | 17    | 43124027 | 17_43124027_ACT_A    | ACT | A   |


* Following that, our objective is to generate a CSV file associating the IDs identified in the VCF header (women ID) with the variant genotyping information.
  It will be accomplished through a two-step process: first, writing the VCF's headers and genotyping data to a text file at the designated location, and then, on the local machine, converting it into an .xlsx file.
  ```
  gunzip -c SHEBA_Freeze_Seven.17.NF.vcf.gz | head -44 | tail -1 > ID_Var_Gen.txt
  ```
  ```
  unzip -c SHEBA_Freeze_Seven.17.NF.vcf.gz | grep -e 43124027 >> ID_Var_Gen.txt
  ```

