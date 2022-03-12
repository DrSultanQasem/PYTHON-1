
print("""### if condition ###
#ال if بتستخدمها لو عندك شروط لتنفيذ اوامر معينه 
#صيغتها كالتالى if + condition: order
#ولها كذا شكل تانى ها نشوف ف التمارين
x=[1,2,3,4,5]
if 5 in x :print("IN")#هنا بقوله لو رقم 5 موجود ف الليسته اطبع ان 
""")
### if condition ###
#ال if بتستخدمها لو عندك شروط لتنفيذ اوامر معينه 
#صيغتها كالتالى if + condition: order
#ولها كذا شكل تانى ها نشوف ف التمارين
x=[1,2,3,4,5]
if 5 in x :print("OUTPUT IS : IN")#هنا بقوله لو رقم 5 موجود ف الليسته اطبع ان 

print("""#+++++++++++++++=
if 6 in x :print("IN")
else:print("OUT")# هنا بقوله لو ملقتش 6 ف الشرط ال فوق ده اطبع اوت
""")
#+++++++++++++++=
if 6 in x :print("OUTPUT IS : IN")
else:print("OUTPUT IS : OUT")# هنا بقوله لو ملقتش 6 ف الشرط ال فوق ده اطبع اوت

print("""#+++++++++++++++=
if 9 >=10  :print("IN")
elif 9>=11 :print("IN1")
elif 9>=12 :print("IN2")#لو جربت تحط ف الشرط ده بدل 12 9 ها يخرجلك الامر ان 2 
elif 9>=13 :print("IN3")
else:print("NO ANSWER")#هنا بما ان كل الشروط ال فوق مش متحققه ها يطلعلك نو انسر 
""")
#+++++++++++++++=
if 9 >=10  :print("OUTPUT IS : IN")
elif 9>=11 :print("OUTPUT IS : IN1")
elif 9>=12 :print("OUTPUT IS : IN2")#لو جربت تحط ف الشرط ده بدل 12 9 ها يخرجلك الامر ان 2 
elif 9>=13 :print("OUTPUT IS : IN3")
else:print("OUTPUT IS : NO ANSWER")#هنا بما ان كل الشروط ال فوق مش متحققه ها يطلعلك نو انسر 


for i in range(10001):
    i=int(input("ENTER NUMBER ' 0 ' IF YOU WANT QUIT OR PREES ENTER :  "))
    if i== 0:break
    