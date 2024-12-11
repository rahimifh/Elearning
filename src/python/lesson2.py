# ***************** Lists *****************

objects = [1, "ali", True, [4,5], 5.5]

# print(objects)
# print(objects[-1])
# print(objects[1])
# print(objects[1:3])
objects[2] = 15.5


objects.append("sara")
objects.append(17 % 4)


# print(len(objects))

matrix = [[4,5,6],[7,8,9]]

# print(matrix[1][1])

#  ************************* input and output ******************************

# name = input("please enter a number: ")

# print(name)


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