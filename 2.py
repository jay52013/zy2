import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('US-pumpkins.csv')
data.head()

data['Date'] = pd.to_datetime(data['Date'])

cols_for_visualization = ['City Name', 'Package', 'Variety', 'Date', 'Low Price', 'High Price', 'Unit of Sale']
data_cleaned = data[cols_for_visualization].dropna()

data_cleaned['Average Price'] = data_cleaned[['Low Price', 'High Price']].mean(axis=1)

data_cleaned.head()

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
city_avg_price = data_cleaned.groupby('City Name')['Average Price'].mean().sort_values(ascending=False)
sns.barplot(x=city_avg_price.index, y=city_avg_price.values)
plt.xticks(rotation=90)
plt.title('Average Price by City')
plt.xlabel('City Name')
plt.ylabel('Average Price')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
package_avg_price = data_cleaned.groupby('Package')['Average Price'].median()
sns.boxplot(x='Package', y='Average Price', data=data_cleaned)
plt.xticks(rotation=90)
plt.title('Average Price by Package Type')
plt.xlabel('Package Type')
plt.ylabel('Average Price')
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
price_trend = data_cleaned.groupby('Date')['Average Price'].mean()
sns.lineplot(x=price_trend.index, y=price_trend.values)
plt.title('Price Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()