import pyupbit
import pandas as pd

# df = pyupbit.get_ohlcv("KRW-BTC", count = 100  , period = 0.1, interval = "minute1", to = "20240205") # count = 4,000,000 개
# KRW-BTC : 20170925 12:00:00 이 마지막
# df = pyupbit.get_ohlcv("KRW-BTC") 
# df.to_csv("KRW-BTC_upbit2.csv") csv파일로 저장

<<<<<<< HEAD
# upbit에서 ohlcv 정보를 다운로드하는 함수.
=======

# upbit에서 ohlcv 데이터 받아오는 함수.

>>>>>>> 19f18d973083b80800173e5c1a62e0b54a1d305e
'''
symbol의 to 바로 앞부터 과거의 interval봉 데이터를 count개 만큼 period 간격으로 불러온다.

symbol = str    티커 정보(ex. "KRW-BTC")
interval = str  봉 정보(ex."minute1", "minute3"...)
count = int     봉 개수 정보 (ex. 100)
period = float  data 불러오는 주기(ex. 0.1)
<<<<<<< HEAD
to = any        가장 최근일 입력 (ex. "2024-02-05") # 입력시각 > utc 기준, 출력시각 : ktc로 나옴. >> 입력한 시각에 9시간 더해져서 나온다. >> 조정해보기
                to에 시간,분,초 정보 입력하지 않고 2024-02-05 라고 입력하면 2024-02-05 의 08:59:00까지 보여준다.
                to에 2024-02-05 입력하고 일봉데이터를 불러오면 2024-02-04가 마지막 데이터임
=======
to = any        가장 최근일 입력 (ex. "2024-02-05 21:10:00") # to는 utc(세계협정시) 기준임. to에 입력한 시각 = utc >> kst는 거기에 9시간을 더함.
>>>>>>> 19f18d973083b80800173e5c1a62e0b54a1d305e
'''
def get_upbit_ohlcv(symbol, interval, count , to, period):
    df = pyupbit.get_ohlcv(ticker = symbol, interval = interval, count = count , period = period, to = to ) # index에 시계열 데이터, index이름은 없음.
    return df

<<<<<<< HEAD
# 거래 정보가 없는 시각을 추가하는 함수.
'''
df = ohlcv DataFrame
start_date = 시작 시각  YYYY-MM-DD hh:mm:ss
end_date = 종료 시각    YYYY-MM-DD hh:mm:ss'
freq = 추가할 시각의 간격. # H -시간별, T -분별, S - 초별, L -밀리초별
start_date 부터 end_date 까지 df의 시계열data가 없는 행을 찾아 빈 시각을 추가해줌. 시각 추가 간격은 freq.

* 없는 시각 추가하는 속도 개빠름...  
'''

def add_missing_timestamps(df, start_date, end_date):
    date_range = pd.date_range(start=start_date, end=end_date, freq= '1T')
    df = df.reindex(date_range)
    return df


=======
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

>>>>>>> 19f18d973083b80800173e5c1a62e0b54a1d305e
# 거래 정보 없는 시각 추가해서 null 처리

# 양봉, 음봉을 판별하는 bool 값 추가하는 함수.
def add_candle_type_column(df):
    df['candle_type'] =None
    df['candle_type'][df['close'] > df['open']] = True
    df['candle_type'][df['close'] < df['open']] = False
    return df 

def save_to_csv(df, file_path):
    df.to_csv('KRW-BTC_upbit')







df = get_upbit_ohlcv("KRW-BTC", "minute1", 4000000, "20240206", 0.1 )
df = add_missing_timestamps(df, "2017-09-25 11:50:00", "2024-02-07 00:20:00") 
df = add_candle_type_column(df)
save_to_csv(df,"help")
print(df)

