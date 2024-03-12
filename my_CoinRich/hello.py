from datetime import datetime

# 주어진 두 날짜 및 시간
start_date = datetime(2023, 6, 27, 0, 0, 0)
end_date = datetime(2024, 3, 12, 10, 35, 0)

# 두 날짜와 시간 간의 차이 계산
time_difference = end_date - start_date

# 총 소요 시간을 분으로 변환
total_minutes = time_difference.total_seconds() / 60

print(f"총 {total_minutes} 분 걸렸습니다.")
