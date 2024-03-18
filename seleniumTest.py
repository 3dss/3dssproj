from selenium import webdriver
import time
import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chromeDriverPath = sys.argv[1]
driver = webdriver.Chrome(chromeDriverPath)

url = 'https://www.google.com/'
xpath = '//*[@id="SIvCob"]'
for i in range(3):
    driver.get(url)
    time.sleep(3)
    price = driver.find_element("xpath", xpath)
    price_html = price.get_attribute("innerHTML")
    print(price_html)
