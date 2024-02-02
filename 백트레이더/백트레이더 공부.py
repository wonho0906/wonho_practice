# https://trading-for-chicken.tistory.com/9


import backtrader as bt


class MyStrategy(bt.Strategy):
    def __init__(self): pass
    # __init__(self) 메서드 부분은 백트레이더의 변수 네이밍 룰에 따라 필요한 변수를 설정해주는 부분이다.
    def next(self): pass
    # next 메서드는 매일 매일 트레이딩을 진행하는 부분이다.
if __name__ == "__main__":
    cerebro = bt.Cerebro()
    cerebro.addstrategy(MyStrategy)
    # Strategy 부분을 설정해주기 전에 Cerebro의 세팅이 우선 되어야 한다.
    # cerebro = bt.Cerebro( )로 cerebro를 설정해주고 addstrategy를 이용해 cerebro에 전략을 설정해준다.
    '''
    이제 전략을 수행할 data를 추가해주어야 하는데, 

    Naver금융에서 데이터를 파싱하여 Backtrader에서 사용가능한 Pandas형태로 바꾸어주는 함수를 만들어 사용한다.
    '''
    df = 
    data = bt.feeds.PandasData(dataname = df)
