my_list = []  # creates an empty list

my_list.append(10)

print(my_list)  # 10
print(type(my_list))  # <class 'list'>

my_list.append("abc")
my_list.append(12)
my_list.append(25)
my_list.append("def")

print(my_list)

print(my_list[0])
print(my_list[1])
print(my_list[2])  # 12
print(my_list[3])  # 25
print(my_list[4])

print()
print(my_list[4 // 2])  # 12

a = 3
print(my_list[a])  # 25

print()  # prints newline
# Challenge: using a while loop, iterate over and print out each element individually from the list
#   0    1     2   3    4
# [10, 'abc', 12, 25, "def"]
# len(my_list) -> 5

# Make sure you really understand how to iterate over a list
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1  # i = i + 1

print()
# Challenge: using a for loop, iterate over the elements of the list and print them individually
for e in my_list:
    print(e)

print()

# Challenge: using a for loop, iterate over the elements of a list and print out both index and the element

# Solution 1
index = 0
for e in my_list:
    print(f"{index}: {e}")
    index += 1

print()

# Solution 2 (better)
for idx, e in enumerate(my_list):
    print(f"{index}: {e}")  # used tuple
print()

my2d_list = [[10, 20], [30, 40]]  # lists as elements within list
print(my2d_list[0][1])  # 20
print(my2d_list[1][0])  # 30

print("\nNested For-loop")
# Nested for loops
for l in my2d_list:
    # print(l)
    for element in l:
        print(element, end=" ")
print()

# Unpacking
print("\nUnpacking")
my_list2 = ["Bach", "Tran", 24]
first_name, last_name, age = my_list2
print(first_name)
print(last_name)
print(age)

print()

fruits = ["apple", "orange", "banana", "pear"]
x, y, *other_fruits = fruits  # * is used when unpacking to put all remaining elements into a list

print(x)  # apple => str
print(y)  # orange => str
print(other_fruits)  # [banana, pear]  => list
print(type(other_fruits))  # <class 'list'>

people = [['Bach', 'Tran'], ['John', 'Doe'], ['Mary', 'Poppins']]
for first_name, last_name in people:  # unpacking
    print(f"{first_name} {last_name}")

# Lists are MUTABLE
print("\nLists are MUTABLE")
my_list3 = [1, 2, 3, 4, 5]  # You can pre-populate elements in the list instead of using
# .append() over and over
print(my_list3)
my_list3.append(22)  # The append method actually modifies (mutates) the list object
# .append() changes the list "in-place"
print(my_list3)  # lists are mutable, so original list changes unlike strings

my_list3[0] = 9999  # replaces element @ index 0 from 1 to 9999
print(my_list3)

# List Methods
print("\nLIST METHODS")
# .append()
# .clear(): remove all elements from the list
# .copy(): return a copy of the list (a brand new object)
# .count(): returns number of elements with specified value
# .extend(): add the elements from another list (or iterable) to the current list
# .index(): returns the index of the first occurrence of a specified value
# .insert(): insert an element at a particular index
# .pop(): remove an element at specified position (or end of list if no position is given)
# .remove(): removes the first element with a specified value
# .reverse(): reverse the list (in-place)
# .sort(): sort the list

my_list4 = [3, 10, -10, 10, 20, 25, 4, 100, 9, 63, 78]
print(my_list4)

my_list4.append(1000)
print(my_list4)

print(my_list4.pop())  # 1000
print(my_list4)

my_list4.pop(5)  # 25
print(my_list4)

my_list4.remove(10)
print(my_list4)

my_list4.insert(2, 800)  # 800 will be inserted @ index 2, and all elements will be shifted right
print(my_list4)

my_list4.extend([10, 20, 30])
print(my_list4)

print()

print(my_list4)
x = my_list4
x[0] = 999999999
print(my_list4)  # [999999999, 10, 800, -10, 10, 20, 4, 100, 9, 63, 78, 1000, 10, 20, 30]

# x and my_list4 are pointing to the same list object
y = my_list4.copy()  # y is pointing to a second list object
y[0] = 888
print(y)
print(my_list4)
print()

# How do you make a copy of list without using .copy()?
# Slicing
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = a[::]  # Slicing creates a copy of the segment in which you are slicing
# in this case, the whole list
b[0] = 1000
print(b)

print(a[0:5:2])  # [1, 2]
print(a[::-1])  # [8, 7, 6, 5, 4, 3, 2, 1]
