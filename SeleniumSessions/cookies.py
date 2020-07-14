from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)

driver.get('https://reddit.com')
print(driver.get_cookies())

driver.add_cookie({"name":"python","domain":"reddit.com","value":"python"})
print(driver.get_cookies())
print(driver.get_cookie('domain'))

driver.delete_all_cookies()

print(driver.get_cookies())
#driver.get_screenshot_as_file("screenshot.png")

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')


# cookies = driver.get_cookies()
# for cook in cookies:
#     print(cook)


driver.quit()