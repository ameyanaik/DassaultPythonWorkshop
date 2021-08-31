import csv

f = open("test2.csv", "w")

csv_writer = csv.writer(f, delimiter=',')

csv_writer.writerow(['EmpID','EmpName','BirthDate'])
csv_writer.writerow(['1001','John','1/1/1991'])

f.close()
