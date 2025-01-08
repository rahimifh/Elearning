class person:
    live = True
    age = 0
    def __init__(self, name, height, weight, code):
        self.full_name = name
        self.height = height
        self.weight = weight
        self.code = code    
    def intro(self):
        print(f"I am {self.full_name}")
        
    def speak(self):
        print("I can speak")
        
    def getAge(self):
        self.age += 1
        self.height += 10
        self.weight += 5 
    def die(self):
        self.live = False

p1 = person("sara hamidi", height=30, weight=3, code="001859674")
# print(p1.age)
# print(p1.height)
# print(p1.weight)


class Teacher(person):
    def __init__(self, name, height, weight, code,age, edu = "Bacheor's degree"):
        self.education = edu
        self.level = "E"
        self.age = age
        super().__init__(name, height, weight, code)
    def Teach(self):
        print("I can teach")
        return 0
    def intro(self):
        super().getAge()
        print(f"I am {self.full_name} and I am a Teacher")
    def setLevel(self):
        score = self.age + (self.weight - 50)
        print(score)
        if score < 30:
            self.level = "E"
        elif score >=30 and score < 50:
            self.level = "C"
        elif score >= 50 and score < 60:
            self.level = "B"
        else:
            self.level = "A"


p2 = Teacher("Ali Ahmadi", 175, 73,"009687458",25, "Master's degree")
print(p2.age)
print(p2.Teach())
p2.intro()
p2.setLevel()
print(p2.level)