from tkinter import *
from tkinter import messagebox
from mysql import connector
from mysql.connector import Error

def database():
    conn = connector.connect(
        user='root',

        password='root',

        host='127.0.0.1',

        port='3307',

        database='demo')
    mycursor = conn.cursor()
    mycursor.execute("insert into college values(%d,%s,%s,%s,%s,%s)",

                     (w1.get(),w2.get(),var.get(),w4.get(),w5.get(),w6.get()))
    messagebox.showinfo("Info","Submitted")
    conn.commit()


root=Tk()


Label (root, text = "Registration Form", bg="black", fg="white",font="Verdana 16 bold italic").grid(row=0, columnspan=5)

lab1= Label( root, text= "Sr_No", height=2, width=15,fg='black',font="BOLD")
lab1.grid(row=1,column=1,sticky=W)
w1=Entry(root)
w1.grid(row=1,column=2)

lab2= Label( root, text= "Name", height=2, width=15,fg='black',font="BOLD")
lab2.grid(row=2,column=1,sticky=W)
w2=Entry(root)
w2.grid(row=2,column=2)


lab3= Label( root, text= "Gender", height=2, width=15,fg='black',font="BOLD")
lab3.grid(row=3,column=1,sticky=W)

var=StringVar()
w3=Radiobutton(root, text= "Male",variable=var, value=1)
w3.grid(row=3,column=2,sticky=N)
w3=Radiobutton(root, text= "Female",variable=var, value=2)
w3.grid(row=3,column=3,sticky=N)


lab4= Label( root, text= "Address", height=2, width=15,fg='black',font="BOLD")
lab4.grid(row=4,column=1,sticky=W)
w4=Text( root, bd=2,height=5,width=15,relief=RAISED )
w4.grid(row=4,column=2)

lab5= Label( root, text= "Roll_No", height=2, width=15,fg='black',font="BOLD")
lab5.grid(row=5,column=1,sticky=W)
w5=Entry(root)
w5.grid(row=5,column=2)


lab6= Label( root, text= "Branch", height=2, width=15,fg='black',font="BOLD")
lab6.grid(row=6,column=1,sticky=W)
w6=Entry(root)
w6.grid(row=6,column=2)


B=Button(root,text="SUBMIT", height=1, width=15, command=database, bg="black", fg="White",font="Verdana 16 bold")
B.grid(row=12,columnspan=3)
