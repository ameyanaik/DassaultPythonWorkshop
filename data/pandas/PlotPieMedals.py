import pytest
import pandas as pd
from data.pandas.MySQLDB import read_db
import matplotlib.pyplot as plt


def main():
    df = pd.read_excel("Medals.xlsx")

    print(df)

    # series = df['Gold']
    # labels = df['Team/NOC']

    series = list(filter(lambda x: x > 10, df['Gold']))
    print(series)

    labels = df.loc[0:5, 'Team/NOC']
    print(labels)

    plt.pie(series, labels=labels, autopct='% 0.2f %%')
    #
    plt.show()




if __name__ == "__main__":
    main()