import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv

df = pd.read_csv('8K.csv', index_col=0)
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

# with open("dash_info_first.csv", 'w', newline='', encoding='UTF-8') as csvfile:
#     fieldnames = ['city', 'price_for_meter']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for city in list_of_cities:
#         writer.writerow({'city': city, 'price_for_meter': price_for_meter(city)})

dash_info = pd.read_csv('dash_info_first.csv', index_col=0)
dash_info.sort_values(["price_for_meter"], axis=0, ascending=[False], inplace=True)
sns.set_style("whitegrid")
sns.barplot(x='city', y='price_for_meter', data=dash_info,  palette='dark:pink')
plt.xticks(rotation=60)
plt.show()