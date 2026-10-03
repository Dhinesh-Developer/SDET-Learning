import logging

logging.basicConfig(
    filename="test_execution.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    force=True
)

logger = logging.getLogger(__name__)

def test_login_validataion():
    logger.info("Starting login validation")

    username = "admin"
    password = "admin123"

    logger.debug("Username supplied")
    assert username == "admin"
    assert password == "admin123"

    logger.info("Login validation passed")


# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v logging/writing_logs.py
# =============================== test session starts ===============================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 1 item                                                                  

# logging/writing_logs.py::test_login_validataion PASSED                      [100%]

# ================================ 1 passed in 0.01s ================================