# Encapsulation reason: prevent other programmers from using your class in unintended ways

class Person:
    # Constructor: used to populate values when an object is created => dunder method
    def __init__(self, fn, ln, a):
        self.__first_name = fn  # __ is used to signify that an attr is private
        # private means that the attr cannot be accessed directly outside the class
        self.__last_name = ln  # __last_name is attribute and ln is parameter
        self.__age = a
        self.__full_name = f"{self.__first_name} {self.__last_name}"

    # Dunder methods:
    # This dunder method will replace the original string representation when printing out eh obj
    # The default behavior is <person.Person obj at <memory address>>
    def __str__(self):
        return f"Person object [first_name = {self.__first_name}, last_name = {self.__last_name}, age = {self.__age}]"

    # The length of a person is defined as the len of their full name
    def __len__(self):
        return len(self.__full_name)

    # Dunder method to check if the element exists in the object
    def __contains__(self, name):
        if name in self.__full_name:
            return True

        return False

    def say_hi(self):
        print(f"Hi my name is {self.__first_name} {self.__last_name}, and my age is {self.__age}")

    # Getters: Used for retrieve value from private attributes
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age

    def get_full_name(self):
        return self.__full_name

    # Setters: Used to set value for private attributes
    def set_first_name(self, first_name):
        self.__first_name = first_name
        self.__full_name = f"{self.__first_name} {self.__last_name}"

    def set_last_name(self, last_name):
        self.__last_name = last_name
        self.__full_name = f"{self.__first_name} {self.__last_name}"

    def set_age(self, age):
        self.__age = age
