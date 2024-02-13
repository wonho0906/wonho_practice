import pandas as pd
import pyupbit
import backtrader as bt
import ccxt

upbit = ccxt.upbit()
btc_candle = ccxt.upbit.fetch_ohlcv(upbit, "KRW-BTC", "1m")
columns = ['', 'open', 'high', 'low', 'close', 'volume']
df = pd.DataFrame(btc_candle, columns=columns)
df[''] = pd.to_datetime(df[''], unit='ms')
df.set_index('', inplace=True)

class MyStrategy(bt.Strategy):
    def __init__(self): pass
    def next(self): pass


# pyupbit를 이용.
'''
def get_upbit_ohlcv(symbol, interval, count, to):
    df = pyupbit.get_ohlcv(symbol, interval=interval, count=count, to=to)
    return df

def add_missing_timestamps(df, start_date, end_date):
    date_range = pd.date_range(start=start_date, end=end_date, freq='1T')
    df = df.reindex(date_range)
    return df

def add_candle_type_column(df):
    df['candle_type'] = None
    df['candle_type'][df['close'] > df['open']] = True
    df['candle_type'][df['close'] < df['open']] = False
    return df

def save_to_csv(df, file_path):
    df.to_csv(file_path)

# 설정
symbol = 'KRW-BTC'
interval = 'minute1'
start_date = '2017-09-25-20:46:00'
end_date = '2017-09-26'
output_file = 'btc_ohlcv_data.csv'
chunk_size = 2000

# 초기 데이터 다운로드
df = get_upbit_ohlcv(symbol, interval, chunk_size, end_date)
df = add_missing_timestamps(df, start_date, end_date)
df = add_candle_type_column(df)
# save_to_csv(df, output_file)
'''
'''
# 추가 데이터 다운로드 및 파일에 이어쓰기
while df.index[-1] > pd.to_datetime(start_date):
    last_timestamp = df.index[-1] - pd.Timedelta(minutes=1)
    df_chunk = get_upbit_ohlcv(symbol, interval, chunk_size, last_timestamp)
    df_chunk = add_missing_timestamps(df_chunk, start_date, end_date)
    df_chunk = add_candle_type_column(df_chunk)
    df = pd.concat([df, df_chunk[1:]])
    save_to_csv(df_chunk, output_file)

print("데이터 다운로드 및 저장 완료.")
'''

if __name__ == "__main__":
    cerebro = bt.Cerebro()
    
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    cerebro.addstrategy(MyStrategy)
    cerebro.broker.setcash(20000000)
    cerebro.run()
    cerebro.plot()

