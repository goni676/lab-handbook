import pandas as pd
main_file = 'check.xlsx'
df = pd.read_excel(main_file)

# Samples not carrying mutations to be excluded from the VCF.
selected_columns = [col for col in df.columns if "0/0" in str(df.at[0, col])]
with open('ex_185delAG_CH17', 'w') as output_file:
    for element in selected_columns:
        output_file.write(element + '\n')

CH_17_var = [col for col in df.columns if "0/1" in str(df.at[0, col])]

main_file = 'BRCA.xlsx'
df = pd.read_excel(main_file)
df['Unnamed: 0'] = df['Unnamed: 0'].astype(str)

# Retrieve the women ID from the column names in the format 'SHEBA_10114262_21-08773'
list_ID_CH_17 = [element.split('_')[1] for element in CH_17_var]


print("#women having the 185delAG mutation in the 'SHEBA_Freeze_Seven.17.NF.vcf.gz' file:", len(CH_17_var))
print("IDs of women with the 185delAG mutation in the 'SHEBA_Freeze_Seven.17.NF.vcf.gz' file:")
print(list_ID_CH_17)

# Compare to the phenotypes file
df_185delAG = df[df['mutation'].str.contains('185delAG', case=False, na=False)]
list_ID_185delAG = list(df_185delAG['Unnamed: 0'])
print("********")
print("#Women having the 185delAG mutation in the phenotype file:", len(list_ID_185delAG))
print("IDs of women with the 185delAG mutation in the phenotype file:")
print(list_ID_185delAG)
print("********")

list_filter = [element for element in list_ID_CH_17 if element not in list_ID_185delAG]

print("#women with the 185delAG mutation in 'SHEBA_Freeze_Seven.17.NF.vcf.gz' not present in the phenotype file:", len(list_filter))
print("IDs of women with the 185delAG mutation in 'SHEBA_Freeze_Seven.17.NF.vcf.gz' not present in the phenotype file:")
print(list_filter)