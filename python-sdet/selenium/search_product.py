from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_opencart_search(driver):
    driver.get("https://demo.opencart.com/")

    search = WebDriverWait(driver=driver,timeout=15).until(
        EC.visibility_of_element_located(
            (By.NAME, "search")
        )
    )
    search.send_keys("MacBook")

    button = driver.find_element(
        By.CSS_SELECTOR, "#search button"
    )
    button.click()

    WebDriverWait(driver=driver,timeout=15).until(
        EC.url_contains("search=")
    )

    assert "search=" in driver.current_url




