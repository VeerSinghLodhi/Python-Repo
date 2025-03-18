
list1=[5,6,4,2,7,8,4,2,5]
print(list1)

# Print all elements by the using of loop
# We have two options in loop to print the all elements in list
# 1 With length
for i in range (len(list1)):# len()--> Length Function
    print(list1[i],end=",")

print()

# 2 Direct
for i in list1:
    print(i,end=",")


print()
# Sorting in ASC ORDER
list1.sort()
print(list1)

print()
# Sorting in DESC ORDER
list1.sort(reverse=True)
print(list1)


