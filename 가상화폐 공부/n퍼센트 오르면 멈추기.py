# ㅁ코인의 ㅁ초/ㅁ분/ㅁ시간 후 가격이 ㅁ 퍼센트 증가했을 때 출력을 멈추는 프로그램을 짜보자.
import time
import pyupbit

### ㅁ코인 가격 가져오기
def get_coin_price1():
    market_symbol = f"KRW-{coin_name.upper()}"
    price = pyupbit.get_current_price(market_symbol)
    return price


def stop_program():
    global running
    running = False

running = True
coin_name = input("어떤 코인의 현재가를 조회하시겠습니까? ")
prev_price = get_coin_price1()
input_time = input("간격을 몇초로 설정하시겠습니까? ")
time_interval = int(input_time)
input_rise_rate = input("몇% 상승 했을 때 멈출까요? :")
rise_rate = int(input_rise_rate)*1/100 + 1 
print(rise_rate)

try:
    while running:
        price = get_coin_price1()
        print(f"{coin_name}의 현재가: {price} 원")

        # 가격 변동 계산
        if price > prev_price * rise_rate:  # 이전 가격보다 ㅁ% 이상 상승했을 때
            print("가격이 1% 이상 올랐으므로 프로그램을 종료합니다.")
            stop_program()
            break  # 종료
        else:
            prev_price = price  # 이전 가격 업데이트

        time.sleep(time_interval)
except KeyboardInterrupt:
    print("프로그램을 종료합니다.")

