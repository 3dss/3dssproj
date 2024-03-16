from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

for i in range(3):
    driver.get(url)
    time.sleep(3)
    price = driver.find_element("xpath", xpath)
    price_int = float(price.get_attribute("innerHTML")[1:])
    print(price_int)
    if price_int <= my_price:
        print('price dropped!!!')
        
    time.sleep(wait)
