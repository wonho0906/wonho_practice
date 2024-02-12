
import pyupbit 
import pandas as pd


'''
스페이스 아이디 빗썸 상장 후 업비트 상장, (2024-02-07 14:00:00)
'''

df = pyupbit.get_ohlcv("KRW-ID", "minute1", to = "2024-02-07 07:34:00" , count = 1000)
print(df)
df.to_csv("KRW-ID")