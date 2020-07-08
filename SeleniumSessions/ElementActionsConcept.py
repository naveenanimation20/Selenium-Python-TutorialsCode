from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://app.hubspot.com/login')

username_ele = driver.find_element(By.ID, 'username')
password_ele = driver.find_element(By.ID, 'password')
login_button_ele = driver.find_element(By.ID, 'loginBtn')

act_chains = ActionChains(driver)
act_chains.send_keys_to_element(username_ele, 'batchautomation@gmail.com')
act_chains.send_keys_to_element(password_ele, 'Test@12345')
act_chains.click(login_button_ele).perform()