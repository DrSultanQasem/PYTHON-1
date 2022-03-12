### STATISTICS * LIBRARY ###
print("""
import statistics as st

list1=[9,4,3,3,9,1,5,2,9]
list2=[4,5,1,5,3,2,5,1,6,8]
list3=[1.5,6.4,3.3,2.3,7.2]#
print("THE MEAN IS   : ",st.mean(list1))
#دى بتستخدمها علشان تحسب الوسط الحسابى العادى .
print("THE FLOAT MEAN IS :",st.fmean(list3))
#دى بردو بتحسب الوسط الحسابى لكن اسرع من العاديه لما تكون الداتا عباره عن ارقام float .
print("---------------------------------")""")

###############################
import statistics as st

list1=[9,4,3,3,9,1,5,2,9]
list2=[4,5,1,5,3,2,5,1,6,8]
list3=[1.5,6.4,3.3,2.3,7.2]
list4=[1,1,1,2,2,2,3,3,3,4,4,4,5,6,7,8,9]
print("THE MEAN IS   : ",st.mean(list1))
#دى بتستخدمها علشان تحسب الوسط الحسابى العادى .
print("THE FLOAT MEAN IS :",st.fmean(list3))
#دى بردو بتحسب الوسط الحسابى لكن اسرع من العاديه لما تكون الداتا عباره عن ارقام float .
print("---------------------------------")
################################
print("""print("THE MEDIAN IS : ",st.median(list1)," AND : ",st.median(list2))
#دى بتجيب الوسيط
print("THE HIGH VALUE IS : ",st.median_high(list2))
#دى لما بيكون عدد القيم زوجى الطبيعى اجمع الرقمين واقسم على 2 لكن هنا لا هنا بيجيب القيمه الاكبر فى القيمتين ال ف الوسط
print("THE LOW VALUE IS : ",st.median_low(list2))
#ودى عكس ال high دى بتجيب القيمه الاقل ف الاتنين ال ف الوسط .
print("---------------------------------")
""")
################################
print("THE MEDIAN IS : ",st.median(list1)," AND : ",st.median(list2))
#دى بتجيب الوسيط
print("THE HIGH VALUE IS : ",st.median_high(list2))
#دى لما بيكون عدد القيم زوجى الطبيعى اجمع الرقمين واقسم على 2 لكن هنا لا هنا بيجيب القيمه الاكبر فى القيمتين ال ف الوسط
print("THE LOW VALUE IS : ",st.median_low(list2))
#ودى عكس ال high دى بتجيب القيمه الاقل ف الاتنين ال ف الوسط .
print("---------------------------------")
################################
print("""print("THE MODE IS   : ",st.mode(list1)," AND : ",st.mode(list2))
#دى بتجيب المنوال .
print("the mode is :",st.mode(list4))
#شوف دى جابت ال 1 اكانه المود الوحيد انما ال تحت جابت 1 2 3 4 
print("THE MULTIMODE IS : ",st.multimode(list4))
#دى بتجيب المود عادى لكن ميزيتها ان لو فى اكثر من مود بتجيبهم مش بتديك ايرور زى المود العاديه 
print("---------------------------------")
print("THE STANDARD DEVIATION IS : ",st.stdev(list1)," AND : ",st.stdev(list2))
#دى بتجيب الانحراف المعيارى .
print("---------------------------------")
print("THE VARIANCE IS : ",st.variance(list1)," AND : ",st.variance(list2))
#اما دى بتجيب التشتت .
""")
################################
print("THE MODE IS   : ",st.mode(list1)," AND : ",st.mode(list2))
#دى بتجيب المنوال .
print("the mode is :",st.mode(list4))
#شوف دى جابت ال 1 اكانه المود الوحيد انما ال تحت جابت 1 2 3 4 
print("THE MULTIMODE IS : ",st.multimode(list4))
#دى بتجيب المود عادى لكن ميزيتها ان لو فى اكثر من مود بتجيبهم مش بتديك ايرور زى المود العاديه 
print("---------------------------------")
print("THE STANDARD DEVIATION IS : ",st.stdev(list1)," AND : ",st.stdev(list2))
#دى بتجيب الانحراف المعيارى .
print("---------------------------------")
print("THE VARIANCE IS : ",st.variance(list1)," AND : ",st.variance(list2))
#اما دى بتجيب التشتت .

for i in range(11):
    x=int(input("ENTER NUMBER '0' IF YOU WANT QUIT OR PREES ENTER : "))
    if x==0:
        break
"""
print("----------------")

b=st.harmonic_mean(list1)
a=st.geometric_mean(list1)
print(a,b)
"""
