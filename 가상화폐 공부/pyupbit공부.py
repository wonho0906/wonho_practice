import pyupbit

# 암호화폐 목록
'''pyupbit.get_tickers() # 업비트가 지원하는 모든 암호화폐 목록을 얻어옴
'''
# 최근 체결가격
'''pyupbit.get_current_price("KRW-BTC") # 암호화폐의 현재가를 얻어온다.
'''
'''pyupbit.get_current_price(["KRW-BTC", "KRW-XRP"]) # 리스트에 여러개의 티커를 입력해 한 번에 현재가를 조회 가능
'''
'''{'KRW-BTC': 8300000.0, 'KRW-XRP': 511.0} 여러 종목을 조회한 경우 딕셔너리로 현재가를 리턴함.
'''
df = pyupbit.get_ohlcv("KRW-BTC", count = 100  , period = 0.1, interval = "minute5", to = "2024-02-03 09:10:00") # count = 4,000,000 개 
print(df)

# interval을 minute1로 지정한 경우 2020-10-10 보다 1분 이전 (2020-10-09 23:59:00)까지의 데이터를 반환합니다.
# to를 시간 단위까지 입력하면? KST로 반환함. 그런데 to에 입력한 시각 기준으로  9시간을 더함.
# ex) to에 입력한 시각 = utc(협정세계시) >>> 한국은 utc에서 9시간 더한 시각.