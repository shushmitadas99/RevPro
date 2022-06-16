a = "This is a string"
b = 'This is another string'

# Slicing
# Applies not only to Strings like in this example, but also lists and tuples
# Everytime you slice, you're creating a new object, and not a substring
print(a)  # This is a string
print(a[0])  # T => character in first index
print(a[3])  # s
print(a[0:3])  # Thi => last index is not included

print(a[0:-1])  # This is a strin => g is the last index -> -1

print(a[-1])  # g
print(a[15])  # g

print(a[-2])  # n
print(a[14])  # n

# print(a{20])  # IndexError => index out of range

# Skipping indices => a[index: last index : steps]
print(a[0:6:2])  # Ti<space> => 0 2 4 6 (6 excluded)
print(a[0:7:2])  # Ti s

print(a[::-1])  # gnirts a si sihT => reverse order
print(a[::2])  # Ti sasrn
print(a[-5:-2])  # tri => using negative indices for this one

print(a[-6:])  # string => starts at -6 and goes all the way to the end including the end
print(a[-6:-1])  # strin

# String concatenation
print("hello " + "World")
num = 10
print("Number: " + str(num))

# String Methods
print("abc".upper())  # ABC
my_string_1 = "abc"
print(my_string_1.upper())  # ABC

# The upper() method returns a brand-new string object. We know this because strings are immutable
# Therefore, upper does not modify the original "hi" string
my_string_2 = "hi"

my_string_2.upper()
print(my_string_2) # Doesn't change anything => strings are immutable
print(my_string_2.upper())
my_string_2 = my_string_2.upper()  # string now point to HI
print(my_string_2)

# lower()
print("ABC".lower())

# strip() =>  removes whitespace before and after the string
a_string = "       ABC          "
print(a_string.strip())

#replace()
my_string_3 = "Hello"
my_string_3 = my_string_3.replace("l", "p")
print(my_string_3)

# String formatting
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

greeting_message = "Hi, my name is " + first_name + " " + last_name + ", and my age is " + age
print(greeting_message)

greeting_message_2 = "Hi, my name is {} {}, and my age is {}".format(first_name, last_name, age)
print(greeting_message_2)

# f-string
greeting_message_3 = f"Hi, my name is {first_name} {last_name}, and my age is {age}"
print(greeting_message_3)

print("It's a great day!")
# Backslash => escape character
# It eliminates the special meaning of a character such that it only
# considers that character as part of the string literal
print('It\'s a great day!')
print("He said, \"hi there\"")

print("!st line \n 2nd line")  # newline character
print("\t New paragraph blah blah blah")
print("This is a backslash \\")

print("a", end =", ")
print("b", end ="\n")  # a, b
print("c", end ="\n")  # c  => newline is default

print("a", "b", "c", sep="\t")  # a     b       c => tab seperator

# Length of a string
my_string_4 = "Hello, my name is Shushmita Das. I'm a software engineer who loves to build solutions for community."
print(len(my_string_4))  # 100

# Occurrence of a character
print(my_string_4.count("e"))  # 7 e's in the string

# Find where an occurrence is
print(my_string_4.find("engine"))  # 48 (the first occurrence of "engine" starts at index 48)
