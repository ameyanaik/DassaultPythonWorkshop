try:
    f = open("test.txt", "r+")
    print(f.readline())
    try:
        f.write("\nNew Line in the file")
    except Exception as e:
        print(e)
    else:
        print("Able to write file")
        f.seek(0)
        print("Printing from Else: ",f.readline())
except (TypeError, ValueError):
    print("Caught Exception")
else:
    print("Inside Else")
finally:
    print("Inside Finally")
x = "Hello"

if x != "Hello":
    raise ValueError("The value of x is not correct")

# if not type(x) is int:
#     raise TypeError("X is not of type int")

class MyException(TypeError):
    def __init__(self, arg):
        if __name__ == '__main__':
            self.message = arg

if not type(x) is int:
     raise MyException("X is not of type int")


