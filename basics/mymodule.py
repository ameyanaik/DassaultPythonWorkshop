# This is a module
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, self.age)


message = "Hello World"
x = "This is MyModule"

def main():
    print("printing from mymodule")
    print(x)
    print(message)


if __name__ == "__main__":
    main()

