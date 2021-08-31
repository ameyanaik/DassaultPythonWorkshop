import pytest
import pandas as pd
from data.pandas.MySQLDB import read_db
import matplotlib.pyplot as plt

def main():
    df = read_db('localhost', 'testdata', 'ameya', 'ameya123', 'employee')

    y = df['empsalary']
    x = df['empage']

    x = x.sort_values(ascending=True)

    plt.plot(x, y)

    plt.xlabel("Age of the employee")
    plt.ylabel("Salary of the employee")
    plt.title("Relationship between Age and Salary")

    plt.show()


if __name__ == "__main__":
    main()