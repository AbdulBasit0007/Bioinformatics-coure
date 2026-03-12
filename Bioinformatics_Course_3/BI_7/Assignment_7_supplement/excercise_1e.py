import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Reading file
data = pd.read_csv('gene_expression.csv', sep='\t')

# Extracting gene names and their corresponding expression data
genes = data['Gene']
expression_data = data.drop(columns=['Gene'])

# Handling missing values
expression_data = expression_data.apply(lambda x: x.fillna(x.mean()), axis=0)

correlations = []

for i, gene1 in enumerate(genes):
    for j, gene2 in enumerate(genes):
        if i < j:  # Only calculate correlation once for each pair
            corr, _ = pearsonr(expression_data.iloc[i], expression_data.iloc[j])
            correlations.append(corr)

# Plotting the distribution of correlation coefficients
plt.figure(figsize=(8, 6))
sns.histplot(correlations, bins=20, kde=True)
plt.title('Distribution of Pearson Correlation Coefficients')
plt.xlabel('Correlation Coefficient')
plt.ylabel('Frequency')
plt.show()
