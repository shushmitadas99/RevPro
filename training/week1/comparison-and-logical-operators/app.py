print("\nComparison Operators: testing for strings")
print(3 == 3)  # True
print("dog" == "dog")  # True
print("dog" != "dog")  # False
print("dog" != "cat")  # True
print("dog" == "cat")  # False

print("\nComparison Operators: testing for numbers")
print(3 == 3.0)  # True
print(3 == 3.01)  # False
print(2 > 3)  # False
print(2 < 3)  # True
print(2 >= 2)  # True
print(3 <= 4)  # True

# Note: Multiple string literals with same value will point to same String object in string pool within the heap
# In python, everything is an object : refer to week 1-day 3 miro board

print(3 is 3.0)  # False
# The 'is' operator compares to see if both sides are the same object
# The left side is an object, while the right side is float object

print(3 is 3)  # True
print("hi" is "hi")  # True

# Variables are stored in stack and Objects are stored in Heaps
greeting = "hi"  # variable 'greeting' is pointing/referring to string object "hi"
print(greeting is "hi")  # True

my_string = input("input a string: ")
print(my_string is "hi")  # False => strings are immutable, so different string objects

# The id function will return a unique identifier for an object (memory address)
print("\nid() function: ")
print(id("hi"))
print(id(3))
print(id(3))
print(id(3.0))

print("\nTesting int and float equality")
print(float(3) is 3.0)  # False
print(int(3.0) is 3)  # True => inconsistent

x = 3
print(x is 3)  # True

x = int(3.0)
print(x is 3)

# Logical Operators
print("\nLogical Operators: ")
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

print("\nAnd operator: ")
print(5 > 2 and 4 < 100)  # True
print(5 > 10 and 2 < 100)  # False

print("\nOr operator: ")
print(5 == 5 or 2 == 3)  # True
print(10 == 10 or 5 == 5)  # True

print("\nNot operator: ")
print(not True)  # False
print(not False)  # True

x = 10
print(not x == 11)  # True
print(not x == 10)  # False

print((True and True) or (True and False))
# True or (True and False)
# True or False
# True
