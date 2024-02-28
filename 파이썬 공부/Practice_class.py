import ccxt

def get_btc_listing_time():
    exchange_id = 'upbit'
    symbol = 'BTC/KRW'

    exchange = ccxt.upbit()
    market = exchange.load_markets()[symbol]
    ticker = exchange.fetch_ticker(symbol)

    listing_time = market['timestamp']
    print(f'BTC 상장 시간: {listing_time}')

get_btc_listing_time()
