import pandas as pd

# Load data
df = pd.read_csv('../data/sample_dataset.csv', parse_dates=['date'])

# Filter by region and date range
mask = (df['region'] == 'East') & (df['date'] >= '2024-01-01') & (df['date'] <= '2024-03-31')
filtered = df.loc[mask]

# Aggregation by category
agg = filtered.groupby('category')['value'].agg(['count','sum','mean']).reset_index()
print(agg)

# Example: remove outliers using IQR
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1
low = Q1 - 1.5 * IQR
high = Q3 + 1.5 * IQR
clean = df[(df['value'] >= low) & (df['value'] <= high)]

clean.to_csv('../data/sample_dataset_clean.csv', index=False)
