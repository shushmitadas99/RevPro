# Programming languages can do math (most of them)
# We can do so using arithmetic operators
print(2 + 3)      # 5       # Addition
print(100 - 3)    # 97      # Subtraction
print(3 * 3)      # 9       # Multiplication
print(10 / 2)     # 5.0     # Division (always gives you a float)
print(5.0 // 3)   # 1.0     # Integer Division (it will truncate the decimal places)
print(11 % 3)     # 2       # Modulus
print(3 ** 3)     # 27      # Exponentiation

# print(10 / 0) => ZeroDivisionError

#  Boolean Operators
x = 10
print(x == 10)  # True
print(x != 10)  # False

# Assignment Operators
x = 10
print(x)  # 10

x += 2    # x += 2 ---> x = x + 2 ---> x = 12
print(x)  # 12
x -= 5    # x = x - 5
print(x)  # 7

x *= 2
print(x)  # 14

print(x + 100)  # 114  => this doesn't change the value of x
print(x)  # 14

# PEMDAS
# (3 ** 3) * 3 -> (27) * 3 -> 81
print(3 * 3 ** 3)  # 81
