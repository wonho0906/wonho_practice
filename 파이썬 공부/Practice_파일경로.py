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



"""
## 문자열 앞에 r을 붙이는 이유:

r은 "raw"의 약자로, 파이썬에서 문자열 앞에 붙일 수 있는 접두사 중 하나입니다. r을 사용하면 문자열 안의 이스케이프(escape) 문자를 해석하지 않고 그대로 문자열로 인식합니다.

예를 들어, \n은 줄바꿈 문자를 나타내지만, r을 사용하면 이를 그대로 문자열로 표현할 수 있습니다. 이는 정규 표현식, 파일 경로 등에서 특히 유용합니다. """

"""
## 문자열 앞에 f를 붙이는 이유

f는 "formatted"의 약자로, 파이썬 3.6 버전 이상에서 도입된 f-string을 사용할 때 문자열 앞에 붙입니다. f-string은 문자열 내에서 변수나 표현식을 간편하게 삽입할 수 있도록 하는 기능입니다.

f-string을 사용하면 문자열을 더 간결하고 가독성 있게 작성할 수 있습니다. 변수나 표현식을 중괄호 {}로 감싸면, 중괄호 안에 있는 내용이 해당 변수나 표현식의 값으로 대체됩니다. """