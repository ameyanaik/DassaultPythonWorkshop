import csv

def read_csv(path):
    f = open(path)
    csv_reader = csv.reader(f)
    listoftuples = []
    header = next(csv_reader)
    print(header)
    for row in csv_reader:
        listoftuples.append(row)

    f.close()
    return listoftuples

read_csv("something")