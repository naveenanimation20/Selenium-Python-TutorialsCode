from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('http://amazon.in')

driver.find_element(By.LINK_TEXT, 'Best Sellers').click()
time.sleep(2)

driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.back()
time.sleep(2)

driver.refresh()

driver.quit()