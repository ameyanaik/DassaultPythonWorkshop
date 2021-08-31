set1 = set(['Ram','Shyam', 'Sam'])

set2 = {'One','Two','Three', 4}

set3 = set1.union(set2)

print(set3)

print(set1, set2)

set2 = set1.copy()

print(set2)

print(type(set2))

for x in set2:
    print(x)

print("Sam" in set2)

set2.add("Ameya")

print(set2)


set2.update({'One','Two','Three','Four', 'Ram'})

print(set2)

set2.remove('Four')

print(set2)

print(set2.pop())

set2.clear()

print(set2)

set4 = {'One','Two','Three'}
set5 = {1, 'Two', 'Three'}

set6 = set4.intersection(set5)

print(set6)

set4.intersection_update(set5)

print(set4)