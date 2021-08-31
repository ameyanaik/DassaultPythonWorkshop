import csv

f = open("test2.csv")

csv_reader = csv.DictReader(f)

# for row in csv_reader:
#     print(row.get("EmpName"))

for row in csv_reader:
    print(row.keys())

f.close()