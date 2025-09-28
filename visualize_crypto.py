import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Coins to track
coins = ['bitcoin', 'ethereum', 'solana']
days = 30  # last 30 days

for coin in coins:
    url = f'https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency=usd&days={days}'
    data = requests.get(url).json()
    prices = data['prices']

    # Convert to DataFrame
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Plot
    plt.plot(df['date'], df['price'], label=coin.capitalize())

plt.title('Crypto Prices Last 30 Days')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
