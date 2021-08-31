import pytest
import pandas as pd
from data.pandas.MySQLDB import read_db
import matplotlib.pyplot as plt

def main():
    df = read_db('localhost', 'testdata', 'ameya', 'ameya123', 'employee')
    df['empdept'].hist()
    plt.show()


if __name__ == "__main__":
    main()