import pandas as pd

# CSV 파일로부터 데이터 읽어오기
df = pd.read_csv(r'C:\Users\Administrator\Desktop\업무관련\사회복무요원\정원호\이것저것\파이썬\blur\KRW-BLUR_upbit.csv')

# 'Unnamed: 0' 열을 인덱스로 설정
df['Unnamed: 0'] = pd.to_datetime(df['Unnamed: 0'])  # 문자열로 된 날짜를 datetime으로 변환 : pyupbit의 ohlcv 데이터의 datetime은 int형으로 되어있어서 datetime으로 바꿔야함.
df.set_index('Unnamed: 0', inplace=True)  # 'Unnamed: 0' 열을 인덱스로 설정 : pyupbit의 ohlcv 데이터는 시계열이 index가 아니라 새로운 열로 지정되어있음.
