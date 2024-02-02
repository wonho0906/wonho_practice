import pybithumb
import time

def get_price(currency):
    ticker = pybithumb.get_current_price(currency)
    return ticker

consecutive_bullish = 0  # 연속 양봉 횟수를 저장할 변수
trading_status = 0
while True:
    if trading_status == 1:
        #매도함수 입력!
        trading_status = 0 # while문 시작할 때 trading_status = 1이라면 (= 매수 상태라면) 0으로 전환. (=매도하기)
        previous_price = get_price('BTC')
        time.sleep(1)  # 1초 대기
        current_price = get_price('BTC')

        price_difference = current_price - previous_price 

        if price_difference > 0:
            consecutive_bullish += 1
            print("현재가:",current_price,"이익: ", price_difference," 양봉입니다. ",consecutive_bullish)
            if consecutive_bullish > 2:
                trading_status +=1 #여기서 시장가 매수함수 입력!                 
                print("매수했습니다.")

        else:
            consecutive_bullish = 0  # 연속 양봉 횟수 초기화
            print("현재가:",current_price,"이익: ", price_difference," 양봉이 아닙니다.")
    
    else:
        previous_price = get_price('BTC')
        time.sleep(1)  # 1초 대기
        current_price = get_price('BTC')

        price_difference = current_price - previous_price 

        if price_difference > 0:
            consecutive_bullish += 1
            print("현재가:",current_price,"이익: ", price_difference," 양봉입니다. ",consecutive_bullish)
            if consecutive_bullish > 2:
                trading_status +=1 #여기서 시장가 매수함수 입력!                 
                print("매수했습니다.")

        else:
            consecutive_bullish = 0  # 연속 양봉 횟수 초기화
            print("현재가:",current_price,"이익: ", price_difference," 양봉이 아닙니다.")

# 출력했을때의 현재가와 이전의 현재가를 비교했을 때의 이익이 다른 이유: 이전에 출력한 현재가(=current_price)가 현재의 출력한 이익(price_difference)을 구하는데 사용되는 previous_price가 아니기 때문.