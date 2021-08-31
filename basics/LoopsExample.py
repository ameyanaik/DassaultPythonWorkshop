list1 = [1,2,3,4,5,6,7]
list2 = ["One", "Two", "Three", "Four"]

i = 0;
while i < len(list1):
    print(list1[i])
    i = i + 1

for i in range(10):
    print(i, end=' ')

print()

for i in range(1,10):
    print(i, end=' ')

print()

# i = iter(list2)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

list2 = ["One", "Two", "Three", "Four", "Five", "Six"]

i = iter(list2)

# j = 0;
# while j < len(list2):
#     print(next(i))
#     j = j + 1

# item = next(i, 'stop')
# while item != 'stop':
#     print(item, end=" : ")
#     item = next(i, 'stop')

item = next(i, None)
while item is not None:
    print(item, end=" : ")
    item = next(i, None)


