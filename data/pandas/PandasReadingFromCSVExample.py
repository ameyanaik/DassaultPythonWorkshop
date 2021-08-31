import pandas as pd

df = pd.read_csv("testdata.csv")

print(df)

print(df.info())

print(df[['Duration', 'Calories']])

print("First 2 rows: \n", df[0:2])

print("First 2 rows of Duration and Calories:\n", df.loc[[0, 1], ['Duration', 'Calories']])

df1 = df.loc[[0, 1], ['Duration', 'Calories']]

print(df1)

df1numpy = df1.to_numpy()

print(df1numpy)

print(type(df1numpy))