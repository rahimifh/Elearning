answers = []

def printAns():
    for i in answers:
         print(i)
def calc(calinput):
    try:
        ans = eval(calinput)
        return ans
    except:
        return "oops there is an error!"


while True:
    calinput = input("=>  ")

    ans = calc(calinput)
    print(ans)
    answers.append(f"{calinput} = {ans}")
    command = input("Do you whant to print answers? Y/N/C: ")
    if command == "Y" or command == "y":
         printAns()
    elif command == "C" or command == "c":
        answers.clear()
    else:
        pass
   


    