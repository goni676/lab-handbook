import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
plt.switch_backend('Qt5Agg')



def print_fig(df, mutation, gene, age_lists, type):
    filtered_df = df[df['mutation'].str.contains(f"{mutation}", case=False, na=False)]
    list_type = filtered_df[type].to_list()
    list_type = [value for value in list_type if not math.isnan(value)]

    age_lists.append(list_type)
    plt.figure()
    c_bins = [20, 25, 30, 35, 40, 45, 50,55, 60, 65, 70, 75, 80, 85,90]

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.gca().set_axisbelow(True)
    for spine in plt.gca().spines.values():
        spine.set_linewidth(1.2)
    plt.hist(list_type, bins=c_bins, edgecolor='black', color='darkgreen', rwidth=0.8, alpha=0.7)  # Adjust the number of bins as needed
    plt.xlabel('Age (years)')
    plt.ylabel('Frequency')
    plt.title(f"{gene}_{mutation} AOO Distribution\nTotal Samples: {len(list_type)}", fontsize=11)

    plt.savefig(f"{gene}_{mutation} {type} Distribution")

if __name__ == '__main__':
    main_file = 'filtered_phen_0.xlsx'
    df_freeze = pd.read_excel(main_file)
    to_print = df_freeze[['ID', 'Gene', 'mutation']]
    print(to_print)
    to_print.to_excel("IDs_Regeneron_mutation.xlsx")
    df_freeze.rename(columns={'Merged_Column': 'Gene_Genotype_Data'}, inplace=True)
    df_freeze.rename(columns={'Had cancer': 'Had cancer BRE'}, inplace=True)
    df_freeze = df_freeze.drop('Gene', axis=1)
    # df_freeze = df_freeze.drop('mutation', axis=1)
    df_freeze = df_freeze.drop('DOB', axis=1)
    df_freeze = df_freeze.drop('cancer type', axis=1)


    age_lists=[]
    print_fig(df_freeze, '185delAG', 'BRCA1', age_lists, 'AOO')
    print_fig(df_freeze, '185delAG', 'BRCA1', age_lists, 'Age')
    print_fig(df_freeze, '5382insC', 'BRCA1', age_lists, 'AOO')
    print_fig(df_freeze, '5382insC', 'BRCA1', age_lists, 'Age')
    print_fig(df_freeze, '6174delT', 'BRCA2', age_lists, 'AOO')
    print_fig(df_freeze, '6174delT', 'BRCA2', age_lists, 'Age')
    mut_list = ["BRCA1 185delAG", "BRCA1 5382insC", "BRCA2 6174delT"]
    len_lst = [len(list) for list in age_lists]
    df = pd.DataFrame({'Group': ['Group 1'] * len(age_lists[0]) + ['Group 2'] * len(age_lists[1]) + ['Group 3'] * len(
        age_lists[2]) + ['Group 4'] * len(age_lists[3]) + ['Group 5'] * len(age_lists[4]) + ['Group 6'] * len(
        age_lists[5]),
                       'Age': [age for age_list in age_lists for age in age_list]})


    palette = sns.color_palette(['#ff0000', '#1f78b4'], n_colors=2)

    # Create subplots with two groups in each subplot
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16, 5))

    for i, (group_start, group_end) in enumerate([(0, 1), (2, 3), (4, 5)]):
        subset_df = df[df['Group'].isin([f'Group {group_start + 1}', f'Group {group_end + 1}'])]

        # Create violin plot with hue
        sns.violinplot(x='Group', y='Age', hue='Group', data=subset_df, palette=palette, ax=axes[i], alpha=0.8)
        for age_line in [0,5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]:
            axes[i].axhline(age_line, color='gray', linestyle='--', linewidth=0.8, alpha=0.3)

        axes[i].set_title(mut_list[i])
        axes[i].set_xlabel('')
        axes[i].set_ylabel('Age (years)')
        axes[i].set_xticks([])
        axes[i].set_xticklabels([])
        axes[i].set_ylim(5, 110)


        legend_labels = ['Yes','No']
        axes[i].legend(
            handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in
                     palette], title='BC', labels=legend_labels, loc='upper left', fontsize=10)


        group_labels = [f'Group {group_start + 1}', f'Group {group_end + 1}']
        for j, group_label in enumerate(group_labels):
            group_subset_df = subset_df[subset_df['Group'] == group_label]
            x_position = j * 0.5 + 0.25  # Adjust the multiplier based on the number of groups
            axes[i].text(x_position, -0.03, f"n =  {len(group_subset_df)}", ha='center', va='center',
                         transform=axes[i].transAxes, fontsize=10)
        line_start = (x_position, -0.1)
        line_end = (x_position, 0.05)
        axes[i].annotate('', xy=line_start, xytext=line_end, arrowprops=dict(arrowstyle='-', color='black'))

    plt.tight_layout()


    plt.show()
