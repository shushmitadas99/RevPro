# Comments which are created using # symbol, allow for the interpreter to
# ignore that text. It will not be considered part of the program
# Comments are intended to make confusing code easier for other programmers.
# Comments should not be abused. You shouldn't overuse comments to explain
# every single line of code

# Rule of thumb: code should be easily self-explanatory as much as possible to other devs

# Variables allow you to store different values
# For example, we create a variable with the name abc (abc is our identifier)
# and we assign it a value of 100j

# Off-topic note: Objects are always stored in a heap

abc = 100
print(abc)  # 100
abc = "hello"  # str
print(abc)  # hello => replaces 100 when abc reassigned

x = 18  # int
y = 20.0  # float
print(x)
print(y)

print(abc)  # hello
print("hello")  # hello

# Datatypes
print(type(abc))  # <class 'str'>
print(type(x))    # <class 'int'>
print(type(y))    # <class 'float'>

