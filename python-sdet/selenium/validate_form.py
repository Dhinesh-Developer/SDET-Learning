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

def test_from_submission(driver):
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    text_box = WebDriverWait(driver=driver, timeout=10).until(
        EC.element_to_be_clickable((By.NAME, "my-text"))
    )
    text_box.send_keys("Dhinesh")

    driver.find_element(
        By.CSS_SELECTOR, "button"
    ).click()

    message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "message")
        )
    )

    assert message.text == "Received!"

# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v selenium/validate_form.py
# ================================= test session starts ==================================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1','html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 1 item                                                                       

# selenium/validate_form.py::test_from_submission PASSED                           [100%]

# ================================== 1 passed in 4.88s ===================================


