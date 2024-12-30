# def test(name, last_name = None):
#     if last_name:
#         return f"my name is {name} and my last name is {last_name}"
#     else:
#         return f"my name is {name}"
# x = test("Ali", "Ahmadi")

# def example(name, *args, **kwargs):
#     """
#         this function return  name of student
#     """
#     print(name)
#     print(kwargs)
#     for i in args:
#         print(i)

# example("zahra", "hossin", "Ali","siavash", Class="102")
# print(example.__doc__)

# ************stack *************
# stack = []

# def addtoStack(obj):
#     stack.append(obj)

# def getitem():
#     return stack.pop()

# for i in range(10):
#     addtoStack(i)
#     print(stack)

# for i in range(10):
#     x = getitem()
#     print(x)


# *************Queues**************
# from collections import deque
# queue = deque(["Ali", "Reza", "behroz", "negin", "Ali"])

# queue.append("Arash")
# print(queue.popleft())
# print(queue.popleft())
# print(queue.popleft())
# print(queue.popleft())
# print(queue.popleft())
# print(queue.popleft())
# print(queue)


def intro(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)


intro("sara", "naseri", "Ali", "Hossin", Test="hjbasdjfb", test2=5558)
