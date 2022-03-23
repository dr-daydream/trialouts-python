# logical operators (and, or & not)

temp = int(input("What is the temperature outside? "))

if not (temp >= 0 and temp <= 30):
    print("The temperature is good today.")
    print("Go to the swimming!")

elif not (temp < 0 or temp > 30):
    print("Get a coat!")
    print("You should wear gloves.")