'''
# todo:
1. 저장할 데이터의 거래소와 ticker, 최초의 데이터 시간을 입력한다.
- ticker은 input함수로 입력할 수 있게 할 수 있을듯.
- 거래소는 input함수와 if문을 통해 설정하게 할 수 있을듯.
- 최초의 데이터 시간을 구하는 방법은 찾아봐야 될 것 같다. 지금은 우선 일일이 거래소에서 일봉으로 바꿔서 찾는 중...

2. 빈 csv 파일을 생성한다.
3. 반복문
3.1. csv 파일을 열고 저장된 데이터 중 마지막 시간을 얻는다.
3.2. 마지막 시간으로부터 1000개의 데이터를 ccxt를 통해 DataFrame class로 받는다.
- 200 개씩으로 바꿔야 될 듯...? 200개씩밖에 안 받아지네

3.3. 필요한 기타 수치들을 추가한다. (value, bull)
3.4. 얻은 데이터를 csv 파일에 이어서 저장하고 csv 파일을 닫는다.
3.5. 얻은 데이터의 개수가 1000개 이하면 반복문을 종료한다.
4. 마지막 데이터를 삭제한다. (불완전 데이터이므로)
'''

import ccxt
import time
import pandas as pd
import os

#거래소 설정
upbit = ccxt.upbit()
binance = ccxt.binance()
bithumb = ccxt.bithumb()

# 입력한 시각을 timestamp로 바꿔주는 작업
# input_time = input("최근 데이터 시각을 입력하세요 (utc입력) (ex.2024-01-15 00:15:00): ") 
input_time = "2023-01-15 00:15:00"
utc_time = pd.to_datetime(input_time, utc = True)
timestamp = int(utc_time.timestamp()) * 1000

# 비트코인의 최초 거래 시각
first_time = "2017-09-25 03:00:00"
first_utc_time = pd.to_datetime(first_time, utc = True)
first_timestamp = int(first_utc_time.timestamp())

# 빈 csv파일 생성하기
current_directory = os.getcwd()
data_folder_path = os.path.join(current_directory, 'data')
csv_file_path = os.path.join(data_folder_path, 'krw-btc.csv')

# 1분봉 정보 입력
'''
symbol = input("조회할 티커를 입력하세요(ex.KRW-BTC): ")
timeframe = input("timeframe입력(ex.1m): ")
since = timestamp
input_limit = input("몇개의 candlestick을 불러올까요?: ")
limit = int(input_limit)
'''
since = timestamp

# 1분봉 정보 불러오는 작업
# btc_candle = ccxt.upbit.fetch_ohlcv(upbit, symbol, timeframe, since, limit)
'''
count = 1000
for pos in range(count, 0, -200):
    query_count = min(pos,200)
'''
btc_candle= ccxt.upbit.fetch_ohlcv(upbit, "KRW-BTC", "1m", since, limit = 1000)#query_count)

# 불러온 data를 dataframe으로 가공하기
columns = ['', 'open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(btc_candle, columns=columns)
df[''] = pd.to_datetime(df[''], unit='ms')
df.set_index('', inplace=True)
print(df)

# 1분은 6만ms차이.
# csv파일로 저장
# df.to_csv("")
