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
total_data_count = (end_date - start_date).days * 24 * 60 // 5  # 전체 데이터 개수 계산

print("데이터 다운로드를 시작합니다.")
print("진행 중...")

while start_date < end_date:
    df = pyupbit.get_ohlcv(ticker, interval, to=start_date.strftime("%Y-%m-%d %H:%M:%S"), count=200)
    data.append(df)
    start_date = df.index[0] - timedelta(seconds=1)

    # 진행률 표시
    downloaded_data_count = len(data) * 200
    progress_percentage = min(100, downloaded_data_count / total_data_count * 100)
    print(f"진행률: {progress_percentage:.2f}% 완료", end="\r")

result = pd.concat(data).sort_index()
file_name = "BLUR_5min_data.xlsx"
result.to_excel(file_name)
print("\n데이터 다운로드가 완료되었습니다.")
print(f"데이터를 {file_name}에 성공적으로 저장했습니다.")
