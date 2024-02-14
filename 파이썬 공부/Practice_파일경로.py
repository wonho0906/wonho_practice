'''
상대경로를 이용하여 csv파일을 만드는 방법을 알려줘.
현재 나는 python폴더에 있고 하위 폴더로 data가 있어. data폴더에 krw-btc.csv를 to_csv함수를 이용해서 만들고싶어.
'''

import pandas as pd
import os

# 현재 작업 디렉토리 확인
current_directory = os.getcwd()
print("현재 작업 디렉토리:", current_directory)

# data 폴더의 경로 생성 (상대 경로)
data_folder_path = os.path.join(current_directory, 'data')
print("data 폴더의 경로:", data_folder_path)

# 샘플 데이터프레임 생성
data = {'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'Open': [40000000, 41000000, 38000000],
        'High': [42000000, 43000000, 39000000],
        'Low': [38000000, 40000000, 36000000],
        'Close': [41000000, 42000000, 37000000]}

df = pd.DataFrame(data)

# krw-btc.csv 파일의 경로 생성 (data 폴더 내부)
csv_file_path = os.path.join(data_folder_path, 'krw-btc.csv')
print("krw-btc.csv 파일의 경로:", csv_file_path)

# 데이터프레임을 CSV 파일로 저장
df.to_csv(csv_file_path, index=False)

print(f"{csv_file_path} 파일을 생성했습니다.")
