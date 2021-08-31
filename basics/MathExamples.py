import math

x = math.log(100,10)
print(x)

pi = math.pi;
radius = 5;

area = pi * radius * radius;
print(area)

print(math.sqrt(100))

print(math.factorial(5))

print(math.e)

print(math.pow(2,15))

print(math.fabs(123.45))

print(round(123.456678, 2))

print('la'*3)

print(13/4)
print(13//4)

print(13%4)

#Assignment: For numbers 1 to 10, print if number is even or odd
#1 : Odd
#2 : Even
#3 : Odd

for i in range(1,11):
    print("number :",i,end=' ')
    if(i%2==0):
        print("Even")
    else:
        print("Odd")

#Write code to find number of characters of each type in a string
#str = "This is a Python Workshop"
#count the number of occurences for each character
str = "This is a Python Workshop"

for c in str:
    print(f'Number of occurrence of {c}:', str.count(c));