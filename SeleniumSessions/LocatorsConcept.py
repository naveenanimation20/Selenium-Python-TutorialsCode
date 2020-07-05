from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)

username_url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_FirstName')
last_name = driver.find_element(By.ID, 'Form_submitForm_LastName')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
feature_link = driver.find_element(By.LINK_TEXT, 'Features')

username_url.send_keys("naveenautomationlabs")
first_name.send_keys("Naveen")
last_name.send_keys("automationlabs")
email.send_keys("naveen@gmail.com")
feature_link.click()
