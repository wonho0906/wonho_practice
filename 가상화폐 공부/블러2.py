import pyupbit
import pandas as pd
from datetime import datetime, timedelta

# BLUR의 심볼을 넣어주세요. 만약 BLUR이 존재하지 않는다면 다른 코인의 심볼로 바꿔주세요.
ticker = "KRW-BLUR"
interval = "minute5"

# 데이터 가져오기
start_date = datetime.strptime("2023-11-01 00:00:00", "%Y-%m-%d %H:%M:%S")
end_date = datetime.strptime("2023-12-10 23:59:59", "%Y-%m-%d %H:%M:%S")
data = []

while start_date < end_date:
    df = pyupbit.get_ohlcv(ticker, interval, to=start_date.strftime("%Y-%m-%d %H:%M:%S"), count=200)
    data.append(df)
    start_date = df.index[0] - timedelta(seconds=1)

result = pd.concat(data).sort_index()
file_name = "BLUR_5min_data.xlsx"
result.to_excel(file_name)
print(f"데이터를 {file_name}에 성공적으로 저장했습니다.")
