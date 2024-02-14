import ccxt
import time
import pandas as pd
202
#거래소 설정
upbit = ccxt.upbit()

# 입력한 시각을 timestamp로 바꿔주는 작업
input_time = input("최근 데이터 시각을 입력하세요 (utc입력) (ex.2024-01-15 00:15:00): ") 
utc_time = pd.to_datetime(input_time, utc = True)
timestamp = int(utc_time.timestamp()) * 1000
# print(timestamp)

# 1분봉 정보 입력
symbol = input("조회할 티커를 입력하세요(ex.KRW-BTC): ")
timeframe = input("timeframe입력(ex.1m): ")
since = timestamp
limit = input("몇개의 candlestick을 불러올까요?: ")

# 1분봉 정보 불러오는 작업
btc_candle = ccxt.upbit.fetch_ohlcv(upbit, symbol, timeframe, since, limit)

# 불러온 data를 dataframe으로 가공하기
columns = ['', 'open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(btc_candle, columns=columns)
df[''] = pd.to_datetime(df[''], unit='ms')
df.set_index('', inplace=True)

# csv파일로 저장
df.to_csv("")