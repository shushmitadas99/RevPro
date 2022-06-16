weather = input("Is it sunny, rainy, or snowy: ")

if weather == "sunny":
    print("It is sunny")
    print("Don't bring an umbrella")
elif weather == "rainy":
    print("It is raining")
    print("Bring an umbrella")
elif weather == "snowy":
    print("It is snowing")
    print("Go make a snowman")
else:
    print("It is not sunny but also not raining or snowing")

print("\nRest of the program")

print("\nNested-if statements")
gender = input("Are you male or female? ")
age = int(input("What is your age? "))

if gender == "male":
    if age < 18:
        print("You are a boy")
        # pass: passes the empty conditional block without throwing error
    else:
        print("You are a man")

if gender == "female":
    if age < 18:
        print("You are a girl")
    else:
        print("You are a woman")
