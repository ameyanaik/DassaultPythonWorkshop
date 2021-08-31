import pytest


@pytest.mark.parametrize(
    "num1, num2, expected",
    [(2, 3, 5),
     pytest.param(4, 5, 10, marks=pytest.mark.xfail(reason="Expected to Fail due to some reason")),
     (7, 8, 15)]
)
def test_addition(num1, num2, expected):
    result = num1 + num2
    assert result == expected
