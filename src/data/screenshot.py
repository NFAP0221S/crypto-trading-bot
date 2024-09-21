# screenshot.py - 셀레니움을 사용하여 차트 스크린샷을 저장
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def take_screenshot(url, save_path="charts/chart.png"):
    """
    차트의 스크린샷을 저장하는 함수. URL을 받아서 해당 페이지의 스크린샷을 저장합니다.
    """
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.save_screenshot(save_path)
    driver.quit()
