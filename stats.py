import pandas as pd

df = pd.read_csv('cleaned_11K.csv', index_col=0)

print(df['location'].value_counts())