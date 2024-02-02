import backtrader as bt

class MyStrategy(bt.Strategy):
    def __init__(self): pass
    def next(self): pass

if __name__ == "__main__":
    cerebro = bt.Cerebro()
    cerebro.addstrategy(MyStrategy)