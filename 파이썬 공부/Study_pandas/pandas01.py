import pandas as pd
import pyupbit 
'''
1.
pd.read_csv() , pd.read_excel()
: CSV나 엑셀파일에서 데이터를 읽어오는 함수.

2.
to_csv() , to_excel()
: 데이터프레임을 CSV나 엑셀 파일로 저장하는 함수.
: df.to_csv("파일명", index = True) 를 입력하면 df의 index가 

3.
df.head(), df.tail()
: 데이터프레임의 처음 또는 마지막 일부를 확인.
df.head(3) : 처음 3개 행을 확인
'''
# df = pd.read_csv(r'C:\Users\Administrator\Desktop\업무관련\사회복무요원\정원호\이것저것\파이썬\blur\KRW-BLUR_upbit.csv')
df = pd.read_csv(r'C:\Users\Administrator\Desktop\업무관련\사회복무요원\정원호\이것저것\파이썬\blur_240312.csv', index_col = 0, parse_dates=True)
print(df.head(3))
print(df.index.dtype)
# df2 = pyupbit.get_ohlcv("KRW-BLUR", interval = "minute1", count = 50 , period = 0.1)
# print(df2.index.dtype)
# print(df.head(1))
# print(df)
# df.to_csv("blur_240312.csv", index = True)
# df2 = pd.read_csv("blur200.csv")
# print(df2.index) """