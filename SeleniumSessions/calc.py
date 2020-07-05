from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains

import time

browser_name = "chrome"
if browser_name == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(15)
    driver.get("https://www.westpac.co.nz/kiwisaver/calculators/kiwisaver-calculator/")

    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, 'div#calculator-embed iframe'))

    ele = driver.find_element(By.XPATH, "//div[@class='control text-control']//input[@class='ng-pristine ng-valid']")
    ActionChains(driver).move_to_element(ele).send_keys("23").perform()

    driver.find_element(By.XPATH, "(//div[@class='well-value ng-binding'])[1]").click()
    empStatusList = driver.find_elements(By.CSS_SELECTOR, "ul.option-list li div.label span")
    for ele in empStatusList:
        print(ele.text)
        if ele.text == "Self-employed":
            ele.click()
            break