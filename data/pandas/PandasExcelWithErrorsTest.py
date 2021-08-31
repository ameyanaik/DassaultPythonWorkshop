import pandas as pd

def is_empty(col, df):
    return bool(df[col].isnull().values.any())


def test_verify_rank_isnot_empty():
    df = pd.read_excel("Medals_withErrors.xlsx")
    #print(df.info())
    #print("Are there any Null Values? ", df['Rank'].isnull().values.any())
    #print("Number of Null Values = ", df['Rank'].isnull().sum())
    #assert bool(df['Rank'].isnull().values.any()) is not False
    assert str(df['Rank'].isnull().values.any()) is not "True"

def test_total_medals_lessthan114():
    df = pd.read_excel("Medals_withErrors.xlsx")
    for x in df['Total']:
        #print(type(x))
        assert x <= 114

def transform_incorrect_total(df):
    counter = 0;
    for x in df['Total']:
        if x > 113:
            df.loc[counter, 'Total'] = x/10
        counter += 1

#Assignment - Remove alphabets from any integer or float column
# def remove_alphabets(df):
#     for x in df:
#         if( x in ['Gold', 'Silver', 'Bronze']):
#             for y in df['x']:




def main():
    df = pd.read_excel("Medals_withErrors.xlsx")

    # Data Transformation
    if is_empty('Rank', df):
        for x in df.index:
            if pd.isnull(df.loc[x, 'Rank']):
                print("Found NaN")
                df.loc[x, 'Rank'] = df.loc[x-1, 'Rank'] + 1

    print(df.head(10))

    if is_empty('Team/NOC', df):
        df['Team/NOC'].fillna('Unknown Country', inplace=True)

    print(df.head(10))

    transform_incorrect_total(df)

    print(df.head(10))

    print(df.tail(10))
    #remove duplicates
    df.drop_duplicates(inplace=True)

    print(df.tail(10))

    print(df.loc[49, 'Silver'])

    # remove_alphabets(df)
    # for x in df.index:
    #     if 'ABC' in df.loc[x, 'Silver']:
    #         new_value = ""
    #         for char in df.loc[x, 'Silver']:
    #             if char not in [r"[a-zA-Z]"]:
    #                 new_value = new_value + char
    #         df.loc[x, 'Silver'] = new_value
    #
    # print(df.to_string())

    df['Silver'].replace(to_replace=r'[a-zA-Z]', value="", regex=True, inplace=True)
    print(df.to_string())

    # df['Silver'].replace(to_replace='2ABC', value="2", inplace=True)
    # print(df.to_string())

    df['Gold'] = df['Gold'].map(lambda x: str(x).lstrip("*").rstrip("*"))
    print(df)







if __name__ == "__main__":
    main()

# use iter() in while loop - Done
# remove alphabets - Done
# Data visualization - Done
# Install Mysql workbench on Mac - Done
# Install MongoDB on Mac - Done