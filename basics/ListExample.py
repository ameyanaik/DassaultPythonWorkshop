# Created a List
list1 = ['Ameya', 'Aditya', 'Akshay', 'Anup', 'Atiq', 'Aviral']

# Reading the List
print(list1)

print(len(list1))

list2 = ['Brijesh']

list3 = list1 + list2 * 3

print(list3)

# Updating the List
list3.append("Deepthi")

print(list3)

print(list3.count("Brijesh"))

# Updating the List
list3.extend(['Nagalakshmi', 'Jaya'])

print(list3)

index = list3.index("Anup")

print(index)

list3.insert(0, "Nithin")

print(list3)

# Removing a Value
list3.remove("Ameya")

print(list3)

lastobject = list3.pop()

print("Removed " + lastobject + " from the list")

print(list3)

list3.pop(1)

print(list3)

list3.reverse();

print(list3)

# How can we remove the last object and insert it at the first position
# lastvalue = list3.pop()
# list3.insert(0,lastvalue)
list3.insert(0, list3.pop())
print(list3)

# Print the sum of numbers in the list
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(list4))

result = 0
for x in list4:
    result = result + x

print(result)

# #Remove Duplicates
new_list = []
[new_list.append(x) for x in list3 if x not in new_list]
print(new_list)

# Remove all duplicate names from the list
# finallist=[]
# for i in list3:
#     if i not in finallist:
#         finallist.append(i)
# list3 = finallist
# print(list3)

# Remove all names with number of characters greater than or equal to 7 from list 3
# for i in list3:
#     if len(i) >= 7:
#         list3.remove(i)
# print(list3)

list1 = ['ABC','NAIR','PreetiNAIR','DASSAULT','ABC']
list2 = []
for i in list3:
    if len(i) >= 7:
        print(i)
        list3.remove(i)
    else:
        list2.append(i)

print(list2)

#Create a new list based on an existing list
#list5 = [4,6,8]
list4 = [2,3,4]
list5=[]
for i in list4:
    list5.append(i*2)

print(list5)

#List Comprehension Example
list6 = [i*2 for i in list4 if i > 2]
print(list6)

#strlist=['one','two','three']
#Using list comprehension, create a new list with following data
#newstrlist = ['onetest', 'twotest', 'threetest']
strlist=['one','two','three']
newstrlist = [x+'test' for x in strlist]
print(newstrlist)