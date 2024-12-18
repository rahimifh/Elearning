myset = {"Ali", "Reza", "behroz", "negin", "Ali"}
# mylist = ["Ali", "Reza", "behroz", "negin", "Ali"]
myset2 = {"tahmine", "hasti", "reyhaneh"}
# print("Rezaa" in  myset)


myset.add("Reza")


myset.update(myset2)


# myset2.remove("hasti")

# myset2.discard("hastii")
# x = myset.pop()

myset.clear()
# print(myset)


# dic 

mydic = {
    "name": "سارا",
    "age": 15,
    "student": True,
    "friends":["zahra", "hasti", "reyhaneh"]
}

mydic2 = {
    "Hello": {
        "mean": "سلام",
        "des": "sdkfsdflsdf",
        "exam":"aoisjdoasiasiohd"
    }
}

# mydic3 = dict(name= "سارا",age= 15,student= True,friends=["zahra", "hasti", "reyhaneh"])

# x = mydic.keys()

mydic["books"] = ["book1", "book2"]
mydic.update({"year":"2025"})
mydic.update({"birthday":"2010-3-16"})
x = mydic.pop("birthday")
# print(x)
# print(mydic)

# for i in mydic:
#     print(mydic[i])

# for i in mydic.values():
#     print(i)

for i, j in mydic.items():
    print(f"{i} = {j}")