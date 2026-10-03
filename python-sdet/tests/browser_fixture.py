import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

def test_homepage(driver):
    driver.get("https://example.com")
    assert "Example Domain" in driver.title


# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v tests/browser_fixture.py
# ====================== test session starts ======================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 1 item                                                

# tests/browser_fixture.py::test_homepage PASSED            [100%]

# ======================= 1 passed in 3.84s =======================