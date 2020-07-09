from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

#type="file"
driver.find_element(By.NAME, 'upfile').send_keys('/Users/NaveenKhunteta/Desktop/diagram.py')

driver.find_element(By.XPATH, "//input[@type='submit']").click()
