my_var = 10 # my_var

class Animal_1:
    pass

def my_func_1():
    pass

# Rules for identifiers:
# a-z, A_Z, 0-9, _
# Cannot starts with a num
# No special characters


my_string = "hello"
my_int = 24
my_float = 24.34
my_bool = True
my_none = None

# print all types of above variables
print(type(my_string))
print(type(my_int))
print(type(my_float))
print(type(my_bool))
print(type(my_none))
print()

# Arithmetic operators to do math
my_sum = my_int + my_float
print(my_sum)
my_difference = round(my_int - my_float, 2)
print(my_difference)
my_product = my_int * my_float
print(my_product)
my_quotient = my_int / my_float
print(my_quotient)
my_truncated_quotient = my_int // my_float
print(my_truncated_quotient)
my_remainder = 5 % 3
print(my_remainder)
my_exponent = 5 ** 3
print(my_exponent)
print()

# Assignment operators
# =
# +=
# -=
# *=
# /=
# //=
# %=
# **=

# x += 2 -> x = x + 2
# x -= 2 -> x = x - 2
# x *= 2 -> x = x * 2
# etc.


# Function : block of code that can be executed and re-used over and over again
def my_func():
    print("Hello")
    print("Hi")
    print("Greetings")


my_func()  # Function invocation (invoking the function)
my_func()  # Function invocation (invoking the function)
my_func()  # Function invocation (invoking the function)


# Functions can also have parameters (inputs)
def print_sum(num1, num2):  # 2 parameters, num1 and num2
    print(f"The sum of {num1} and {num2} is {num1 + num2}")


print_sum(3, 5)  # first argument corresponds to num1 parameter, second arg corresponds to num2 parameter


# Functions can return a value
def get_num_zero():
    return 0


my_num = get_num_zero()
print(my_num)


# Functions can also have both parameters and return
def addition(num1, num2):
    my_sum1 = num1 + num2
    return my_sum1


print(addition(3.5, 4.5))


# *args and **kwargs
# *args allows us to have an indefinite num of args
def addition(*args):  # args is treated as a tuple
    print(args)
    my_sum2 = 0
    for num in args:
        my_sum2 += num

    return my_sum2


print(addition(10.2, 5.3, 4.5, 6.75, 5.25, 4.23))


# **kwargs allows us to have keyword arguments
def kwargs_demo(**kwargs):
    print(kwargs)
    print(kwargs['keyword1'])
    print(kwargs['keyword2'])
    print(kwargs['keyword3'])


kwargs_demo(keyword1="value1", keyword2="value2", keyword3="value3")


# You can use positional arguments, variable arguments (*args), and keyword arguments (**kwargs) together
def combined_demo(num1, num2, *args, **kwargs):
    print(num1)  # 10
    print(num2)  # 20
    print(args)  # (30, 50, 20)
    print(kwargs)  # { 'keyword1': 10, 'keyword2': 25.4 }
    print(kwargs['keyword1'])  # 10
    print(kwargs['keyword2'])  # 25.4


combined_demo(10, 20, 30, 50, 20, keyword1=10, keyword2=25.4)

# Type conversion
print("\nTYPE CONVERSION")
print("My age is " + str(10))  # We need to convert the int 10 into "10"

print(str(10.54))
print(float("3.2") + float("10.54"))
print(int("10"))
print(int(10.54))  # 10

print("\nFALSY VALUE EXAMPLES")
# Falsy value examples
print(bool(0))  # False
print(bool(""))  # False
print(bool([]))  # False
print(bool(set()))  # False
print(bool(()))  # False
print(bool({}))  # False
print(bool(None))  # False
print(bool(range(0)))  # False

# Truthy value examples
print("\nTRUTHY VALUE EXAMPLES")
print(bool(-10))  # True
print(bool("A string"))  # True
print(bool([1, 2, 3]))  # True
print(bool({1, 2, 3}))  # True
print(bool((1, 2)))  # True
print(bool({'key1': 12, 'key2': 23}))  # True
print(bool(range(5)))  # True
print()

# Slicing can be performed on anything with an index
# Strings, Lists, Tuples have indices
print("\nSLICING")
print(my_string[0:3])  # App
print(my_string[0:-2])  # App
print(my_string[3:0:-1])  # lpp
print(my_string[3::-1])  # lppA
print(my_string[0:5:2])  # Ape
print(my_string[3:])  # le
print(my_string[::-1])  # elppA

# Strings are essentially a sequence of characters
# Strings are immutable, meaning the internal attributes of the string object cannot be changed
# Any of the methods that you can use on a string that "modify" the string will actually return
# a new string object, not modify the original string object
print("\nSTRING METHODS")
my_string = "hello"

# Below is a useless line of code since we are not doing anything with the value it is returning
my_string.upper()  # This does not modify the string object
print(my_string)  # hello

my_string = my_string.upper()
print(my_string)  # HELLO

print("\nCOMPARISON OPERATORS")
# Comparison operators
# Allows us to compare two values and return True if it's a yes, False if it's a no

print(2 == 2)   # True
print(2 == 3)  # False
print(2 != 2)  # False
print(2 != 3)  # True
print(2 > 2)  # False
print(2 > 1)  # True
print(2 >= 2)  # True
print(2 >= 3)  # False
print(2 <= 2)  # True
print(2 <= 3)  # True
print(2 <= 1)  # False


class Dog:
    pass


# There is also the "is" operator to see if two variables are pointing to the same object or not
d1 = Dog()
d2 = Dog()
print(d1 is d2)  # False because d1 and d2 are referring to two different Dog objects

d3 = Dog()
d4 = d3  # d4 is pointing to the same object as d3
print(d4 is d3)  # True

# Logical operators
# and, or, not
print("\nLOGICAL OPERATORS")
print("\nAND")
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
print(True and True)  # True

print("\nOR")
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
print(True or True)  # True

print("\nNOT")
print(not True)  # False
print(not False)  # True

print("\nMEMORY MANAGEMENT")
# Memory management
# Stack is where variables that are not attributes of object will go
d5 = Dog()  # d5 is in the stack, the Dog object is in the heap
d6 = d5

# garbage collection
d6 = None
d5 = None  # d5 and d6 is now referring to None, and therefore the Dog object previously instantiated
# will now be automatically destroyed by the garbage collector
print("\nCONTROL FLOW")
# Control flow
# if, elif, else
# for loops
# while loops

print("\nIF, ELIF, ELSE")
# prints out c
if False:
    print("a")
elif False:
    print("b")
elif True:
    print("c")
else:
    print("d")


# prints out b
if False:
    print("a")
elif True:
    print("b")
elif True:
    print("c")
else:
    print("d")


# prints out d
if False:
    print("a")
elif False:
    print("b")
elif False:
    print("c")
else:
    print("d")


print("\nWHILE LOOPS")
# While loops
x = 0
while x < 100:
    print(x, end=", ")
    x += 1
print()

print("\nFOR LOOPS")
# For loop
# for loops are used to iterate over iterables
# range
for num in range(100):
    print(num)
print()

# list (ordered)
for element in [12, 5, 8, 20]:
    print(num)
print()

# tuple (ordered)
for element in ('a', 12, 12.2, 'test'):
    print(element)
print()

# set (not ordered)
for element in {'apple', 12.5, 'banana', 'test'}:
    print(element)
print()

# dict
my_dict = {'key1': 12.5, 'key2': 34.5}
for key in my_dict:
    print(key)
    print(my_dict[key])
print()

# str
for character in "Hello world":
    print(character)
