a = 5

def func1():
    a = 1
    print("Inside Function", a)

def func2(arg1, arg2):
    global a
    print(arg1, " : ", arg2, " : ", a)

def func3(arg1, arg2):
    return arg1 + " " + arg2

#Find the cube of a number that the funciton provides
def cube(n):
    return n**3


func1()
func2("Ameya", "Naik")
name = func3("Ameya", "Naik")
print(name)

print(cube(8))


def print_name(firstname, lastname, additionalname=""):
    print(firstname, additionalname, lastname)

print_name("Ameya", "Naik", "Sr")

def print_full_name(firstname, middlename="", lastname="", additionalname=""):
    print(firstname, middlename, lastname, additionalname)

print_full_name("Ameya")
print_full_name("Ameya", additionalname="Sr", lastname="Naik")

def total(a=5, *numbers, **phonebook):
    print('a =:',a)
    print(numbers)
    print(phonebook)

total(1,5,6,7,john=1001,Mark=1002)

def print_variable_full_name(*names):
    """This function taken an unlimited number of arguments and prints them back together.
    This is meant for printing long names"""
    #print(names)
    for name in names:
        print(name, end=" ")
    print()

print_variable_full_name("John","Matt", "Raymond", "Sr")
print_variable_full_name("John")

print(print_variable_full_name.__doc__)

print(max.__doc__)