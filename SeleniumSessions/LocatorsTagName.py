from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.freshworks.com/")

header_element = driver.find_element(By.TAG_NAME, 'h1')
print(header_element.text)

