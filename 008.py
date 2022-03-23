# if statement 

age = int(input("How old are you? "))

if age == 100:
    print("You are really old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("Damn, you're in the womb!")
else:
    print("Ok, you're just a child.")