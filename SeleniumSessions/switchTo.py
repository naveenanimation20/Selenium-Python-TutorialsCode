from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

'''frame handle'''
# driver.get('http://www.londonfreelance.org/courses/frames/index.html')
# frame_element = driver.find_element(By.NAME, 'main')
# #driver.switch_to.frame(frame_element)
# #driver.switch_to.frame(2)
# driver.switch_to.frame('main')
# header = driver.find_element(By.CSS_SELECTOR, 'body > h2').text
# print(header)


'''pop up handle'''
# driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
# driver.find_element(By.NAME, 'proceed').click()
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()

'''auth pop up'''
#driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth')

'''file upload pop up'''
driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')
driver.find_element(By.NAME, 'upfile').send_keys('/Users/NaveenKhunteta/Desktop/MyWork.xml')


