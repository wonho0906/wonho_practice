import time
import pyupbit

def get_bitcoin_price():
    price = pyupbit.get_current_price("KRW-BTC")
    return price

while True:
    bitcoin_price = get_bitcoin_price()
    print(f"비트코인 현재가: {bitcoin_price} 원")
    time.sleep(10)