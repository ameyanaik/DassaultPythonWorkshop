import pytest
import pandas as pd
from data.pandas.MongoDB import read_db


def test_Number_Of_Records():
    df = read_db('localhost', 27017, 'personalinfo')
    assert len(df['firstname']) == 8
