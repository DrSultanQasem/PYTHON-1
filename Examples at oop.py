print("========1=======")
class students():
    def __init__(self,name):
        self.name=name
        self.marks=[]            
        print(f"WELCOME {name} TO THE SCHOOL")
    def marks(self):
        return self.marks
    def addmark (self, *mark):
        for item in mark:
            self.marks.append(item)
            
    # @property
    def avg (self):
        return sum (self.marks) /len(self.marks)

std1=students("AHMED")
std1.addmark(19,20,17,14,19,20)
print(std1.marks)
print(std1.avg())

print("========2=======")
class animal1():
    def __init__(self,name):
        self.name=name.title()
        print(f"Animal's Name IS {self.name}")
    def eat (self,food):
        print(f"{self.name} eat {self.food}")
animal_1=animal1("dog")
print("-------")
class animal2(animal1):
    def __init__(self,name,food):
        self.food=food.title()
        super().__init__(name)
        print(f"{self.name} Is Your Animal And Eat {self.food}")
    
animal_2=animal2("cat","fish")
        
        