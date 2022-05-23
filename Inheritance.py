###super,Parent,Base_class
class persons:
    def __init__ (self):
        print("%%Person Initialized%%")
        self.fname=""
        self.lname=""
    def GetFullNmae(self):
        return self.fname+" "+self.lname
###sup,chiled,derived_class
class Teatcher(persons) :
    def __init__ (self):
        print("%%Teatcher Initialized%%")
        self.salary=""
    #دى نفس ال فى الاب لكن اتعملها اوفر رايدينج ف بالتالى هينفذ دى داخل كلاس التيتشرز ولن يلتفت الى الموجوده فى كلاس الاب
    def GetFullNmae(self):
        return "NO NAME"
    def Degree(self):
        return "DR"
###another  sup,child,derived_class
class student(persons):
    def __init__ (self):
        print("%%Student Initialized%%")
        self.year=1
    def study_year(self):
        return "first year"
#client_Code
p=persons()
print("Before Edit :",p.GetFullNmae())
p.fname="Samer"
p.lname="Atwan"
print("After Edit  :",p.GetFullNmae())
################################################
t=Teatcher()
print("Degree is   :",t.Degree())
#here because we put name of parent class in paranthess of child class 
#we can use all methods that there are in parent class 

#HERE OVER_RIDING
print("Before Edit :",t.GetFullNmae())
t.fname="SAM"
t.lname="ATW"
print("After Edit  :",t.GetFullNmae())
#################################################
s=student()
print("study year  :",s.study_year())

#دى ما ينفعش ترن لان الكونستراكتور بتاع الاب مش بيشتغل علشان انت عامل هنا كونستراكتور ف بيرن الكونستراكتور بتاع الابن بس 
#print("Before Edit :",s.GetFullNmae())
s.fname="samy"
s.lname="atwa"
print("After Edit  :",s.GetFullNmae())

### Multiple Inheritance ###

class class1():#grand pa
    def fun1(self):
        print("class1 fun1")
class class2(class1):#pa
    def fun2(self):
        print("class2 fun2")
class class3(class2):#child
    def fun3(self):
        print("class3 fun3")
print("class 1")
c1=class1()
c1.fun1()
print("class 2")
c2=class2()
c2.fun1()
c2.fun2()
print("class 3")
c3=class3()
c3.fun1()
c3.fun2()
c3.fun3()





