import pyupbit

# Upbit API로 데이터 가져오기
symbol = "BTC-KRW"
interval = "minute10"
start_time = "2023-11-11 00:00:00"
end_time = "2023-11-11 23:59:59"

# 10분봉 데이터 가져오기
candles = pyupbit.get_ohlcv(symbol, interval=interval, to=end_time)

# 결과 출력
print(candles)