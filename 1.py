import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('US-pumpkins.csv')
data.head()

#直方图
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

axs[0].hist(data['Low Price'].dropna(), bins=20, color='blue', alpha=0.7)
axs[0].set_title('Distribution of Low Price')
axs[0].set_xlabel('Low Price')
axs[0].set_ylabel('Frequency')

axs[1].hist(data['High Price'].dropna(), bins=20, color='green', alpha=0.7)
axs[1].set_title('Distribution of High Price')
axs[1].set_xlabel('High Price')
axs[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

#箱线图
plt.figure(figsize=(14, 8))
plt.boxplot([data[data['City Name'] == city]['Low Price'].dropna() for city in data['City Name'].unique()],
            labels=data['City Name'].unique())
plt.title('Price Distribution by City (Low Price)')
plt.xlabel('City Name')
plt.ylabel('Low Price')
plt.xticks(rotation=90)
plt.show()
