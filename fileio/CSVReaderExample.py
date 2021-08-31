import csv

f = open("test.csv")
csvf = csv.reader(f, delimiter=",")

for row in csvf:
    print(row)

f.close()

# line_no = 0
# for row in csvf:
#     if line_no ==0:
#         print(row)
#         line_no += 1
#     print(line_no)

f = open("test.csv")
def readCell(f, rowno, columnno):
    csv_reader = csv.reader(f)
    line_no = 0;
    for row in csv_reader:
        if line_no == rowno:
            list1 = row
            return list1[columnno-1]
        line_no += 1

mycell = readCell(f,2,2)
print(mycell)
f.close()