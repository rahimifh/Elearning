
while True:
    age = int(input("How old are you: "))
    if age < 10 and age > 0: 
        print("you are child!") 

    elif age >= 10 and age < 30:
        print("You are young!")
    elif age >= 30:
        print("you are old")
    else:
        print("invalid age")

