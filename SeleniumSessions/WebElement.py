from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import time

def enter_name(locator, value):
    driver.find_element(By.ID, locator).send_keys(value)


def do_get_title():
    return driver.title


if __name__ == "__main__":
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
    print(do_get_title())
    enter_name("Form_submitForm_subdomain",  "naveen")
