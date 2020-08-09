from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


driver = None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("--------------------setup---------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    yield
    print("--------------------tear down---------------")
    driver.quit()


@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"


@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"

