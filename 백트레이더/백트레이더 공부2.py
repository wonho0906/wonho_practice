import pandas as pd
import os
print(os.getcwd())

file_path = 'C:/Users/asus/Desktop/파이썬 연습용/bithumb-krw_btc-20240110.csv'
df = pd.read_csv(file_path)
print(df)
