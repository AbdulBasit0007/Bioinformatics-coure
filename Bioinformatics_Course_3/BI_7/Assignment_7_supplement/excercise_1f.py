import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Reading file
data = pd.read_csv('gene_expression.csv', sep='\t')

# Extracting gene names and their corresponding expression data
genes = data['Gene']
expression_data = data.drop(columns=['Gene'])

# Handling missing values
expression_data = expression_data.apply(lambda x: x.fillna(x.mean()), axis=0)

# Calculating Pearson correlation coefficients between MCTS1 and all other genes
mcts1_corr = {}
mcts1_expression = expression_data.loc[data['Gene'] == 'MCTS1'].squeeze()

for gene in genes:
    if gene != 'MCTS1':
        gene_expression = expression_data.loc[data['Gene'] == gene].squeeze()
        corr, _ = pearsonr(mcts1_expression, gene_expression)
        mcts1_corr[gene] = corr

# Converting the dictionary to a DataFrame
mcts1_corr_df = pd.DataFrame(list(mcts1_corr.items()), columns=['Gene', 'Correlation'])

# Genes with the most positive, most negative, and closest to zero correlation
most_positive = mcts1_corr_df.loc[mcts1_corr_df['Correlation'].idxmax()]
most_negative = mcts1_corr_df.loc[mcts1_corr_df['Correlation'].idxmin()]
closest_to_zero = mcts1_corr_df.iloc[mcts1_corr_df['Correlation'].abs().idxmin()]

# Create scatter plots
plt.figure(figsize=(18, 5))

# Gene with the most positive correlation
plt.subplot(1, 3, 1)
plt.grid(True)
plt.scatter(mcts1_expression, expression_data.loc[data['Gene'] == most_positive['Gene']].squeeze())
plt.title(f'Most Positive Correlation: {most_positive["Gene"]}\nCorrelation: {most_positive["Correlation"]:.2f}')
plt.xlabel('MCTS1 Expression')
plt.ylabel(f'{most_positive["Gene"]} Expression')

# Gene with the most negative correlation
plt.subplot(1, 3, 2)
plt.grid(True)
plt.scatter(mcts1_expression, expression_data.loc[data['Gene'] == most_negative['Gene']].squeeze())
plt.title(f'Most Negative Correlation: {most_negative["Gene"]}\nCorrelation: {most_negative["Correlation"]:.2f}')
plt.xlabel('MCTS1 Expression')
plt.ylabel(f'{most_negative["Gene"]} Expression')

# Gene closest to zero correlation
plt.subplot(1, 3, 3)
plt.grid(True)
plt.scatter(mcts1_expression, expression_data.loc[data['Gene'] == closest_to_zero['Gene']].squeeze())
plt.title(f'Closest to Zero Correlation: {closest_to_zero["Gene"]}\nCorrelation: {closest_to_zero["Correlation"]:.2f}')
plt.xlabel('MCTS1 Expression')
plt.ylabel(f'{closest_to_zero["Gene"]} Expression')

plt.tight_layout()
plt.show()
