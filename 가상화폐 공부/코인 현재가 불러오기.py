import pyupbit

def get_coin_price(coin_name):
    try:
        # 코인의 마켓 심볼을 가져오기 (예: KRW-BTC)
        market_symbol = f"KRW-{coin_name.upper()}"
        
        # 현재 코인 가격 조회
        coin_price = pyupbit.get_current_price(market_symbol)
        
        # 결과 출력
        print(f"{coin_name}의 현재가: {coin_price} 원")
    except Exception as e:
        print(f"에러 발생: {e}")

# 사용자로부터 코인 이름 입력 받기
coin_name = input("어떤 코인의 현재가를 조회하시겠습니까? ")
get_coin_price(coin_name)
# ex) BTC, .