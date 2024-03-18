from selenium import webdriver
import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chromeDriverPath = 'chromedriver1'
s = Service(os.getcwd() + '/chromeDriverPath')
driver = webdriver.Chrome(service=s)

url = 'https://www.google.com/'
xpath = '//*[@id="SIvCob"]'
for i in range(3):
    driver.get(url)
    time.sleep(3)
    price = driver.find_element("xpath", xpath)
    price_html = price.get_attribute("innerHTML")
    print(price_html)
