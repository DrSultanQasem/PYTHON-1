print("""### FOR LooP ###
#لها عدة استخدامات والاكثر استعمالا عندما يتعلق الامر بالتكرارات والاسرع . 
##FOR LOOP WITh LIST##
x=[1,2,3,4]
for i in x:print(i)
# هنا بقوله لكل عنصر  ف الليسته اطبع لى العنصر ف بيطبع كل عنصر فى سطر . 
print("--------")
for i in x:
     if i==3:break
     print(i)
#هنا قولتله الما توصل للعنصر 3 ما تجيبوش واخرج من اللوب .
print("--------")
for i in x:
    if i==3:continue
    print(i)
#هنا بقوله لما تلاقى الرقم 3 سيبه و كمل اللوب للاخر . 
#=====================================

""")
################################
### FOR LooP ###
#لها عدة استخدامات والاكثر استعمالا عندما يتعلق الامر بالتكرارات والاسرع . 
##FOR LOOP WITh LIST##
x=[1,2,3,4]
for i in x:print(i)
# هنا بقوله لكل عنصر  ف الليسته اطبع لى العنصر ف بيطبع كل عنصر فى سطر . 
print("--------")
for i in x:
     if i==3:break
     print(i)
#هنا قولتله الما توصل للعنصر 3 ما تجيبوش واخرج من اللوب .
print("--------")
for i in x:
    if i==3:continue
    print(i)
#هنا بقوله لما تلاقى الرقم 3 سيبه و كمل اللوب للاخر . 
#=====================================
##################################
print("""##FOR LOOP WITh DICTIONARY##
print("###########################")

y={1:"a",2:"b",3:"c",4:"d"}
for l in y.keys() :print(l)#هنا جبت قيم المفاتيح بس
print("====")
for l in y.values() :print(l)# هنا جبت قيم القيم بس 
print("====")
for h,u in y.items() :print(h,u)#هنا جبت المفاتيح وقيمها 
""")
###################################
##FOR LOOP WITh DICTIONARY##
print("###########################")

y={1:"a",2:"b",3:"c",4:"d"}
for l in y.keys() :print(l)#هنا جبت قيم المفاتيح بس
print("====")
for l in y.values() :print(l)# هنا جبت قيم القيم بس 
print("====")
for h,u in y.items() :print(h,u)#هنا جبت المفاتيح وقيمها 

###################################
print("""#=====================================
### WHILE LOOP ###
# دى بقا بقوله طول ما الشرط متحقق اعمل الاوامر ال جوه ال while  
q=int(input("Enter number : "))
while True:
     if q<=1:    
         print("number is lesser than or equal 1 ")
     else:print("number is bigger than 1 ")
     break
""")
#####################################
#=====================================
### WHILE LOOP ###
# دى بقا بقوله طول ما الشرط متحقق اعمل الاوامر ال جوه ال while  
q=int(input("Enter number : "))
while True:
     if q<=1:    
         print("number is lesser than or equal 1 ")
     else:print("number is bigger than 1 ")
     break
for e in range(11111):
    e=int(input("ENTER NUMBER ' 0 ' IF YOU WANT QUIT OR PREES ENTER : "))
    if e==0:
        break
    
    