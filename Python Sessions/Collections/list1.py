'''
--------------------------------Common List Methods------------------------------------
        Method	                                        Description
    append(x)	                        Adds an item x to the end of the list
    extend(iterable)	            Adds all elements of an iterable to the list
    insert(i, x)	                        Inserts x at position i
    remove(x)	                        Removes the first occurrence of x
    pop([i])	                            Removes and returns the item at index i
    index(x)	                            Returns the index of the first occurrence of x
    count(x)	                            Counts occurrences of x in the list
    sort()	                                Sorts the list in ascending order
    reverse()	                        Reverses the list in place
    copy()	                                Returns a shallow copy of the list
    clear()	                            Removes all elements from the list
'''

list1=['Apple','Banana','Cherry','Orange']
print(list1)
print('-----------------------------------------------------')
print(list1[0:3]) # Will print 0 to 3-1 mean  (three elements)
#Here  0-->from and 3--> to
print('-----------------------------------------------------')

print(list1[0:])# Will Print 0 to length-1 (Default)
print('-----------------------------------------------------')

print(list1[:3]) # Will Print 0 to 3-1 (Default) starting from 0(zero).
print('-----------------------------------------------------')

list1.sort()
print(list1) # Sorting by Alphabetical order and ASC (A to Z)
print('-----------------------------------------------------')

list1.sort(reverse=True)
print(list1) # Sorting by Alphabetical Order and DESC (Z to A)
print('-----------------------------------------------------')

list1.reverse() # used for reversed list elements
print(list1)
print('-----------------------------------------------------')

print(list1.index('Apple')) # Return the index of this element
print('-----------------------------------------------------')

print(list1.index('Banana',1)) # Second argument is, where do you want search from
print('-----------------------------------------------------')

length=len(list1)# Return the list length
print(length)
print('-----------------------------------------------------')

list1.clear() # clear all the elements of list but list will not be deleted
print(list1)# EMPTY List
print('-----------------------------------------------------')

list1.append('Apple') # add a new element at the end position of the list
print(list1)
print('-----------------------------------------------------')

print("Print List by using of Loop")
# 1 Way
length = len(list1)
for i in range(length):
    print(list1[i],end=" ")
print()
print('-----------------------------------------------------')
# 2 Way
for i in list1:
    print(i,end=" ")


print('-----------------------------------------------------')

del(list1)#List Deleted
#print(list1) # Cannot be access again







