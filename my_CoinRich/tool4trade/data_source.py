from datetime import datetime, timezone
import csv
import ccxt
import os

class DataSource:
    """한 거래소의 종목에 대해 데이터를 불러오고 수정하고 가공하는 클래스.

    Attributes:
        exchange (ccxt.Exchange): 사용할 거래소의 ccxt 인스턴스.
        ticker (str): 데이터를 가져올 시장 식별자 (예: 'BTC/USDT').
        csv_file (str): 데이터를 저장할 CSV 파일 경로.
    """
    def __init__(self, exchange_id, ticker):
        """DataSource 클래스의 인스턴스를 초기화합니다.

        Args:
            exchange_id (str): ccxt 라이브러리에서 사용할 거래소의 ID.
            ticker (str): 데이터를 가져올 시장 식별자.
            csv_file (str): 데이터를 저장할 CSV 파일 경로.
        """
        self.exchange = getattr(ccxt, exchange_id)()
        self.ticker = ticker
        # ticker의 '/'를 '_'로 대체하고 모두 소문자로 변경
        formatted_ticker = ticker.replace('/', '_').lower()
        # exchange와 formatted_ticker를 조합하여 새로운 문자열 생성
        self.csv_file = f"db/{exchange_id}/{exchange_id}-{formatted_ticker}.csv"

    def fetch_data(self, since):
        """지정된 시간 이후의 시장 데이터를 가져옵니다.

        Args:
            since (int): 데이터를 가져올 시작 시간 (Unix 타임스탬프, 밀리초 단위).

        Returns:
            list: 가져온 시장 데이터 리스트.
        """
        timeframe = '1m'
        data = self.exchange.fetch_ohlcv(self.ticker, timeframe, since)
        # 현재 분봉은 1분이 다 채워지지 않아 완전하지 않으므로 수집하는 데이터에서 제외한다.
        if isinstance(data, list):
            if len(data) > 1:
                data.pop()
            else:
                data = None
        return data

    def update_csv(self, data):
        """가져온 데이터를 CSV 파일에 추가합니다.

        Args:
            data (list): CSV 파일에 저장할 데이터.
        """
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            for line in data:
                date = datetime.fromtimestamp(line[0] / 1000, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S') + 'Z'
                open_price, high_price, low_price, close_price, volume = line[1], line[2], line[3], line[4], line[5]
                value = open_price * volume
                bull = close_price > open_price if close_price != open_price else None
                writer.writerow([date, open_price, high_price, low_price, close_price, volume, value, bull])

    def fetch_and_update_csv(self, start_time):
        """지정된 시간 이후부터 최근까지의 시장 데이터를 csv 파일에 저장합니다.
        
        Args:
            start_time (int): 데이터를 가져올 시작 시간 (Unix 타임스탬프, 밀리초 단위)"""
        since = start_time
        while True:
            new_data = self.fetch_data(since)
            if isinstance(new_data, list):
                self.update_csv(new_data)
                since = self.get_start_time_from_csv()
            else:
                break

    def make_new_csv_file(self):
        """csv 파일이 존재하는지 확인하고 존재하지 않으면 새 csv 파일을 만들고 존재하면 False를 반환한다."""
        # 파일이 이미 존재하는지 확인
        if os.path.exists(self.csv_file):
            return False  # 파일이 이미 존재하면 False 반환

        # 파일이 존재하지 않으면 파일 생성
        with open(self.csv_file, 'w') as file:
            file.write("time,open,high,low,close,volume,value,bull\n")

        return True  # 파일이 성공적으로 생성되었으면 True 반환

    def get_start_time_from_csv(self):
        """CSV 파일에서 가장 최근의 데이터 시간을 조회하고 1분 후 시간을 반환합니다.

        Returns:
            int or None: 가장 최근 데이터의 시간입니다. Unix 타임스탬프 (밀리초 단위). 데이터가 없는 경우 None을 반환합니다.
        """
        try:
            with open(self.csv_file, 'r') as file:
                last_line = list(csv.reader(file))[-1]
            last_time = datetime.strptime(last_line[0], '%Y-%m-%d %H:%M:%S%z').timestamp()
            start_time = int(last_time * 1000) + 60000 if last_time else None
            return start_time
        except (FileNotFoundError, IndexError):
            return None