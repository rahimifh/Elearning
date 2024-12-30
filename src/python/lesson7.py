ansList = []
def calc(newinput):
    try:
        ans = eval(newinput)
        return ans
    except:
         return "somthings went wrong!!"
def commandHandeler(command):
        if command == "Y" or command == "y":
            for i in ansList:
                print(i)
        elif command == "C" or command == "c":
            ansList.clear()
        else:
            pass 
while True:
    newinput = input("=> ")

    ans = calc(newinput)
    ex = f"{newinput} = {ans}"
    print(ex)
    ansList.append(ex)
    command = input("write your command (Y/C/N): ")
    commandHandeler(command)
  






# ansList = []
# def calc(num1, op, num2):
#     match op:
#         case "+":
#             return num1 + num2
#         case "-":
#             return num1 - num2
#         case "*":
#             return num1 * num2
#         case "/":
#             return num1 / num2
# def commandHandeler(command):
#         if command == "Y" or command == "y":
#             for i in ansList:
#                 print(i)
#         elif command == "C" or command == "c":
#             ansList.clear()
#         else:
#             pass 
# while True:
#     num1 = int(input("First number: "))
#     op = input("operator: ")
#     num2 = int(input("second number: "))
#     ans = calc(num1, op, num2)
#     ex = f"{num1} {op} {num2} = {ans}"
#     print(ex)
#     ansList.append(ex)
#     command = input("write your command (Y/C/N): ")
#     commandHandeler(command)
  