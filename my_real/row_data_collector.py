import pyupbit
import pandas as pd

# df = pyupbit.get_ohlcv("KRW-BTC", count = 100  , period = 0.1, interval = "minute1", to = "20240205") # count = 4,000,000 개
# KRW-BTC : 20170925 12:00:00 이 마지막
# df = pyupbit.get_ohlcv("KRW-BTC") 
# df.to_csv("KRW-BTC_upbit2.csv") csv파일로 저장


# upbit에서 ohlcv 데이터 받아오는 함수.

'''
symbol = str    티커 정보(ex. "KRW-BTC")
interval = str  봉 정보(ex."minute1", "minute3"...)
count = int     봉 개수 정보 (ex. 100)
period = float  data 불러오는 주기(ex. 0.1)
to = any        가장 최근일 입력 (ex. "2024-02-05 21:10:00") # to는 utc(세계협정시) 기준임. to에 입력한 시각 = utc >> kst는 거기에 9시간을 더함.
'''
def get_upbit_ohlcv(symbol, interval, count , to, period):
    df = pyupbit.get_ohlcv(ticker = symbol, interval = interval, count = count , period = period, to = to )
    return df

# 거래 정보가 없어서 비어있는 시각을 채우는 함수.
'''
df = ohlcv dataframe
start_date = 시작 날짜
end_date   = 종료 날짜   
'''
def add_missing_timestamps(df, start_date, end_date):
    date_range = pd.date_range(start=start_date, end=end_date, freq='1T')
    df = df.reindex(date_range)
    return df

# 거래 정보 없는 시각 추가해서 null 처리

def add_candle_type_column(df):
    df['candle_type'] = None
    df['candle_type'][df['close'] > df['open']] = True
    df['candle_type'][df['close'] < df['open']] = False
    return df 
def save_to_csv(df, file_path):
    df.to_csv('KRW-BTC_upbit')


