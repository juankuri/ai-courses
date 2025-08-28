import pandas as pd
print('read csv')

df = pd.read_csv('winemag-data-130k-v2.csv')

print(df.shape)
print(df.head())