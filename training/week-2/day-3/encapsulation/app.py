from person import Person

p1 = Person("Shushmita", "Das", 25)
print(p1)

print(p1.get_first_name())
print(p1.get_last_name())
print(p1.get_age())
print(p1.get_full_name())
print()

print(p1.say_hi())  # prints None as it doesn't return anything
print()

p1.set_last_name("Danvers")
print(p1.get_full_name())

p1.set_first_name("Carol")
print(p1.get_full_name())
