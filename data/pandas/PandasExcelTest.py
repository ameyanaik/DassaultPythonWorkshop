import pandas as pd

#Create a test to verify the number of countries who won exactly 1 bronze medal and no other medals is less than 10
def test_verify_single_bronze():
    df = pd.read_excel("Medals.xlsx")
    #bronzecolumn = df['Bronze']
    counter = 0
    for x in df.index:
        if df.loc[x, "Bronze"] == 1 and df.loc[x, "Gold"] == 0 and df.loc[x, "Silver"] == 0:
            counter = counter + 1

    print("Number of countries with exactly 1 bronze are:", counter)
    assert counter < 10


def test_rank_India_48():

    df = pd.read_excel("Medals.xlsx")

    for x in df.index:
        if df.loc[x, "Team/NOC"] == "India":
            assert df.loc[x, "Rank"] == 48


def main():
    df = pd.read_excel("Medals.xlsx")
    #print(df)
    #print(df.to_string())

    print(df.head(10))
    print(df.tail(10))

    print(df.info())


if __name__ == "__main__":
    main()