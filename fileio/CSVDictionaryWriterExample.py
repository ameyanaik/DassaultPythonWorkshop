import csv

def write_row(csvw,dictobject):
    csvw.writerow(dictobject)

f = open("test3.csv", "w")
headers = ['EmpNo','EmpName','Dept']
csv_writer = csv.DictWriter(f,fieldnames=headers)

csv_writer.writeheader()

dict1 = {
    'EmpNo': 2001,
    'EmpName': "Sachin",
    'Dept': "IT"
}
csv_writer.writerow(dict1)
csv_writer.writerow({
    'EmpNo': 2002,
    'EmpName': "Rahul",
    'Dept': "IT"
})
write_row(csv_writer,{'EmpNo': 2003, 'EmpName': 'Amit', 'Dept': "HR"})

f.close()

f = open("test3.csv", "a")
csv_writer = csv.DictWriter(f, fieldnames=headers)

write_row(csv_writer, {
    'EmpNo': 2004,
    'EmpName': "Sourav",
    'Dept': "Security"
})

f.close()
