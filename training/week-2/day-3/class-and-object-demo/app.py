# Python has many built-in types
# Everything in Python is also considered an object
# Primitive types: int, float, str, list, set, dict, tuple, range, bool

# You can define your own types in Python using classes
# and create objects based on those classes

class Person:

    # __init__() is a type of "dunder" method
    # "dunder" -> Double underscore
    # In particular, the purpose of __init__() is to initially populate values for a Person object that is
    # being initialized
    def __init__(self, first_name, last_name, age):
        # self refers to the "current" object
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # Instance methods
    def say_hi(self):
        print(f"Hi, my name is {self.first_name} {self.last_name}, and I am {self.age} years old")

    # Instance methods
    def have_birthday_party(self):
        print("Hooray my birthday is today")
        self.age += 1

# Object creation/instantiation/initialization/construction
# Objects can also be referred to as "instances"
# An "instance of Person" is the same as a "Person object"


p1 = Person("Shushmita", "Das", 25)
p2 = Person("Carol", "Danvers", 28)
p3 = Person("Bach", "Tran", 24)

print(type(p1))  # <class '__main__.Person'>
print(type(p2))  # <class '__main__.Person'>
print(type(p3))  # <class '__main__.Person'>
print()

print(p1.first_name)  # John
print(p2.first_name)  # Jane
print(p3.first_name)  # Bach
print()

print(p1.last_name)  # Doe
print(p2.last_name)  # Doe
print(p3.last_name)  # Tran
print()

print(p1.age)  # 25
print(p2.age)  # 28
print(p3.age)  # 24
print()

p1.say_hi()  # self = p1
p2.say_hi()  # self = p2
p3.say_hi()  # self = p3
print()

p1.have_birthday_party()  # self = p1 => Hooray my birthday is today
print()

p1.say_hi()  # self = p1
p2.say_hi()  # self = p2
p3.say_hi()  # self = p3
print()

# You can actually call the instance methods by referring to the class itself (Person)
# But you still need to provide an object that "self" can refer to
# Not usually done this way follow the previous way
Person.say_hi(p1)
Person.say_hi(p2)
Person.say_hi(p3)
print()

print(p1)  # <__main__.Person object at 0x000001F1385C76D0>
print(p2)  # <__main__.Person object at 0x000001F1385C7670>
print(p3)  # <__main__.Person object at 0x000001F1385C74C0>
print()


class Todo:
    def __init__(self, description):
        self.description = description
        self.completed = False


class User:
    def __init__(self, username, mobile_phone):
        self.username = username
        self.mobile_phone = mobile_phone
        self.todos = []


user1 = User("Bachy21", "512-826-0001")

todo1 = Todo("Sweep floor")
user1.todos.append(todo1)

user1.todos.append(Todo("Make bed"))

print(user1.todos)
print(user1)  # <__main__.User object at 0x0000020378027430>



