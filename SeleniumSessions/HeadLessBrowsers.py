from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

options = webdriver.ChromeOptions()
options.headless = False
options.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


# options = webdriver.FirefoxOptions()
# options.headless = True
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

driver.implicitly_wait(10)

driver.get('http://amazon.in')
print(driver.title)