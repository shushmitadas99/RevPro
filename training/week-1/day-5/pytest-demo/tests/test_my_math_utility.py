from utility.my_math_utility import addition


def test_addition_1():
    # assert <boolean expression>
    # assert is used to fail a test case IF the boolean expression is false
    assert addition(10, 20) == 30


def test_addition_2():
    assert addition(2, 3) == 5


def test_addition_3():
    assert addition(1.2, 3) == 4.2

# You run pytest by entering venv and typing the following command:
# python -m pytest <some_directory_name>/<filename>.py
# python -m pytest tests/test_my_math_utility.py -> in our case
# You can also right-click and hit run for the test_utility.py file for pytest
