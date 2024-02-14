'''
KRW-BTC.csv파일이 디렉토리에 존재하는지 확인하고, 존재하지 않는다면 KRW-BTC.csv파일을 만드는 코드를 작성해줘
'''

import os
import pandas as pd

# 파일 경로
file_path = 'KRW-BTC.csv'

# 파일 존재 여부 확인
if os.path.isfile(file_path):
    print(f"{file_path} 파일이 이미 존재합니다.")
else:
    # 새로운 데이터프레임 생성 (여기서는 빈 데이터프레임으로 예시를 들었습니다)
    new_data = pd.DataFrame({
        'Column1': [],
        'Column2': [],
        # ... 필요한 열을 추가하세요
    })

    # 새로운 데이터프레임을 CSV 파일로 저장
    new_data.to_csv(file_path, index=False)
    print(f"{file_path} 파일을 생성했습니다.")
