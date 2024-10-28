import pandas as pd

df = pd.read_csv('cleaned_11K.csv', index_col=0)

del df['deal_type']
del df['accommodation_type']

df.to_csv('cleaned_11K.csv', index=False)