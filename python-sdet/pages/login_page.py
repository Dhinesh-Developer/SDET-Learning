
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "input-email")
        self.password = (By.ID, "input-password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self):
        self.driver.get(
            "https://demo.opencart.com/index.php?route=account/login"
        )    

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)

        wait.until(
            EC.visibility_of_element_located(self.username)
        ).send_keys(username)

        self.driver.find.element(
            *self.password
        ).send_keys(password)

        self.driver.find_element(
            *self.login_button
        ).click()

def test_login_page_opens(driver):
    # from pages.login_page import LoginPage

    page = LoginPage(driver)
    page.open()

    assert "login" in driver.current_url.lower()

# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v pages/login_page.py
# ================================= test session starts ==================================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1','html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 1 item                                                                       

# pages/login_page.py::test_login_page_opens PASSED                                [100%]

# ================================== 1 passed in 2.15s ===================================
