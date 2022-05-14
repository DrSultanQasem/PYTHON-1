### if condition ###
#ال if بتستخدمها لو عندك شروط لتنفيذ اوامر معينه 
#صيغتها كالتالى if + condition: order
#ولها كذا شكل تانى ها نشوف ف التمارين
x=[1,2,3,4,5]
if 5 in x :print("OUTPUT IS : IN")#هنا بقوله لو رقم 5 موجود ف الليسته اطبع ان 
print("--------------")
if 6 in x :print("OUTPUT IS : IN")# الشرط رقم 1
else:print("OUTPUT IS : OUT")# هنا بقوله لو ملقتش '6' ف الشرط رقم 1 اطبع اوت
#+++++++++++++++
print("------------")
#حالة if المركبه بتتكون من عدة شروط
if 9 >=10  :print("OUTPUT IS : IN")
elif 9>=11 :print("OUTPUT IS : IN1")
elif 9>=12 :print("OUTPUT IS : IN2")
elif 9>=13 :print("OUTPUT IS : IN3")
else:print("OUTPUT IS : NO ANSWER") 


for i in range(10001):
    i=input("ENTER NUMBER ' 0 ' IF YOU WANT QUIT OR PREES ENTER :  ")
    
    if i== "0" or i == "": break 
    
