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

The CADD file follows the specified format:
#Chrom	Pos	Ref	Alt	RawScore	PHRED
1	10001	T	A	0.702541	8.478
1	10001	T	C	0.750954	8.921
1	10001	T	G	0.719549	8.634
1	10002	A	C	0.713993	8.583
1	10002	A	G	0.743661	8.854
1	10002	A	T	0.700507	8.460
1	10003	A	C	0.714485	8.588
1	10003	A	G	0.744152	8.859

For successful execution, ensure that the input file is a text file sorted first by position and then by chromosome. Additionally, filter the variants to include only those that transition one base pair at a time, following the format illustrated below:


