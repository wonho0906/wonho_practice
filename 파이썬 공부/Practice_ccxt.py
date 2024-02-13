import ccxt
import time
import pandas as pd
import requests
upbit = ccxt.upbit()

input_time = "2024-01-15 00:15:00"
utc_time = pd.to_datetime(input_time, utc=True)
timestamp = int(utc_time.timestamp())
print(timestamp)

btc_candle = ccxt.upbit.fetch_ohlcv(upbit, "KRW-BTC", "1m", since = timestamp ,limit = 100)
columns = ['', 'open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(btc_candle, columns=columns)
df[''] = pd.to_datetime(df[''], unit='ms')
df.set_index('', inplace=True)

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
df.to_csv("hello2.csv")
# print(df.head(2))
# df = pd.DataFrame(btc_candle)
# print(df)
# print(btc_candle[0:2])

