# utils/image_capturer.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import base64
from utils.logger import logger

def capture_chart_image(url="https://upbit.com/full_chart?code=CRIX.UPBIT.KRW-BTC"):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get(url)
        driver.implicitly_wait(10)

        screenshot = driver.get_screenshot_as_base64()
        driver.quit()
        logger.info("Chart image captured")
        return screenshot
    except Exception as e:
        logger.error(f"Failed to capture chart image: {e}")
        return None
