tuple1 = ('Ameya','Anup','Brijesh')

print(tuple1)

len(tuple1)

tuple2, tuple3 = (123, 'xyz'), (456, 'abc')

print(tuple2 == tuple3)

print(max(tuple1))

print(min(tuple1))

tuple4 = (1,2,3,4)

print(max(tuple4))

print(min(tuple4))

list1 = list(tuple1)
list1.append("Jaya")
tuple1 = tuple(list1)
print(tuple1)

#Unpacking a Tuple
(name1, name2, name3, name4) = tuple1
print(name1)
print(name2)
print(name3)
print(name4)

print(tuple1[1:3])

print(tuple1.index("Ameya"))

print(tuple1.count("Brijesh"))