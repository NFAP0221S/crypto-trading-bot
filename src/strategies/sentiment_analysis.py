# sentiment_analysis.py - 시장 뉴스 및 공포/탐욕 지수 분석
import requests

def fetch_fear_greed_index():
    """
    공포 탐욕 지수 데이터를 가져옵니다.
    """
    url = "https://api.alternative.me/fng/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['data'][0]['value'], data['data'][0]['value_classification']
    else:
        raise Exception(f"Failed to fetch Fear and Greed Index. Status code: {response.status_code}")
