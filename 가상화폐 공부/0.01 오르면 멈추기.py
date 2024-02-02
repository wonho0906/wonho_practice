import time
import pyupbit

def get_bitcoin_price():
    price = pyupbit.get_current_price("KRW-BTC")
    return price

def stop_program():
    global running
    running = False

running = True
prev_price = get_bitcoin_price()

try:
    while running:
        bitcoin_price = get_bitcoin_price()
        print(f"비트코인 현재가: {bitcoin_price} 원")

        # 가격 변동 계산
        if bitcoin_price > prev_price * 1.0001:  # 이전 가격보다 0.01% 이상 상승했을 때
            print("가격이 0.01% 이상 올랐으므로 프로그램을 종료합니다.")
            stop_program()
            break  # 종료
        else:
            prev_price = bitcoin_price  # 이전 가격 업데이트

        time.sleep(10)
except KeyboardInterrupt:
    print("프로그램을 종료합니다.")
