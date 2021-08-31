import pytest
import pandas as pd

# Verify that the column Duration has all elements less than or equal to 60
# expected = 60
# assert actual == expected

def test_duration():
    expected = 60
    df = pd.read_csv("testdata.csv")
    duration = df['Duration']
    print(duration)

    for a in duration.index:
        assert duration.loc[a] <= expected

def test_calories_float():
    df = pd.read_csv("testdata.csv")

    for x in df['Calories']:
        print(type(x))
        assert 'float' in str(type(x))

