name = input("enter a name: ")
birth_year = input("Enter your birth year: ")  # The input function returns a str
age = 2022 - int(birth_year)

# String concatenation: The process of taking 2 strings and combining them together into a new combined string
# In python, strings are immutable (cannot change the value of string once created)
# Whenever string concatenation is performed, a new string is actually created with the characters from the
# original 2 strings
print("Hello my name is " + name)  # str + str -> str
print("I am " + str(age) + " years old")  # we are using the str function to convert an int to a str

# Type conversion functions
# int(...)
# str(...)
# float(...)
# bool(...)

print(float(10))  # 10.0

# Truthy/Falsy values
# For numbers, 0 is Falsy, while every other number is Truthy
print(bool(0))  # False
print(bool(-1))  # True
print(bool(10))  # True
# Floats
print(bool(0.0))  # False
print(bool(0.12))   # True

# For strings, empty strings are Falsy
print(bool("hi"))  # True
print(bool(""))  # False
print(bool("    "))  # True
