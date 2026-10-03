import pytest

def is_valid_age(age):
    return 18 <= age >= 60

@pytest.mark.parametrize(
    "age,expected",
    [
        (17, False),
        (18, True),
        (19, True),
        (60,True),
        (61, False)
    ]
)

def test_age_validation(age, expected):
    assert is_valid_age(age) == expected

# (.venv) dhinesh@Arise:~/eclipse-workspace/SDET/python-sdet/tests$ python -m pytest -q pytest_paramerterization/boundary_value_testing.py
# .FF.F                                                     [100%]
# =========================== FAILURES ============================
# _________________ test_age_validation[18-True] __________________

# age = 18, expected = True

#     @pytest.mark.parametrize(
#         "age,expected",
#         [
#             (17, False),
#             (18, True),
#             (19, True),
#             (60,True),
#             (61, False)
#         ]
#     )
    
#     def test_age_validation(age, expected):
# >       assert is_valid_age(age) == expected
# E       assert False == True
# E        +  where False = is_valid_age(18)

# pytest_paramerterization/boundary_value_testing.py:18: AssertionError
# _________________ test_age_validation[19-True] __________________

# age = 19, expected = True

#     @pytest.mark.parametrize(
#         "age,expected",
#         [
#             (17, False),
#             (18, True),
#             (19, True),
#             (60,True),
#             (61, False)
#         ]
#     )
    
#     def test_age_validation(age, expected):
# >       assert is_valid_age(age) == expected
# E       assert False == True
# E        +  where False = is_valid_age(19)

# pytest_paramerterization/boundary_value_testing.py:18: AssertionError
# _________________ test_age_validation[61-False] _________________

# age = 61, expected = False

#     @pytest.mark.parametrize(
#         "age,expected",
#         [
#             (17, False),
#             (18, True),
#             (19, True),
#             (60,True),
#             (61, False)
#         ]
#     )
    
#     def test_age_validation(age, expected):
# >       assert is_valid_age(age) == expected
# E       assert True == False
# E        +  where True = is_valid_age(61)

# pytest_paramerterization/boundary_value_testing.py:18: AssertionError
# ==================== short test summary info ====================
# FAILED pytest_paramerterization/boundary_value_testing.py::test_age_validation[18-True] - assert False == True
# FAILED pytest_paramerterization/boundary_value_testing.py::test_age_validation[19-True] - assert False == True
# FAILED pytest_paramerterization/boundary_value_testing.py::test_age_validation[61-False] - assert True == False
# 3 failed, 2 passed in 0.07s

