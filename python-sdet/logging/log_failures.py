import logging

logger = logging.getLogger(__name__)

def test_division():
    logger.info("Starting divison test")

    try:
        res = 10/0
        assert res == 5

    except ZeroDivisionError:
        logger.exception("Division failed")
        raise    


# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ python -m pytest -v logging/log_failures.py
# =============================== test session starts ===============================
# platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0 -- /home/dhinesh/eclipse-workspace/SDET/python-sdet/.venv/bin/python
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.3', 'Platform': 'Linux-7.0.0-31-generic-x86_64-with-glibc2.39', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'metadata': '3.1.1', 'html': '4.2.0'}}
# rootdir: /home/dhinesh/eclipse-workspace/SDET/python-sdet
# plugins: metadata-3.1.1, html-4.2.0
# collected 1 item                                                                  

# logging/log_failures.py::test_division FAILED                               [100%]

# ==================================== FAILURES =====================================
# __________________________________ test_division __________________________________

#     def test_division():
#         logger.info("Starting divison test")
    
#         try:
# >           res = 10/0
#                   ^^^^
# E           ZeroDivisionError: division by zero

# logging/log_failures.py:9: ZeroDivisionError
# -------------------------------- Captured log call --------------------------------
# ERROR    log_failures:log_failures.py:13 Division failed
# Traceback (most recent call last):
#   File "/home/dhinesh/eclipse-workspace/SDET/python-sdet/logging/log_failures.py",line 9, in test_division
#     res = 10/0
#           ~~^~
# ZeroDivisionError: division by zero
# ============================= short test summary info =============================
# FAILED logging/log_failures.py::test_division - ZeroDivisionError: division by zero
# ================================ 1 failed in 0.08s ================================
# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet$ 