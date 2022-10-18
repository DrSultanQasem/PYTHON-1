from turtle import shapesize
from numpy import *
import numpy 



###create A matrix
# x=array([range(i,i+10) for i in range(1,11)])
# print(x)
# z=arange(36).reshape(4,3,3)
# print(z)


###create empty matrix
# x=empty((10,10))
# print(x)


###create a matrix with float numbers that it number between twoes numbers and dimintion of this matrix
# x=random.uniform(1,10,(10,10))
# print(x)

###create a Matrix and it items's value in it is between 0&1 all you need  put a dimintion in random.random(?)
# x=random.rand(10,10)
# print(x)
# z=random.random((10,10))
# print(z)

##create  a matrix with integer items
# x=random.randint(1,101,(10,10))
# z=reshape(x,(10,10))
# print(x)
# print(z)


###change sort
# x=random.randint(1,101,size=(10,10)) ## == x=random.randint(1,101,(10,10))
# print(x)
# y=x.tolist()
# random.shuffle(y)
# z=array(y)
# print(z)

# for x in y:
#     random.shuffle(x)
# print(y)

###create zeros or ones matrix 
# x=zeros(10)
# x1=zeros((10,10))
# x2=(zeros((3,10,10)))
# print("11111111",x,"\n2222222\n",x1,"\n33333333\n",x2)
# z=ones(10)
# z1=ones((10,10))
# z2=ones((3,10,10))
# print("11111111",z,"\n2222222\n",z1,"\n33333333\n",z2)

### create identity matrix 
# x=eye(10)
# print(x)

### Create Matrix with only 1 value 
# x=full((3,3), 10)
# print(x)


### Create A Matrix of ordered numbers
# x=linspace(0,100,20).reshape(4,5)
# print(x)
# ###ممكن بردو تستخدم التجزئة دى فى انك تجزء مصفوفه او داتا عندك

### Create Diagonal Matrix 
# x=diag([x for x in range(1,11)]) 
# print(x)

### another way 
# z=zeros((10,10))
# print(z)
# fill_diagonal(z,[x for x in range(1,11)])
# print(z)

### ask about number if none zero items in matrix
# x = random.randint(0, 10, (3, 3))
# print(x,'\n-----------')
# print(count_nonzero(x))#لو سبتها فاضيه هيحسب عدد الارقام ال مش صفر 
# print(count_nonzero(x<6))#انما لو حطيت شرط بيعد الارقام ال متنفذه الشرط عليها 
# # اما لو حطيط الاكسيس بيحسبلك الاعداد ال متنفذ عليها شرط او لو سيبتها فاضي بيحسبلك عدد ال مش اصفار لكن فى الصف الواحد يعنى كل صف على حدا 
# print(count_nonzero(x,axis=1))
# print(count_nonzero(x<6,axis=1))


### ask about condition in all matrix is in or not
# x=random.randint(0,10,(3,3))
# print(x,'\n------------')
# print(any(x<2))#بقوله هل فى عنصر اصغر من 2 ف المصفوفه ككل
# print(any(x<2,axis=1))

### ask if all elemnts is Condition ??
# x=arange(1,21).reshape(4,5)
# print(all(x<20))
#return True or False


### ask about condition 
# x=random.randint(5,20,size=12).reshape(3,4)
# print(x)
# print("_______________")
# print(x>6)
# print("_______________")
# print(x<6)
# print("_______________")
# print(x==6)
# print("_______________")

### Ask about Difference between Elemnts of two matreces

# x=arange(12).reshape(3,4)
# z=arange(12).reshape(3,4)
# a=2*z
# print(x,"\n-------------\n",a)
# print(isclose(x,z,rtol=0.1))
# print(isclose(x,a,rtol=0.1))

### Multiply Elements in matreces عنصر ف اخوة 
# x=arange(25).reshape(5,5)
# z=arange(25).reshape(5,5)
# a=multiply(x,z)
# b=x*z
# print(a)
# print(b)
##multiply elemnts in matrix in each other
# x =arange(9).reshape(3,3)
# z =arange(1,9)
# print(x)
# print(z)
# print(multiply.reduce(x))#columns
# print(multiply.reduce(z))
##multiply each elemnt in all elemnt in it row
# x=arange(9).reshape(3,3)
# print(x)
# print(multiply.outer(x,x))



### power of elemnts in matrices
# x =arange(5)
# print(x)
# print(power(x,2))
# print(x**2)
### Sum elemnts of matrices 
# x =arange(15)
# print(add.reduce(x))
# print(sum(x))


### poly nomial ###
import numpy as np


# Polynomial = np.polynomial.Polynomial
# X= np.array([0,20,40,60,80,100,120,140,160,180])
# Y= np.array([10,9,8,7,6,5,4,3,2,1])

# points,stats = Polynomial.fit(X,Y,1,full=True)

# print(points)



# a = poly1d((-7))
# b = poly1d((-7,2))
# c = poly1d((-7,2,1))
# print(a,"\t",a(1))
# print(b,"\t",b(1))
# print(c,"\t",c(1))
#-----------------)
# b=polyval((-7,2),1)
# c=polyval((-7,2,1),1)

# print(b)
# print(c)


###drivediv
# a=poly1d((-7,2,1))
# b=polyder(a)
# c=b(3)
# print(a,"\n-----1-----",b,"\n",c)



#####----------
# a=poly1d((-7,2,1))
# b=polyder(a)
# print(a,"\n-----2-----",b)
# ### integrition
# a=polyint(b)
# print("Integration : ",a)


###dates
# x = datetime64('2015-07-04')
# y = x + range(50)
# print(x,"\n-----------",y) 





















# x=[]
# for i in range(10):
#     x.append([])
#     for o in range(10):
#         if i!=o:
#             x[i].append(0)
#         else:
#             x[i].append(o+1)
# print(array(x))




























# d=0
# v=1
# c=0
# a=arange(100).reshape(10,10)
# print(a)
# b=a.tolist()
# print(b)
# while True:    
#     for x in b:
#         for i in x:
#             #print(i)
#             if x.index(i) == d:
#                 x[d] = v
#             elif c == 11:
#                 break
#             else:
#                 pass
                
#             d+=1
#             v+=1
#             c+=1

# print(b)                    


