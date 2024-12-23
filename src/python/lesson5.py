# age = int(input("please enter your age: "))

# if age < 18 or age > 0:
#     print("you'r not able to voting")
# elif age > 18 and age  < 80:
#     print("you are able to voting")
# else:
#     print("wrong value")

# name = None
# if name:
#     print("OK you can buy it")
# else:
#     name = input("pleas write your name")
#     if name != "":
#         print("OK you can buy it")

# print(name)


# for item in "siavash":
#     print(item)

# mylist = ["a","b","c","d", "e"]
# for item in mylist:
#     print(item)

# def intro (name, lastname, code):
#     print(f"name = {name} _ lastname = {lastname} _ code= {code}")

# intro(code="rahimi",lastname="siavash", name="hossini")
# for i in range(50, 60, 2):
#     print(i)
# for i in range(50, 60, 2):
#     print(i)


# for i in range(1, 100):
#     pass

# for i in range(1, 100):
#     if i %2 == 0:
#         continue
 
#     print(i)


# mydic = {"Ali":"active", "Hassan":"inactive", "sina":"active"}

# for key, value in mydic.copy().items():
#     if value == 'inactive':
#         del mydic[key]

# print(mydic)

# active_users = {}
# for key, value in mydic.items():
#     if value == "active":
#         active_users[key] = value

# print(active_users)


# prime number
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         print(n, "is a prime number")


# def die():
#     pass

# message = 401

# match message:
#     case 200:
#          print("ok")
#     case  400:
#         print("bad request")
#     case _:
#         print("bad message")


# enum 
# from enum import Enum
# class Color(Enum):
#     RED = 'red'
#     GREEN = 'green'
#     BLUE = 'blue'

# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

# match color:
#     case Color.RED:
#         print("I see red!")
#     case Color.GREEN:
#         print("Grass is green")
#     case Color.BLUE:
#         print("I'm feeling the blues :(")




# def fib(number):
#     """Print a Fibonacci series less than n."""
#     a, b = 0, 1
#     while a < number:
#         print(a, end=" ")
#         a,b = b, a+b
#     print()

# f = fib
# f(500)


# def student(name, code = 0, Class="ovom B", school="sabori"):
#     print(f"the student name is {name} and it's code is {code} and class is  {Class}")

# student("ALi", 846343)

# i = 5

# def f(arg=i):
#     print(arg)

# i = 6
# f(i)

def func(a, mylist=None):
    if mylist is None:
        mylist = []
    mylist.append(a)
    return mylist 

print(func(5))
print(func(8))
print(func(9))