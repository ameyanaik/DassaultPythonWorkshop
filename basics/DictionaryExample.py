employeesDictionary = {
    1001: "Tom",
    1002: "John",
    1003: "Mark",
    1004: {
        "name": "Brenda",
        "empID": 1004,
        "tel": 6765432012,
        "address": {
            "street1": "some address",
            "zip": 671875
        }
    }
}

print(employeesDictionary)
print(employeesDictionary[1001])

print("Employee 1001 is: %s" % employeesDictionary[1001])

#Get All items including keys and values
print(employeesDictionary.items())

#Get All values in a dictionary
print(employeesDictionary.values())

#Get All Keys
print(employeesDictionary.keys())

dict2 = {
    1004: "Joe",
    1005: "Ben"
}

#Update an existing dictionary with new data
employeesDictionary.update(dict2)
print(employeesDictionary)

dict2.clear()

print(dict2)

print(employeesDictionary.pop(1005))
print(employeesDictionary)

print(employeesDictionary.popitem())
print(employeesDictionary)

for x in employeesDictionary.keys():
    print(employeesDictionary.get(x))

for x,y in employeesDictionary.items():
    print(x,y)
