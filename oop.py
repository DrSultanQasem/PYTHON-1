###constractor###
class welcome:
    def __init__(self, name):
        self.name = name
        print("WELCOME {}".format(name))
# دى حاجه كده اساسيه بتشتغل بمجرد استدعاء object باسم ال class
# تقدر تخزن فيها methods و attributes  عادى


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

c = circle()

print(c.get_pi())
print(c.get_name())
print(c.set_area())    #return None
print(c.get_area())
print(c.set_primeter())#return None
print(c.get_primeter())

###Inheritance###
#هنا بنورث كل حاجه ف اى class عندك لاى class جديد بمجرد ما تكتب اسم ال class ال عندك فى اقواس ال class الجديد وبس
print("""##Inheritance##""")
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









