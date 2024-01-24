import pandas as pd

def BRCA_sheba(gen_file_name, phen_file, mutation, source_file, output_file_name, gene):
    main_file = gen_file_name
    df_freeze = pd.read_excel(main_file)
    output_name = f"exc_{mutation}"

    # Samples not carrying mutations to be excluded from the VCF.
    selected_columns = [col for col in df_freeze.columns if "0/0" in str(df_freeze.at[0, col])]
    with open(output_name, 'w') as output_file:
        for element in selected_columns:
            output_file.write(element + '\n')

    CH_17_var = [col for col in df_freeze.columns if "0/1" in str(df_freeze.at[0, col])]

    main_file = phen_file
    df_phen = pd.read_excel(main_file)
    df_phen['Unnamed: 0'] = df_phen['Unnamed: 0'].astype(str)
    phen_list = set(df_phen['Unnamed: 0'].to_list())


    # Retrieve the women ID from the column names in the format 'SHEBA_10114262_21-08773'
    list_ID_CH_17 = [element.split('_')[1] for element in CH_17_var]

    df_filtered = df_phen[df_phen['Unnamed: 0'].isin(list_ID_CH_17)]
    df_filtered = df_filtered[~df_filtered['mutation'].str.contains(mutation, case=False, na=False)]
    df_filtered = df_filtered[['Unnamed: 0', 'Gene', 'mutation']]

    with open(output_file_name, 'a') as output_file:
        output_file.write(f"======================{gene}_{mutation}======================" + '\n' + '\n')
        output_file.write(f"#women having the {mutation} mutation in the {source_file}: " + str(len(CH_17_var)) + '\n')
        output_file.write(str(list_ID_CH_17) + '\n')

        # Compare to the phenotypes file
        df_1 = df_phen[df_phen['mutation'].str.contains(mutation, case=False, na=False)]
        list_ID = set(df_1['Unnamed: 0'])


        df_freeze = df_freeze.iloc[:, 9:]
        new_column_names = [col.split('_')[1] for col in df_freeze.columns]
        df_freeze.columns = new_column_names
        df_freeze = df_freeze.transpose()
        df_freeze.columns = ['genotype']
        df_freeze.reset_index(inplace=True)
        df_freeze.rename(columns={'index': 'ID'}, inplace=True)
        df_filtered_2 = df_freeze[df_freeze['ID'].isin(list_ID)]
        df_filtered_2 = df_filtered_2[~df_filtered_2['genotype'].str.contains("0/1", case=False, na=False)]

        print(df_filtered_2)


        output_file.write("********" + '\n')
        output_file.write(f"#Women having the {mutation} mutation in the phenotype file: " + str(len(list_ID)) + '\n')
        output_file.write(str(list_ID) + '\n')
        output_file.write("********" + '\n')
        common_elements = list(set(list_ID) & set(list_ID_CH_17))
        print("intersection")
        print(len(common_elements))
        print(common_elements)

        list_filter_2 = set([element for element in list_ID if element not in list_ID_CH_17 and element not in df_filtered_2['ID'].to_list()])
        list_filter_3 = set([element for element in list_ID_CH_17 if element not in phen_list])
        list_filter = set([element for element in list_ID_CH_17 if element not in list_ID and element not in df_filtered['Unnamed: 0'].to_list()])


        output_file.write(
            f"#Women with the {mutation} mutation from the {source_file} who are entirely absent in the phenotype file: " +
            str(len(list_filter_3)) + '\n' + str(list_filter_3)+ '\n')
        output_file.write(f"#Women with the {mutation} mutation from the {source_file} who are not identified as mutation carriers in the phenotype file: " +
                          str(len(df_filtered['Unnamed: 0'].to_list())) + '\n'+ '\n')
        df_filtered.to_csv(output_file, index=False, sep='\t')
        output_file.write('\n')
        output_file.write("********" + '\n')
        output_file.write(f"#Women with the {mutation} mutation in the phenotype file who are entirely absent in {source_file}: " +
                          str(len(list_filter_2)) + '\n')

        output_file.write(str(list_filter_2) + '\n'+ '\n')
        output_file.write(
            f"#women with the {mutation} mutation in the phenotype file who are not identified as carriers in the {source_file}: " + str(len(df_filtered_2['ID'].to_list())) +'\n'+ '\n')
        df_filtered_2.to_csv(output_file, index=False, sep='\t')
        output_file.write('\n'+ '\n')




BRCA_sheba('IDs_185delAG_FREEZE.xlsx', 'BRCA.xlsx', '185delAG', 'SHEBA_Freeze_Seven.17.NF.vcf.gz', 'summary.txt', 'BRCA1')
BRCA_sheba('IDs_5382insC_FREEZE.xlsx', 'BRCA.xlsx', '382insC', 'SHEBA_Freeze_Seven.17.NF.vcf.gz', 'summary.txt', 'BRCA1')
BRCA_sheba('IDs_6174delT_FREEZE.xlsx', 'BRCA.xlsx', '6174delT', 'SHEBA_Freeze_Seven.13.NF.vcf.gz', 'summary.txt', 'BRCA2')
