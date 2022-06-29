from functools import reduce
# Functools module is for higher-order functions that work on other functions
# Higher-order function: Functions taking or returning other functions

# MAP
my_fruits = ["Apple", "Banana", "Apricot", "Peach"]

# Using map, create a new list that will contain the boolean value True if the element starts with an "A"
# and False if the element does not start with "A"
new_list = list(map(lambda x: x[0] == "A", my_fruits))
print(new_list)  # [True, False, True, False]


# Using map, create a new list that will contain the boolean value True if the length of the element is greater
# than 5, otherwise False
greater_that_5 = list(map(lambda x: len(x) > 5, my_fruits))
print(greater_that_5)  # [False, True, True, False]

# FILTER
# Creates a new structure that keeps elements that meet a certain True condition
starts_with_A = list(filter(lambda x: x[0] == 'A', my_fruits))
print(starts_with_A)  # ['Apple', 'Apricot']

# REDUCE
# Combines things into a single value
# reduce(func, iterable, initial_accumulator_value)
# Get sum of elements in list
my_numbers = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, my_numbers))  # 10

# Get product of elements in list
print(reduce(lambda accumulator, e: accumulator * e, my_numbers, 1))  # 24
