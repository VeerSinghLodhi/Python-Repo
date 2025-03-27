'''
set ->
 syntax    set_name={element1,element2,element3,element4};
 this is a set.
 and set doesn't have any index or order
 it has only unique elements. not duplicate elements.
'''
set1={'C','C++','Java','Python','C#','Kotlin'}
set2={'Java','Python','R'}
print(set1)
print(set2)

#print(set1[1])     Cannot be access by the using of index.

# add
set1.add('Python')# Add new Element if the element already exists in the set then it will be considered only one time
print(set1)

# remove
set1.remove('Python') # it is used to to remove a element. if element doesn't exists in the set. then it will be give an  error.
print(set1)

# union   -> LIKE MATH UNION.
# We have two option to achieve union.
print(set1.union(set2)) #1
print(set1 | set2)#2

# intersection
# here also we have two option to achieve intersection
print(set1.intersection(set2))  #1
print(set1 & set2)  #2

# difference
# here also we have two option to achieve difference
print(set1.difference(set2))  #1
print(set1 - set2) #2

# symmetric difference
# here also we have two option to achieve difference
print(set1.symmetric_difference(set2))  #1
print(set1 ^ set2) #2


# we have multiple method to access the set (print)

#1 Direct print
print(set1)

#2 loop
for element in set1:
    print(element ,end=" ")



