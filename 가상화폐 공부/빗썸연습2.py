import pybithumb
import time

# 5개의 원화 상장된 암호화폐 리스트
selected_currencies = ['BTC', 'ETH', 'XRP', 'STRAX', 'BLUR']

def get_price(currency):
    ticker = pybithumb.get_current_price(currency)
    return ticker

def compare_prices(currency):
    current_price = get_price(currency)
    time.sleep(1)  # 1초 대기
    previous_price = get_price(currency)

    price_difference = (current_price - previous_price) / previous_price * 100
    if price_difference >= 0.01:
        return True
    return False

while True:
    for currency in selected_currencies:
        current_price = get_price(currency)
        print(f"{currency}의 현재 가격: {current_price}")
    
    for currency in selected_currencies:
        if compare_prices(currency):
            print(f"{currency}의 가격이 1초 전보다 0.01% 이상 상승했습니다.")
    
    time.sleep(1)  # 1초 대기
