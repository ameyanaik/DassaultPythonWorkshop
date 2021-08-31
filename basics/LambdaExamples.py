# def func1(a):
#     return a*2
#
#
# x = func1(2)
# print(x)
#
# # Lambda Function
# x = lambda a: a * 2
# print(x(2))
#
# x = lambda a,b,c: [a*2,b*3,c*4]
# print(x(2,3,4))


# Usage of Lambda inside a function
# def table(t):
#     r = lambda a: a * t
#     return r
#
# n = 7;
# get_value = table(n)
# print(type(get_value))
# for i in range(1,11):
#     result = get_value(i)
#     print(f"{n} X {i} =", result)


# Function to find whether number exists in a list
# def find_number_in_list(l):
#     return lambda no: no in l
#
#
# list1 = [1,2,3,4,5,6,7]
# x = find_number_in_list(list1)
# result = x(8)
# print(result)


#Find Even number - Criteria
def find_even(num):
    if num%2 ==0:
        return True;
    else:
        return False;

# Filter Concept
# Filter will filter any collection based on the logic tht you provide and return a new collection
# This logic can be created in a function
# This function is passed as a parameter to filter function
# newcollection = filter(criteria, oldcollection)
# criteria should return true or false
# For each element inside oldcollection, the criteria is executed and if it returns true,
# then it is added to newcollection

# OldCollection
list2 = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(find_even,list2))
print("Filter with function: ",result)

result = [i for i in list2 if i%2 == 0]
print("Comprehension: ", result)

result = list(filter(lambda a: a%2 == 0, list2))
print("Filter with Lambda: ",result)

result = list(filter(lambda a: a%2 != 0, list2))
print("Filter with Lambda for ODD: ", result)

# MAP - For each element in oldCollection, apply a transformation and
# create a New Collection
result_cube = list(map(lambda a: a ** 3, list2))
print(result_cube)

result_cube_comprehension = [i**3 for i in list2]
print(result_cube_comprehension)