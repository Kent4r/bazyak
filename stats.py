import pandas as pd

df = pd.read_csv('9K.csv', index_col=0)

print(df['location'].value_counts())