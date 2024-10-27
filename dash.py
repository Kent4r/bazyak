import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
df = pd.read_csv('11K.csv')
list_of_cities = df['location'].unique()
#print(list_of_cities)

# Function for calculate price for meter^2
def price_for_meter(location):
    city = df[df['location']==location]
    city_price = city['price'].sum()

    cleaned_data = [x.replace("м²", "").strip() for x in city['total_meters']]
    cleaned_data = [x.replace("-1", "0").strip() for x in cleaned_data]
    cleaned_data = [x.replace("���", "0").strip() for x in cleaned_data]
    cleaned_data = pd.to_numeric([x.replace(",", ".").strip() for x in cleaned_data]).sum()

    return round(city_price/cleaned_data,2)

# Создаю csv с ценами на квадратный метр

# with open("dash_info_fourth.csv", 'w', newline='', encoding='UTF-8') as csvfile:
#     fieldnames = ['city', 'price_for_meter']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for city in list_of_cities:
#         writer.writerow({'city': city, 'price_for_meter': price_for_meter(city)})

# Здесь все дешы через пандас
dash_info = pd.read_csv('dash_info_fourth.csv')
dash_info.sort_values(["price_for_meter"], axis=0, ascending=[False], inplace=True)
# sns.set_style("whitegrid")

# sns.barplot(hue='city', legend=False, x='city', y='price_for_meter', data=dash_info,  palette='dark:pink')
# plt.xticks(rotation=60)

# sns.countplot(x='location', data=df,  palette='dark:pink')

# plt.show()
figs, axs = plt.subplots(2,2, figsize=(26,10))
sns.set_style('whitegrid')

sns.barplot(hue='city', legend=False, x='city', y='price_for_meter', data=dash_info, palette='dark:pink', ax=axs[0,0])
axs[0,0].set_title('Цена за кв^2 в городах')
axs[0,0].set_xticklabels(axs[0,0].get_xticklabels(), rotation=60, ha='right')

sns.countplot(x='location', data=df,  palette='dark:pink', ax=axs[1,0], order=df['location'].value_counts().index)
axs[1,0].set_title('Количество городов')
axs[1,0].set_xticklabels(axs[1,0].get_xticklabels(), rotation=60, ha='right')

plt.show()