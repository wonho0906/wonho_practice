from pybithumb import Bithumb

df = Bithumb.get_candlestick("BTC", chart_intervals="1m")
print(df.tail(3))
