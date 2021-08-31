import pandas as pd

data = {
    "calories": [420, 380, 590],
    "duration": [40, 35, 60]
}

df = pd.DataFrame(data, index=['day1', 'day2', 'day3'])

print(df)

print("My Activity on Day 1:\n ", df.loc['day1'])

print("My Calories burned on Day 1:\n ", df.loc['day1', 'calories'])

print("My Activity on Day 1 and 2:\n ", df.loc[['day1', 'day2']])

days = ['day2','day3']

print("My Activity on Day 2 and 3:\n ", df.loc[days])


