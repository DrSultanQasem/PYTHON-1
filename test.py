from cProfile import label
from  tkinter import * 
#creat the main app
test = Tk()
#change title
test.title("Test APP")
#set dimension
test.geometry("640x480")
#write test label
the_text=Label(test,text="WELCOME",height=2,font=("Arial",20))
the_text.pack()#put text into main window






#run infintly
test.mainloop()   