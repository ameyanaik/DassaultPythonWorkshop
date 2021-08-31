print("Enter First Number: ")

x = input()

print("Enter Second Number: ")

y = input()

if int(x) > int(y):
    print(f"{x} is greater than {y}")
elif int(x) == int(y):
    print("Both inputs are equal")
else:
    print(f"{y} is greater than {x}")

print(f"{x} is greater than {y}") if int(x) > int(y) \
    else print("Equal") if int(x) == int(y) \
    else print(f"{y} is greater than {x}")

z = 100

if int(x) > int(y) and int(x) > z:
    print("x is the largest")
else:
    print("x is not the largest")