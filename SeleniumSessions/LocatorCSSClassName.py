from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")

#driver.find_element(By.CSS_SELECTOR, '#username').send_keys("naveen30@gmail.com")
# driver.find_element(By.CLASS_NAME,'login-email').send_keys("naveen@gmail.com")
# driver.find_element(By.CLASS_NAME, 'login-password').send_keys("test@123")
# driver.find_element(By.CLASS_NAME, 'login-submit').click()

#driver.find_element(By.CSS_SELECTOR, 'input.form-control.private-form__control.login-email').send_keys("test@gmail.com")
#driver.find_element(By.XPATH, "//input[@class='form-control private-form__control login-email']").send_keys("test@gmail.com")

#driver.find_element(By.CLASS_NAME, 'form-control private-form__control login-email').send_keys("test@gmail.com")

# form-control private-form__control login-email
#form-control private-form__control login-password m-bottom-3

#driver.find_element(By.LINK_TEXT, 'Sign up').click()
#driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign').click()