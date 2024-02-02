# api key, api secret, 매도주문/매수주문, 거래할 코인, 지정가, 거래량 모두 입력.
import pybithumb

def get_api_keys():
    api_key = input("Bithumb API Key를 입력하세요: ")
    api_secret = input("Bithumb API Secret을 입력하세요: ")
    return api_key, api_secret

def place_limit_order(currency, order_type, price, quantity):
    try:
        if order_type == "buy":
            order_result = bithumb.buy_limit_order(currency, price, quantity)
            print(f"{currency}를 {price}원에 {quantity}개 매수 주문이 완료되었습니다.")
        elif order_type == "sell":
            order_result = bithumb.sell_limit_order(currency, price, quantity)
            print(f"{currency}를 {price}원에 {quantity}개 매도 주문이 완료되었습니다.")
        else:
            print("올바른 주문 타입을 입력하세요 ('buy' 또는 'sell').")
    except Exception as e:
        print("주문이 실패했습니다:", e)

# 사용자로부터 API 키 입력받기
api_key, api_secret = get_api_keys()
bithumb = pybithumb.Bithumb(api_key, api_secret)

# 사용자로부터 거래 정보 입력 받기

order_type = input("매수 주문을 원하시면 'buy', 매도 주문을 원하시면 'sell'을 입력하세요: ")
currency = input("거래할 코인을 입력하세요 (예: BTC, ETH): ")
price = float(input("지정가를 입력하세요: "))
quantity = float(input("거래량을 입력하세요: "))

# 주문 실행
place_limit_order(currency, order_type, price, quantity)