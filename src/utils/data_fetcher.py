# data_fetcher.py - 실시간 데이터 수집 (업비트 API를 활용)
import requests

def fetch_upbit_data(market="KRW-BTC"):
    """
    업비트에서 실시간 BTC/KRW 시세 데이터를 가져옵니다.
    """
    url = f"https://api.upbit.com/v1/ticker?markets={market}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    else:
        raise Exception(f"Failed to fetch data from Upbit API. Status code: {response.status_code}")
