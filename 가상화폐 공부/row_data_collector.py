"""거래소의 row data를 불러와 저장한다.

거래소의 API를 이용해 OHLCV 데이터를 받는다.
이를 정해진 형식에 맞게 가공하여 InfluxDB에 저장한다.

TODO:
    Wonho:
        csv가 아닌 influxdb로 저장
    Sehun:
        Bithumb 뿐 아니라 Binance 데이터도 저장
        Upbit의 df에 index 이름 Time으로 설정
"""

import pandas as pd
from tool4trade import Exchange, add_bull, add_value
from datetime import datetime

# 초기 설정
exchange_str = "bithumb"    # 거래소 선정 (지원 거래소: "bithumb", "upbit")
count = 1500              # 불러올 정보의 수
last_time = None          # 불러올 정보의 마지막 시간. None이면 현재 시간. Bithumb은 None만 가능


# 거래소 API 객체 생성
exchange = Exchange(exchange_str)

# 해당 거래소의 모든 ticker를 불러온다.
tickers = exchange.get_tickers()

# 불러온 모든 ticker에 대해 ohlcv 데이터를 받아온다.
for ticker in tickers:
    df = exchange.get_1min_ohlcv(ticker, count, last_time)
    # auto_data_collector랑 충돌 - 2024.01.04
    # 열 이름의 첫 글자를 대문자로 변경 -2024.01.04. 이걸 대문자로 변경하면 auto_data_collector랑 충돌함
    '''
    df.columns = [col.capitalize() for col in df.columns]
    
    # Index가 존재할 경우 index의 첫 글자 대문자로 변경
    if df.index.name and df.index.name[0].islower():
        new_index_name = df.index.name.capitalize()
        df.index.rename(new_index_name, inplace=True)
    '''    
    
    # Index 이름이 존재하지 않을 경우 index 이름을 "Time"으로 설정
    if df.index.name is None:
        #Time을 time으로 변경 -2024.01.04 
        df.index.name = "time"
         
    # Bithumb이라면 'Value' 열 추가
    if exchange_str == "bithumb":
        df['Value'] = df.apply(add_value, axis=1)

    # 'Bull' 열 추가
    df['Bull'] = df.apply(add_bull, axis=1)

    # CSV 파일로 저장
    # 현재 날짜와 시간을 불러옵니다.
    today = datetime.now()
    # 날짜를 "yyyymmdd" 형식으로 포맷팅합니다.
    formatted_date = today.strftime("%Y%m%d")
    # df.to_csv(f'./db/{exchange_str}/{exchange_str}-{ticker[0].lower()}_{ticker[1].lower()}-{formatted_date}.csv', index=True)
    df.to_csv(f'./{exchange_str}-{ticker[0].lower()}_{ticker[1].lower()}-{formatted_date}.csv', index=True)
