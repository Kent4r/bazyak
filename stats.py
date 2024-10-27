import pandas as pd

df = pd.read_csv('10K.csv', index_col=0)

print(df['location'].value_counts())