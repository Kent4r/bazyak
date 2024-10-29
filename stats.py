import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv('cleaned_11K.csv', index_col=0)

# print(df['year_of_construction'].value_counts())
# df['year_of_construction'].value_counts().to_csv('years_count.csv')

dash = pd.read_csv('years_count.csv')
dash.sort_values(["year_of_construction"], axis=0, ascending=[False], inplace=True)

plot = sns.barplot(x='year_of_construction', y='count', data=dash, palette='dark:pink', orient='v')
plot.set_xticklabels(plot.get_xticklabels(), rotation=90, ha='right')
sns.despine(left=True, bottom=True)

plt.show()