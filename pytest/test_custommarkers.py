import pytest
import time as t

@pytest.mark.regression
def test_one():
    #t.sleep(2)
    print("Inside Test One")
    assert 1 == 2

@pytest.mark.regression
def test_two():
    #t.sleep(2)
    print("Inside Test Two")
    assert 1 == 2

@pytest.mark.smoke
def test_three():
    #t.sleep(2)
    print("Inside Test Three")
    assert 1 == 2