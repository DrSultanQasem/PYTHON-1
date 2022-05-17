###constractor###
class welcome:
    def __init__(self, name):
        self.name = name
        print("WELCOME {}".format(name))
# دى حاجه كده اساسيه بتشتغل بمجرد استدعاء object باسم ال class
# تقدر تخزن فيها methods و attributes  عادى
# Any Attributes here called instance attribute


# لو حطيط دى __ قبل ال Attribute بيبقى private
# اما دى _ بيبقى protected


class circle():
    ##constractor##

    def __init__(self):
        self.__pi = 22/7       # private
        self._name = "Circle"  # protected
        
     
# ال set بقا هى method بتعمل set ل attribute معين
##SETTER##

    def set_area(self, radius=1):
        self.radius = radius
        self.area= ( self.__pi * self.radius**2 )
    def set_primeter(self, radius=1):
        self.radius = radius
        self.primeter = ( self.__pi * self.radius )


    # بتستخد get علشان تستدعى attribute ودى بتستخدمها لما تعوز تستخد attribute بس هو privatet او protected
##GETTER##

    def get_pi(self):
        return self.__pi

    def get_name(self):
        return self._name

    def get_area(self):
        return self.area
    def get_primeter(self):
        return self.primeter
### %% client code %% ###
c = circle()

print("PI IS :",c.get_pi())
print("Name IS :",c.get_name())
print("=====>",c.set_area(4))    #return None because it use to set radius
print("Area Is :",c.get_area())
print("=====>",c.set_primeter(2))#return None because it use to set radius
print("Primeter IS  :",c.get_primeter())
print("******%%%%*****")
### Puplic & Protected & Private ###
class A:
    def __init__(self,x1,x2,x3):
        self.x1=x1
        self._x2=x2
        self.__x3=x3
    def printx(self):
        print("Puplic x1 :",self.x1)
        print("Protected x2 :",self._x2)
        print("Private x3 :",self.__x3)
class B(A):
    def testx(self):
        print("Puplic x1 :",self.x1)
        print("Protected x2 :",self._x2)
#        print("x3 :",self.__x3)
#it will raise error if you run this line 
#because x3 is private (only run in own calss)
### %% client code %% ###
a=A(1,2,3)
a.printx()
print("******===*****")
b=B(4,5,6)
b.testx()




""" ###Inheritance###
#هنا بنورث كل حاجه ف اى class عندك لاى class جديد بمجرد ما تكتب اسم ال class ال عندك فى اقواس ال class الجديد وبس
print(""#Inheritance##"")
class circle2(circle):
    pass

c2=circle2()


print(c2.get_pi())
print(c2.get_name())
c2.set_area(2)
print(c2.radius)    #return None
print(c2.get_area())
print(c2.set_primeter())#return None
print(c2.primeter)
 """


