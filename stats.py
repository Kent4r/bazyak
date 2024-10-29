import pandas as pd

df = pd.read_csv('11K.csv', index_col=0)

print(df['house_material_type'].value_counts())