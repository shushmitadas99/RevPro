from person import Person

p1 = Person("Shushmita", "Das", 25)
# When we construct the object __init__() is invoked
print(p1)  # memory address

p2 = Person("Bach", "Tran", 24)
print(p2)

print(len([1, 2, 3]))  # prints the number of elements/characters => 3
print(len("a string"))  # 8
# len() won't work as program doesn't know what the len definition is in this case
# So we define our own __len() for person
print()

print(len(p1))  # 13
print(len(p2))  # 9

print("Shush" in p1)  # True
# the 'in' operator can be used via defining what it means for something to be
# in obj. This is defined via the __contains__(self, name) method
