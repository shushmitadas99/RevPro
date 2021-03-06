# External modules that can be imported
# Once we have installed packages using pip from PyPi
# Note: I did it manually from the PyCharm IDE through 'Python Packages' tab
import numpy as np
import silly

# Method 1
# import my_math_utility
#
# print(my_math_utility.addition(10, 20))
# print(my_math_utility.subtraction(40, 20))
# print(my_math_utility.PI)

# Method 2
# import my_math_utility as m
#
# print(m.addition(10, 20))
# print(m.subtraction(40, 20))
# print(m.PI)

# Method 3
from my_math_utility import addition, subtraction, PI

print(addition(10, 20))  # 30
print(subtraction(40, 20))  # 20
print(PI)  # 3.1415

# Following operations done after installing numpy and silly packages
a = np.arange(15).reshape(3, 5)

print(a)
print(type(a))  # <class 'numpy.ndarray'>

name = silly.name()
print(f"My name is {name}")  # My name is ...
