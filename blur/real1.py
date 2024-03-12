import pandas as pd

'''
1. 
df = pyupbit.get_ohlcv("KRW-BLUR", interval = "minute1", count = 50 , period = 0.1) # 인덱스에는 시계열데이터가 저장됨

2.
df.to_csv("blur_240312.csv", index = True) # index = True 를 해야 index가 csv파일에 저장된다. index = True안하면 인덱스였던 시계열데이터가 사라지게된다. 
# index = True를 하면 인덱스의 값들이 첫 열에 채워진다.

3.
df = pd.read_csv('blur_240312.csv', index_col = 0, parse_dates=True) # index_col
csv파일은 인덱스 개념이 없음. 따라서 인덱스로 사용할 열을 index_col = '인덱스로 사용할 열' 로 지정해줘야한다.
parse_dates = True를 이용해서 날짜데이터를 파싱해야 인덱스의 시계열데이터의 자료형이 datetime64로 저장된다. # 특정 열에 대해서만 parse_dates를 적용 : parse_dates=['Date1', 'Date2']
'''
df = pd.read_csv('blur_240312.csv', index_col = 0, parse_dates=True)
# sample_df = df.tail(500)
df.to_excel("blur_240312.xlsx")

