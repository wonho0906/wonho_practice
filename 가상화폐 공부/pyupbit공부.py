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

