my_set = {10, 20}  # Creating a set pre-populated with values 10 and 20
print(my_set)

# Creating an empty set
my_set2 = set()  # We cannot do my_set_2 = {}, because that will actually create an empty dict
print(type(my_set2))  # <class 'set'>

my_string = "abbbaaacccdddddeeefss"

# We want to retrieve all the unique characters in the string
for char in my_string:
    my_set2.add(char)  # If you try to add a value that already exists in the set, it will not add it a second time

for char in my_set2:
    print(char)  # print unique characters in set

print("\nSET METHODS")
# Set Methods
# .add()
# .clear()
# .copy()
# .difference()
# .intersection()
# .union()

# .discard(): remove a specified value (if it exists)
# .pop(): removes a random value from the set

my_set3 = {1, 2, 3, 4}
my_set4 = {3, 4, 5, 6}

# Intersection
print(my_set3.intersection(my_set4))  # intersection does not mutate the set, it will create a brand new set
# intersection_update does mutate

# Difference
print(my_set3.difference(my_set4))  # difference does not mutate the set, it will create a brand new set
# difference_update does mutate

# Union
print(my_set3.union(my_set4))
