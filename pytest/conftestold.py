import pytest

@pytest.fixture
def test_data(first_value, second_value):
    print("Before Test")
    yield first_value, second_value
    print("After Test")

@pytest.fixture
def first_value():
    return 14

@pytest.fixture
def second_value():
    return 11

@pytest.fixture(scope='class', autouse=True)
def super_setup():
    print("Inside Super Setup. This should print above everything else")

@pytest.fixture(scope='function', autouse=True)
def function_setup():
    print("Inside Function Setup")

@pytest.fixture(scope='module', autouse=True)
def module_setup():
    print("Inside Module Setup. This should print above everything else")

@pytest.fixture(scope='package', autouse=True)
def package_setup():
    print("Inside Package Setup. This should print above everything else")