import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV 파일로부터 데이터 읽어오기
df = pd.read_csv(r'C:\Users\Administrator\Desktop\업무관련\사회복무요원\정원호\이것저것\파이썬\blur\KRW-BLUR_upbit.csv')

""" # 인덱스를 datetime 형식으로 변환
df.index = pd.to_datetime(df.index)
 """
# 극대값, 극솟값 찾기
peaks = df[(df['high'].shift(1) < df['high']) & (df['high'].shift(-1) < df['high'])]
troughs = df[(df['low'].shift(1) > df['low']) & (df['low'].shift(-1) > df['low'])]

# 'local_extremum_point' 열 추가
df['local_extremum_point'] = np.select(
    [df.index.isin(peaks.index), df.index.isin(troughs.index)],
    ['l_max', 'l_min'],
    default='none'
)

# 중복된 시간을 포함하여 모든 행 선택
all_extremums = df[df.index.isin(peaks.index) | df.index.isin(troughs.index)]

# 새로운 데이터프레임 생성
extremum_df = pd.DataFrame()

# 극점 데이터 추가
extremum_df['timestamp'] = all_extremums.index
extremum_df['price'] = all_extremums['close'].values
extremum_df['local_extremum_point'] = all_extremums['local_extremum_point'].values
""" 
# 극점 간의 시간 간격(분) 추가
extremum_df['time_interval'] = extremum_df.index.to_series().diff().apply(lambda x: x.total_seconds() / 60)
 """
# 극점 간의 수익률 차이(%) 추가
extremum_df['return_difference'] = extremum_df['price'].pct_change() * 100

# CSV 파일로 저장
extremum_df.to_csv(r'C:\Users\Administrator\Desktop\업무관련\사회복무요원\정원호\이것저것\파이썬\blur\all_extremum_data.csv', index=False)

