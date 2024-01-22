# Documentation for SHEBA's BRCA project

We are searching for three mutations within BRCA1 and BRCA2:

| CHROM | GENE  | MUTATION | POS      |
|-------|-------|----------|----------|
| 17    | BRCA1 | 185delAG | 43124027 |
| 17    | BRCA1 | 5382insC | 43057062 |
| 13    | BRCA2 | 6174delT | 32340300 |

|   index   |   ID     |          genotype          |
|-----------|----------|---------------------------|
|    12     | 1217504  | 0/0:33:33,0:.:67:.:.:..  |
|   500    | 23605801 | 0/0:35:35,0:.:69:.:.:..  |
|   896    | 308339340| 0/0:40:40,0:.:76:.:.:..  |
|   1150   | 32953622 | 0/0:23:23,0:.:51:.:.:..  |
|   1313   | 34208553 | 0/0:42:42,0:.:78:.:.:..  |
|   1389   | 35694918 | 0/0:27:27,0:.:58:.:.:..  |
|   1397   | 35854181 | 0/0:39:39,0:.:75:.:.:..  |
|   1416   | 36234359 | 0/0:36:36,0:.:71:.:.:..  |
|   1662   | 46112215 | 0/0:28:28,0:.:59:.:.:..  |

|      ID       |  Gene  |  Mutation  |
|--------------|--------|------------|
|   27349885   | BRCA2  |  6174delT  |
| 300325800  | BRCA1  |  5382insC  |
|  25591819   | BRCA1  |  5382insC  |
| 315325837  | BRCA1  |  188delAG  |
|  16822942   | BRCA1  |  185delT   |
|   6508071    | BRCA2  |  6174delT  |
| 37680444  | BRCA2  |  6174delT  |

| Index |   ID   |          Genotype         |
|-------|--------|---------------------------|
|  572  | 25188269 | 0/0:24:24,0:.:53:.:.:..  |
|  592  | 25591819 | 0/0:19:19,0:.:44:.:.:..  |
|  738  | 300325800 | 0/0:24:24,0:.:53:.:.:..  |

|   ID  |   Gene   |      Mutation      |
|------------|----------|--------------------|
| 23529027   |  BRCA1   |                    |
| 32953622   | BRCA1+2  | 6174delT+185delAG |
| 308339340  |  BRCA1   |      185delAG      |
| 34208553   |  BRCA1   |      185delAG      |
| 35854181   |  BRCA1   |      185delAG      |
| 46112215   |  BRCA1   |      185delAG      |


| ID |   Gene   |  Mutation  |
|------------|----------|-------------|
| 301267068  |  BRCA2   |  c.5946del  |
| 40684599   |  BRCA2   |  c.5946del  |
| 35694918   |  BRCA1   |  185delAG   |

| Index |      ID      |         Genotype         |
|-------|--------------|--------------------------|
|  500  |   23605801   | 0/0:63:63,0:.:101:.:.:.. |
|  850  |  305691586   | 0/0:64:64,0:.:102:.:.:.. |
|  997  |   31559164   | 0/0:86:86,0:.:120:.:.:.. |
| 1317  |   34237099   | 0/0:53:53,0:.:91:.:.:..  |
| 1478  |   37680444   | 0/0:77:77,0:.:113:.:.:.. |
| 1491  |   38184594   | 0/0:86:86,0:.:120:.:.:.. |
| 1938  |   56777824   | 0/0:61:61,0:.:99:.:.:..  |
| 2076  |    6508071   | 0/0:81:81,0:.:116:.:.:.. |


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

