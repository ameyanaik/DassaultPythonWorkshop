import pytest


def test_subtract():
    result = 3-2
    print("Subtraction result is: ",result)


def test_addition(test_data):
    result = test_data[0] + test_data[1]
    print("Test Is complete: Result of Addition is: ", result)


@pytest.mark.parametrize(
    "first_value, second_value, third_value",
    [
     ('first_value', 'second_value', 7),
     ('first_value', 'second_value', 4),
     ('first_value', 'second_value', 6)
     ],
    indirect=['first_value','second_value']
)
def test_addition_with_fixture_params(first_value, second_value, third_value):
    result = first_value+second_value+third_value
    print(result)




#Assignment:
#Create a CSV file with following columns
#Number1, Number2, Operation, ExpectedResult
#Read Data from CSV File
#Pass it as a Data Driven Input to a Pytest Function
#Use Fixtures and @pytest.mark.parameterize wherever required
#Do the operations in the test and validate the expected values

# import sys
#
# print("sys path:", sys.path)
# sys.path.append("/Users/ameya/Projects/DassaultPythonWorkshop/fileio")
# print("sys path:", sys.path)

# from fileio import utils

# import common.utils as utils

import sys
sys.path.append('/Users/ameya/Projects/DassaultPythonWorkshop')

from fileio import utils

@pytest.mark.parametrize("num1,num2,operation,expected",
                         utils.read_csv("/Users/ameya/Projects/DassaultPythonWorkshop/fileio/calculations.csv")
                         )
def test_calculator_csv(num1, num2, operation, expected):
    result = eval(f"{num1}{operation}{num2}")
    print(f"{num1} {operation} {num2} = {expected}")
    assert result == int(expected)

