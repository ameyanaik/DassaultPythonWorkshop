import pytest
import pandas as pd
from data.pandas.MySQLDB import read_db
import matplotlib.pyplot as plt


def test_Number_Of_Records():
    df = read_db('localhost','testdata','ameya','ameya123','employee')
    assert len(df['empid']) == 7

def main():
    df = read_db('localhost', 'testdata', 'ameya', 'ameya123', 'employee')
    df.plot()
    plt.show()



if __name__ == "__main__":
    main()