import pandas as pd
from scipy.stats import pearsonr

# Reading file
data = pd.read_csv('gene_expression.csv', sep='\t')

# Extracting gene names and their corresponding expression data
genes = data['Gene']
expression_data = data.drop(columns=['Gene'])

# Handling missing values
expression_data = expression_data.apply(lambda x: x.fillna(x.mean()), axis=0)

# Calculating Pearson correlation coefficients for all pairs of genes
correlation_matrix = pd.DataFrame(index=genes, columns=genes)

for i, gene1 in enumerate(genes):
    for j, gene2 in enumerate(genes):
        if i <= j:
            corr, _ = pearsonr(expression_data.iloc[i], expression_data.iloc[j])
            correlation_matrix.at[gene1, gene2] = corr
            correlation_matrix.at[gene2, gene1] = corr

# Print the correlation matrix
print(correlation_matrix)
