'''과거의 데이터를 수집하여 데이터베이스를 구축한다. 이때 bull, value 등 몇몇 값을 추가하는 작업을 한다.

TODO:
    처음 거래 시간 찾는 것
    거래가 없어 데이터가 누락되어 있을 시 반복문이 끝나버려 그 후로 데이터를 받아오지 않는 오류
'''
from tool4trade import data_source
from tool4trade import DataSource
from datetime import datetime
import pytz

## 초기 설정값
exchange = "upbit"
ticker = 'BLUR/KRW'
first_time = "2023-06-27 00:00:00"
first_time_timezone = pytz.timezone('Asia/Seoul')


## main 함수
data_source = DataSource(exchange, ticker)

# first_time을 UTC timestamp로 변환
# 주어진 문자열을 datetime 객체로 변환 (한국 시간대)
korea_time = first_time_timezone.localize(datetime.strptime(first_time, '%Y-%m-%d %H:%M:%S'))
utc_time = korea_time.astimezone(pytz.utc) # 한국 시간을 UTC 시간으로 변환
# UTC 시간을 타임스탬프로 반환 (Unix Epoch 기준)
utc_timestamp = int(utc_time.timestamp()) * 1000

data_source.make_new_csv_file() # 빈 csv파일 생성하기

data_source.fetch_and_update_csv(utc_timestamp) # 지정된 시간부터 1분봉 데이터 가져오기