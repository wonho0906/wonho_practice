import requests

url = "https://api.upbit.com/v1/candles/minutes/1?market=KRW-BTC&to=2024-02-10 00:00:00&count=200"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)