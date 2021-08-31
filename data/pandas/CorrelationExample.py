import pandas as pd

df = pd.read_excel("Medals.xlsx")

print(df.corr())

df1 = df[['Gold', 'Total']]

print(df1.corr())

df2 = df[['Gold', 'Rank']]
print(df2.corr())

df3 = df[['Rank', 'Rank by Total']]
print(df3.corr())

df4 = df[['Gold', 'Silver']]
print(df4.corr())