name = "nastaran"
def parent():
    def local():
        name = "Hasti"
        
    def Nonelocal():
        nonlocal name
        name = "Reza"
        print(name)
    def Global():
        global name
        name = "Ahmad"
    name = "Zahra"
    local()
    # print(name)
    Nonelocal()
    # print(name)
    Global()

parent()
# print(name)

# class myclass:
#     code = 32 
#     command = "aljsdan nansd"
#     def intro(self):
#         print("hello world!")

# n = myclass()
# n.intro()

# class person:
#     live = True
#     age = 0
#     def __init__(self, name, height, weight):
#         self.fullName = name
#         self.height = height
#         self.weight = weight
#     def addHeight(self):
#         if self.age <= 20:
#             self.height += 10

#     def addAge(self):
#         self.age += 1
#         self.addHeight()

# p1 = person("Ali Rahmani", 60, 3)

# print(p1.age)
# print(p1.live)
# print(p1.fullName)
# print(p1.height)
# print(p1.weight)
# p1.addAge()
# p1.addAge()
# p1.addAge()
# p1.addAge()
# p1.addAge()
# p1.addAge()
# p1.addAge()
# p1.addAge()
# p1.addAge()
# print(p1.age)

