f = open("a.txt")

#filecontents = f.read();
#print("1: ",filecontents)

#filecontents = f.read(1000);
#print("2: ",f.read(5))

line = f.readline()
print("1: ",line)
print("2: ",f.readline())
print("3: ",f.readline())
print("4: ",f.readline())
print("5: ",f.readline())
print("6: ",f.readline())

#get the position of the current pointer
pos = f.tell();
print(pos)

#Move the pointer back to the first position
f.seek(0)

counter = 0;

while counter<3:
    print(f.readline())
    counter = counter+1

f.seek(42)

print(f.tell())

f.seek(f.tell()-7)

counter = 0;
while counter<4:
    print(f.readline())
    counter = counter+1

# for line in f:
#     print(line)

#print("7: ",f.read())

# list1 = f.readlines()
# print(list1)

print(f.name)
f.close()


#print(f.read())
