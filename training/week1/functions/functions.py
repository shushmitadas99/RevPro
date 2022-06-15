# This is how you define a function
# The block of code should be indented

def greet():
    print("Hi!")


# invoking/calling/executing the greet function 2 times
greet()  # Hi!
greet()  # Hi!
print(greet())  # Hi! None    => The return type is None


def some_func(x, y):
    value = x + y
    return value


# Whenever you call a function, the invocation of that function is
# an expression, because it gives you a single value
# addition(5, 4.5) is an expression, because it gives you 9.5

print(some_func(5, 4.5))  # 9.5
print(some_func(5 + 2, 4.5 + 2))  # 13.5 => 5 + 2 gets mapped to x and 4.5 + 2 gets mapped to y

# Reminder: expressions can be assigned to variables, passed as arguments,
# or returned inside functions

a = some_func(2, 2.5)
print(a)  # 4.5

print(some_func(some_func(2, 2), some_func(3.5, 4.34)))  # 11.84 => 7 expressions here

print(print("hello"))  # Hello None


def some_func2(x, y):
    return x * y


print(some_func2(2, 3))  # 6
print(type(None))  # print <class 'NoneType'> => Equivalent to Null type

# Scopes
# In python there's 2 scopes
# 1. Global scope
# 2. Function scope

b = 10  # global scope variable


def some_func3():
    b = 20  # function scope variable
    print(b)


def some_func4():
    print(b)


print(b)  # 10
some_func3()  # 20

some_func4()  # This function will print out b in the global scope
