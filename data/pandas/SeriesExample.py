import pandas as pd

a = [1, 7, 2]

print(a)

s1 = pd.Series(a, index=['a', 'b', 'c'])

print(s1)

print(s1['a'])

calories = {'day1': 420, 'day2': 380, 'day3': 390}

s2 = pd.Series(calories)

print(s2)

print(s2['day1'])