import ccxt
import time
import pandas as pd
import requests
upbit = ccxt.upbit()
btc_candle = ccxt.upbit.fetch_ohlcv(upbit, "KRW-BTC", "5m")
columns = ['', 'open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(btc_candle, columns=columns)
df[''] = pd.to_datetime(df[''], unit='ms')
df.set_index('', inplace=True)

# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df.to_csv("hello.csv")
# print(df.head(2))
# df = pd.DataFrame(btc_candle)
# print(df)
# print(btc_candle[0:2])