import pybithumb
import time

def get_price(currency):
    return pybithumb.get_current_price(currency)

def buy_market():
    # 시장가 매수 함수 작성
    pass  # 여기에 시장가 매수 로직을 넣어주세요.

consecutive_bullish = 0
trading_status = 0

while True:
    previous_price = get_price('BTC')
    time.sleep(1)
    current_price = get_price('BTC')
    price_difference = current_price - previous_price 

    if trading_status == 1:
        if price_difference > 0:
            consecutive_bullish += 1
            print(f"현재가: {current_price}, 이익: {price_difference}, 양봉입니다. {consecutive_bullish}")
            if consecutive_bullish > 2:
                buy_market()  # 시장가 매수 함수 호출
                print("매수했습니다.")
        else:
            consecutive_bullish = 0
            print(f"현재가: {current_price}, 이익: {price_difference}, 양봉이 아닙니다.")
        trading_status = 0

    else:
        if price_difference > 0:
            consecutive_bullish += 1
            print(f"현재가: {current_price}, 이익: {price_difference}, 양봉입니다. {consecutive_bullish}")
            if consecutive_bullish > 2:
                trading_status = 1
                print("매수 준비 완료.")
        else:
            consecutive_bullish = 0
            print(f"현재가: {current_price}, 이익: {price_difference}, 양봉이 아닙니다.")
