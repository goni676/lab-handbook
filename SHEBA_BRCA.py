import pandas as pd

def BRCA_sheba(gen_file_name, phen_file, mutation, source_file, output_file_name, gene):
    main_file = gen_file_name
    df = pd.read_excel(main_file)
    output_name = f"exc_{mutation}"

    # Samples not carrying mutations to be excluded from the VCF.
    selected_columns = [col for col in df.columns if "0/0" in str(df.at[0, col])]
    with open(output_name, 'w') as output_file:
        for element in selected_columns:
            output_file.write(element + '\n')

    CH_17_var = [col for col in df.columns if "0/1" in str(df.at[0, col])]

    main_file = phen_file
    df = pd.read_excel(main_file)
    df['Unnamed: 0'] = df['Unnamed: 0'].astype(str)

    # Retrieve the women ID from the column names in the format 'SHEBA_10114262_21-08773'
    list_ID_CH_17 = [element.split('_')[1] for element in CH_17_var]

    with open(output_file_name, 'a') as output_file:  # 'a' for append mode
        output_file.write(f"======================{gene}_{mutation}======================" + '\n' + '\n')
        output_file.write(f"#women having the {mutation} mutation in the {source_file}:" + str(len(CH_17_var)) + '\n')
        output_file.write(f"IDs of women with the {mutation} mutation in the {source_file}:" + '\n')
        output_file.write(str(list_ID_CH_17) + '\n')

        # Compare to the phenotypes file
        df_1 = df[df['mutation'].str.contains(mutation, case=False, na=False)]
        list_ID = list(df_1['Unnamed: 0'])

        output_file.write("********" + '\n')
        output_file.write(f"#Women having the {mutation} mutation in the phenotype file:" + str(len(list_ID)) + '\n')
        output_file.write(f"IDs of women with the {mutation} mutation in the phenotype file:" + '\n')
        output_file.write(str(list_ID) + '\n')
        output_file.write("********" + '\n')

        list_filter = [element for element in list_ID_CH_17 if element not in list_ID]

        output_file.write(f"#women with the {mutation} mutation in {source_file} not present in the phenotype file:" +
                          str(len(list_filter)) + '\n')
        output_file.write(f"IDs of women with the {mutation} mutation in {source_file} not present in the phenotype file:" + '\n')
        output_file.write(str(list_filter) + '\n'+ '\n')



BRCA_sheba('IDs_185delAG_FREEZE.xlsx', 'BRCA.xlsx', '185delAG', 'SHEBA_Freeze_Seven.17.NF.vcf.gz', 'summary.txt', 'BRCA1')
BRCA_sheba('IDs_5382insC_FREEZE.xlsx', 'BRCA.xlsx', '382insC', 'SHEBA_Freeze_Seven.17.NF.vcf.gz', 'summary.txt', 'BRCA1')
# BRCA_sheba('IDs_6174delT_FREEZE.xlsx', 'BRCA.xlsx', '6174delT', 'SHEBA_Freeze_Seven.13.NF.vcf.gz', 'summary.txt', 'BRCA2')
