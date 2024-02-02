import requests
from openpyxl import Workbook
from datetime import datetime
import time

# 엑셀 파일 생성
wb = Workbook()
ws = wb.active
ws.append(["Time", "Bitcoin Price1"])

# 업비트 API 엔드포인트와 요청 헤더 설정
url = 'https://api.upbit.com/v1/ticker'
querystring = {'markets': 'KRW-BTC'}
headers = {'Accept': 'application/json'}

try:
    while True:
        # 업비트 API에 요청을 보내서 데이터 가져오기
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()

        # 현재 시간과 비트코인 가격 가져오기
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        btc_price = data[0]['trade_price']

        # 가져온 데이터를 엑셀에 추가하기
        ws.append([current_time, btc_price])

        # 엑셀 파일 저장
        wb.save('bitcoin_price1.xlsx')

        # 1초 대기
        time.sleep(1)

except KeyboardInterrupt:
    print("프로그램 종료")
