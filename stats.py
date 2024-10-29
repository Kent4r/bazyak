import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('cleaned_11K.csv', index_col=0)
list = ["price","year_of_construction","floor","floors_count","rooms_count","phone"]
for obj in list:
    df[obj] = df[obj].fillna(0)
    df[obj] = df[obj].astype(int)

print(df.dtypes)
df.drop(['url', 'phone'], axis=1, inplace=True)
df.to_csv('truly_cleaned_11K.csv')

year_mode_value = df['year_of_construction'].mode()[0]
df['year_of_construction'] = df['year_of_construction'].fillna(year_mode_value)
df['year_of_construction'] = df['year_of_construction'].astype(int)
df['year_of_construction'].value_counts().to_csv('years_count.csv')



# year_mode_value = df['year_of_construction'].mode()[0]
# df['year_of_construction'] = df['year_of_construction'].fillna(year_mode_value)



# dash = pd.read_csv('years_count.csv')
# dash.sort_values(["year_of_construction"], axis=0, ascending=[False], inplace=True)

# plot = sns.barplot(x='year_of_construction', y='count', data=dash, palette='dark:pink', orient='v')
# plot.set_xticklabels(plot.get_xticklabels(), rotation=90, ha='right')
# sns.despine(left=True, bottom=True)

# plt.show()



# df = pd.read_csv('cleaned_11K.csv', index_col=0)

# print(df['year_of_construction'].value_counts())