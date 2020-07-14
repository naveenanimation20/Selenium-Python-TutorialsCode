from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)

driver.get('https://www.reddit.com/')
#driver.get_screenshot_as_file('reddit_1.png');

'''full screenshot'''
#make sure that you are running in headless mode

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('reddit_full_1.png');

