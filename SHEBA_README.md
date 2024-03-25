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
Subsequently, our aim is to narrow it down to the 311 relevant genes and the specific variant type as needed:

```
cat 185delAG_after_VEP.vcf | grep -w -e AKT1 -e ALKBH2 -e ALKBH3 -e ANKRD28 -e ANKRD44 -e ANKRD52 -e APC -e APEX1 -e APEX2 -e APITD1 -e APLF -e APTX -e ATF1 -e ATM -e ATR -e ATRIP -e BABAM1 -e BACH1 -e BAP1 -e BARD1 -e BCAS2 -e BIVM-ERCC5 -e BLM -e BMPR1A -e BRCA1 -e BRCA2 -e BRCC3 -e BRIP1 -e C17orf70 -e C19orf40 -e CCNH -e CCNO -e CDC25A -e CDC25C -e CDC5L -e CDH1 -e CDK4 -e CDK7 -e CDKN1A -e CDKN2A -e CETN2 -e CHEK1 -e CHEK2 -e CNTLN -e CRY1 -e CRY2 -e CTNNA1 -e CUL3 -e CUL4A -e CUL4B -e CUL5 -e DCLRE1A -e DCLRE1B -e DCLRE1C -e DDB1 -e DDB2 -e DMC1 -e DNTT -e DUT -e E2F1 -e EME1 -e EME2 -e EPCAM -e ERCC1 -e ERCC2 -e ERCC3 -e ERCC4 -e ERCC5 -e ERCC6 -e ERCC8 -e ESR1 -e EXO1 -e EXO5 -e FAM175A -e FAM175B -e FAN1 -e FANCA -e FANCB -e FANCC -e FANCD2 -e FANCE -e FANCF -e FANCG -e FANCI -e FANCL -e FANCM -e FEN1 -e FOXM1 -e GADD45A -e GEN1 -e GTF2H1 -e GTF2H2 -e GTF2H2C -e GTF2H2D -e GTF2H3 -e GTF2H4 -e GTF2H5 -e H2AFX -e HDAC9 -e HES1 -e HFM1 -e HLTF -e HMGB1 -e HOXB13 -e HUS1 -e HUS1B -e KANK4 -e LIG1 -e LIG3 -e LIG4 -e MBD4 -e MDC1 -e MDM4 -e MEN1 -e MGMT -e MLH1 -e MLH3 -e MMS19 -e MNAT1 -e MPG -e MRE11 -e MSH2 -e MSH3 -e MSH4 -e MSH5 -e MSH6 -e MUS81 -e MUTYH -e MYBBP1A -e MYC -e MYCT1 -e NBN -e NEIL1 -e NEIL2 -e NEIL3 -e NF1 -e NHEJ1 -e NOTCH2 -e NTHL1 -e NUDT1 -e NUDT15 -e NUDT18 -e OBSL1 -e OGG1 -e PALB2 -e PAPD7 -e PARP1 -e PARP2 -e PARP3 -e PARP4 -e PCNA -e PCSK7 -e PER1 -e PER2 -e PER3 -e PIK3CA -e PLK1 -e PLRG1 -e PLS3 -e PML -e PMS1 -e PMS2 -e PNKP -e POLB -e POLD1 -e POLD2 -e POLD3 -e POLD4 -e POLE -e POLE2 -e POLE3 -e POLE4 -e POLH -e POLI -e POLK -e POLL -e POLM -e POLN -e POLQ -e POLR2A -e POLR2B -e POLR2C -e POLR2D -e POLR2E -e POLR2F -e POLR2G -e POLR2H -e POLR2I -e POLR2J -e POLR2J2 -e POLR2J3 -e POLR2K -e POLR2L -e POU2F1 -e PPM1D -e PPP4C -e PPP4R1 -e PPP4R2 -e PPP4R4 -e PPP6C -e PPP6R1 -e PPP6R2 -e PPP6R3 -e PRKDC -e PRPF19 -e PRSS1 -e PSMC3IP -e PTCH1 -e PTEN -e RAD1 -e RAD17 -e RAD18 -e RAD23A -e RAD23B -e RAD50 -e RAD51 -e RAD51B -e RAD51C -e RAD51D -e RAD52 -e RAD54B -e RAD54L -e RAD54L2 -e RAD9A -e RAD9B -e RB1 -e RBBP8 -e RBX1 -e RDM1 -e RECQL -e RECQL4 -e RECQL5 -e RET -e REV1 -e REV3L -e RFC1 -e RFC2 -e RFC3 -e RFC4 -e RFC5 -e RINT1 -e RMI1 -e RMI2 -e RNF8 -e RPA1 -e RPA2 -e RPA3 -e RPA4 -e RPS15 -e RRM1 -e RRM2 -e RRM2B -e SBDS -e SHFM1 -e SLX1A -e SLX1B -e SLX4 -e SMAD4 -e SMARCA1 -e SMEK1 -e SMEK2 -e SMO -e SMUG1 -e SPO11 -e SSBP1 -e STAT1 -e STK11 -e STRA13 -e TCEB1 -e TCEB2 -e TCEB3 -e TCEB3B -e TCEB3C -e TCEB3CL -e TDG -e TDP1 -e TELO2 -e TIMELESS -e TIPARP -e TIPIN -e TMEM189 -e TMEM189-UBE2V1 -e TOP3A -e TOP3B -e TOPBP1 -e TP53 -e TP53BP1 -e TREX1 -e TREX2 -e UBE2A -e UBE2B -e UBE2N -e UBE2NL -e UBE2T -e UBE2V1 -e UBE2V2 -e UIMC1 -e UNG -e USP1 -e VHL -e WDR48 -e WRN -e XPA -e XPC -e XRCC1 -e XRCC2 -e XRCC3 -e XRCC4 -e XRCC5 -e XRCC6 -e ZNF350 | grep -w -e 'missense_variant' -e 'inframe_insertion' -e 'inframe_deletion' -e 'stop_gained' -e 'frameshift_variant' -e 'stop_lost' -e 'start_lost' -e 'splice_acceptor_variant' -e 'splice_donor_variant' > output_file.txt
```

## CADD
CADD (Combined Annotation Dependent Depletion) is a tool and a scoring system designed to evaluate the deleteriousness of genetic variants in the human genome. 
CADD corresponds to the assembly of the Human Genome version 38.

| #Chrom | Pos   | Ref | Alt | RawScore  | PHRED  |
|--------|-------|-----|-----|-----------|--------|
| 1      | 10001 | T   | A   | 0.702541  | 8.478  |
| 1      | 10001 | T   | C   | 0.750954  | 8.921  |
| 1      | 10001 | T   | G   | 0.719549  | 8.634  |
| 1      | 10002 | A   | C   | 0.713993  | 8.583  |
| 1      | 10002 | A   | G   | 0.743661  | 8.854  |
| 1      | 10002 | A   | T   | 0.700507  | 8.460  |
| 1      | 10003 | A   | C   | 0.714485  | 8.588  |
| 1      | 10003 | A   | G   | 0.744152  | 8.859  |

For successful execution, ensure that the input file is a text file sorted first by position and then by chromosome. Additionally, filter the variants to include only those that transition one base pair at a time, following the format illustrated above.

Python code to perform filtering:
```
df = df.drop(columns='Var_ID')
df_filtered = df[(df['Ref'].str.len() == 1) & (df['Alternative_Allele'].str.len() == 1)]
df_filtered['Pos'] = df_filtered['Pos'].astype(int)
df_filtered['Chrom'] = df_filtered['Chrom'].astype(int)
df_sorted = df_filtered.sort_values(by=['Chrom', 'Pos'])
```

Command entered on the server's command line:
```
awk '{key=$1 FS $2 FS $3 FS $4} NR==FNR {val[key]=$5" "$6" "$7" "$8; next} key in val {print $0.val[key]}' final_to_CADD.txt /specific/elkon/sapir2/clinvar_data/whole_genome_SNVs.tsv > after_CADD.txt
```

## AlphaMissense
A deep learning model that builds on the protein structure prediction tool AlphaFold2 (see the Perspective by Marsh and Teichmann). The model is trained on population frequency data and uses sequence and predicted structural context, all of which contribute to its performance. AlphaMissense corresponds to the assembly of the Human Genome version 38.

The format of the AlphaMissense file is as follows:

| #CHROM | POS   | REF | ALT | Genome | UniProt_ID | Transcript_ID         | Protein_Variant | Am_Pathogenicity | Am_Class        |
|--------|-------|-----|-----|--------|------------|------------------------|------------------|-------------------|-----------------|
| chr1   | 69094 | G   | T   | hg38   | Q8NH21     | ENST00000335137.4     | V2L              | 0.2937            | likely_benign   |
| chr1   | 69094 | G   | C   | hg38   | Q8NH21     | ENST00000335137.4     | V2L              | 0.2937            | likely_benign   |
| chr1   | 69094 | G   | A   | hg38   | Q8NH21     | ENST00000335137.4     | V2M              | 0.3296            | likely_benign   |
| chr1   | 69095 | T   | C   | hg38   | Q8NH21     | ENST00000335137.4     | V2A              | 0.2609            | likely_benign   |
| chr1   | 69095 | T   | A   | hg38   | Q8NH21     | ENST00000335137.4     | V2E              | 0.2922            | likely_benign   |
 
Python code for filtering to meet the requirements of AlphaMissense file preparation:
```
df = df.drop(columns='Var_ID')
df_filtered = df[(df['Ref'].str.len() == 1) & (df['Alternative_Allele'].str.len() == 1)]
df_filtered['Pos'] = df_filtered['Pos'].astype(int)
df_filtered['Chrom'] = 'chr' + df_filtered['Chrom'].astype(str)
df_sorted = df_filtered.sort_values(by=['Chrom', 'Pos'])
df_sorted.to_csv('final_to_ALPHA.txt', sep='\t', index=False)
```

Command entered on the server's command line:
```
awk '{key=$1 FS $2 FS $3 FS $4} NR==FNR {val[key]=$5" "$6" "$7" "$8" "$9" "$10" "$11" "$12" "$13; next} key in val {print $0.val[key]}' final_to_ALPHA.txt /specific/elkon/sapir2/Lina_project/AlphaMissense_hg38.tsv > after_ALPHA.txt
```

## vcfanno
[vcfanno](https://github.com/brentp/vcfanno/blob/master/README.md) allows you to quickly annotate your VCF with any number of INFO fields from any number of VCFs or BED files. It uses a simple conf file to allow the user to specify the source annotation files and fields and how they will be added to the info of the query VCF. In the Sheba dataset, we utilized vcfanno to ascertain the Minor Allele Frequency (MAF), representing the frequency of the variant within the population.

We achieved this by linking vcfanno to the GNOMAD dataset and specifying the necessary field as 'AF RAW' in the configuration.

### Prepare Data for Vcfanno Processing
* Sort the data frame based on chromosome and position.
  ```
  df.sort_values(by=['Chrom', 'Pos'], ascending=[True, True])
  ```
* Add a new column named "ID" immediately after the 'Pos' column, filling all rows with dots.
  ```
  df.insert(2, 'ID', '.')
  ```
* Split the DataFrame into 22 separate files based on the 'chrom' column.The "CHROM" column is of the format 'chr{num}'. 
* We must provide a VCF file as input, which can be accomplished by appending a header to a text file:
  ```
  header_lines = "##fileformat=VCFv4.3\n##reference=GRCh38\n#CHROM\tPOS\tID\tREF\tALT\tConsequence_Type\tImpact\tGene\tGene_ID\tTranscript_Info\tTranscript_Type\tAmino_Acid_Position\tPolyphen_Score\tAmino_Acid_Change\tNucleotide_Change\tStrand_Info\tcarriers ID\n"
  ```
  
```
output_directory = 'output_vcf'
os.makedirs(output_directory, exist_ok=True)

# Loop through each group (DataFrame) and save it to a VCF file
header_lines = "##fileformat=VCFv4.3\n##reference=GRCh38\n#CHROM\tPOS\tID\tREF\tALT\tConsequence_Type\tImpact\tGene\tGene_ID\tTranscript_Info\tTranscript_Type\tAmino_Acid_Position\tPolyphen_Score\tAmino_Acid_Change\tNucleotide_Change\tStrand_Info\tcarriers ID\n"

# Loop through each group (DataFrame) and save it to a CSV file
for chrom, group_df in grouped_df:
    output_file = os.path.join(output_directory, f'df_chrom_{chrom}.vcf')

    # Save the DataFrame along with the header lines
    with open(output_file, 'w') as f:
        f.write(header_lines)
        group_df.to_csv(f, index=False, header=False, sep='\t', line_terminator='\n', mode='a')
```
* To utilize vcfanno with Gnomad, you must download the Gnomad files, available at [this link](https://gnomad.broadinstitute.org/downloads).
* Modify the configuration file `conf.toml` to correspond to the specific VCF file for the desired chromosome.
```
[[annotation]]
file="/specific/elkon/sapir2/gnomad_data/gnomad.genomes.v3.1.2.sites.chr6.vcf.bgz"
#file="/specific/elkon/sapir2/tools/vcfanno-0.3.5/example/exac.vcf.gz"
# the special name 'ID' pulls out the rs id from the VCF
#fields = ["AF_raw", "vep"]
#ops=["first" , "first"]
fields = ["AF_raw"]
ops=["first"]
...
```

| Covariate | Coefficient (β) | Hazard Ratio (exp(β)) | Std. Error | 95% CI for β | 95% CI for exp(β) | Z-Score | P-Value    | -log2(p)    |
|-----------|-----------------|-----------------------|------------|--------------|-------------------|---------|------------|-------------|
| ALPHA     | 0.78            | 2.18                  | 1.19       | -1.55, 3.10  | 0.21, 22.24       | 0.66    | 0.51       | 0.97        |
| CADD      | 0.08            | 1.08                  | 0.04       | 0.00, 0.16   | 1.00, 1.17        | 2.02    | 0.04       | 4.53        |

| Parameter        | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `df_cox`         | The DataFrame containing the survival data.                                 |
| `duration_col`   | Specifies the column (`'AOO'`) in `df_cox` that contains the survival times.|
| `event_col`      | Indicates the column (`'Had_BRE'`) in `df_cox` that contains the event occurrence (1 if the event has occurred, 0 otherwise). |
| `formula`        | Defines the covariates included in the model (`'ALPHA+CADD'`).              |


## PLINK

### ULTIMA GENOMICS VS. BGI
1. BGI genotyping consolidates all women into a single file. Consequently, we aim to divide it into individual files for each woman.
    ```
    plink --bfile all --keep O12.txt --make-bed --allow-extra-chr --out O12
    ```
2. Since the bed file adheres to this format:

    | Variant ID | Placeholder_1 | Placeholder_2 | Position | Reference Allele | Alternative Allele(s) |
    |------------|---------------|---------------|----------|------------------|-----------------------|
    | 1          | .             | 0             | 10140    | A                | ACCCTAAC              |
    | 2          | .             | 0             | 10146    | A                | AC                    |
    | 3          | .             | 0             | 10177    | C                | A                     |
    
    we must assign an identification (ID) to each variant. This applies to both the big and Ultima genomics files:
    ```
    plink --bfile O9 --set-missing-var-ids @_#_\$1_\$2 --make-bed --allow-extra-chr --out O9_with_ids
    ```
    The new bed file now follows the following format:
    
    | Variant ID | Variant Name | Placeholder | Position | Reference Allele | Alternative Allele(s) |
    |------------|--------------|-------------|----------|------------------|-----------------------|
    | 1          | 1_10146_A_AC | 0           | 10146    | A                | AC                    |
    | 2          | 1_10177_A_C  | 0           | 10177    | C                | A                     |
    | 3          | 1_12807_C_T  | 0           | 12807    | T                | C                     |
    | 4          | 1_13079_C_G  | 0           | 13079    | G                | C                     |

3. Next, we aim to merge the two files representing the same woman, such as O9-UO3. To achieve this, we will execute the following command:

    ```
    plink --bfile O9_with_ids --bmerge ../ultima_genomics/UO3_with_ids --make-bed --allow-extra-chr --out ../combined/O9_UO3_with_ids
    ```
    We expect to encounter this type of error:
    ### Error Encountered
    **Error: 758 variants with 3+ alleles present.**

4. In the 'combined' directory, you'll find the output of the merge operation. One of the files present is 'O9_UO3_with_ids-merge.missnp', which contains information on variants that were not successfully merged.
   Now, we exclude variants that didn't merge successfully from each file (O9_with_ids and UO3_with_ids) and proceed to run the merge operation again.

    ```
    plink --bfile O9_with_ids --exclude ../combined/O9_UO3_with_ids-merge.missnp  --make-bed --allow-extra-chr --out O9_with_ids_no_amb
    plink --bfile UO3_with_ids --exclude ../combined/O9_UO3_with_ids-merge.missnp  --make-bed --allow-extra-chr --out UO3_with_ids_no_amb
    plink --bfile O9_with_ids_no_amb --bmerge ../ultima_genomics/UO_with_ids_no_amb --make-bed --allow-extra-chr --out ../combined/O9_UO3
    ```

5. Now, to calculate genome-wide estimates of pairwise genetic relatedness among individuals in our dataset, we will execute the following command:
     ```
     plink --bfile /specific/elkon/gonicohen/sheba_rinat/combined/O12_UO1_with_ids_no_amb --out /specific/elkon/BRCA_WGS/O12_UO1.relatedness --genome --allow-extra-chr
     ```

