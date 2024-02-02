import pybithumb
import time

def get_price(currency):
    return pybithumb.get_current_price(currency)

def sell_market():
    # 시장가 매도 함수를 작성해야 합니다.
    pass  # 매도 로직을 여기에 추가하세요.

def buy_market():
    # 시장가 매수 함수를 작성해야 합니다.
    pass  # 매수 로직을 여기에 추가하세요.

consecutive_bullish = 0
trading_status = 0

while True:
    previous_price = get_price('BTC')
    time.sleep(1)
    current_price = get_price('BTC')
    price_difference = current_price - previous_price 

    if price_difference > 0:
        consecutive_bullish += 1
        print(f"현재가: {current_price}, 이익: {price_difference}, 양봉입니다. {consecutive_bullish}")
        
        if trading_status == 1:
            if consecutive_bullish > 2:
                sell_market()  # 시장가 매도 함수 호출
                print("매도했습니다.")
                trading_status = 0
        else:
            if consecutive_bullish > 2:
                trading_status = 1
                print("매수 준비 완료.")
    else:
        consecutive_bullish = 0
        print(f"현재가: {current_price}, 이익: {price_difference}, 양봉이 아닙니다.")
