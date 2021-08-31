# f = open("b.txt","a")
# f.write("\nThis is line 8")
# f.close()

# f = open("c.txt", "a+")
#
# for i in range(1,11):
#     f.writelines(f"Line {i}\n")
#
# f.close()
# del f

#Write a program to append to the file by incrementing the line number correctly.
#Create a function to append n number of lines in correct sequence

# f = open("c.txt", 'a+')
# counter = f.tell()
# num = counter / 7;
# print(num)
# for i in range(10):
#     f.writelines(f"\nLine {int(num)+i}")
# f.close()

import linecache
f = open("c.txt")
list1 = f.readlines()
lastline_string = list1[-1]
print(lastline_string)
lastline = len(list1)
line = linecache.getline("c.txt",lastline)
print(line)