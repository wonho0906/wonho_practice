import requests

url = "https://api.upbit.com/v1/candles/minutes/1?market=KRW-BTC&to=2024-01-15%2011%3A00%3A00&count=1"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)