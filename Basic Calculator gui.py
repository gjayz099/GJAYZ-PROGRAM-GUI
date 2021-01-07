#BASIC CALCULATOR GUI

from tkinter import *
from tkinter import messagebox
import sys

cal = Tk()
cal.geometry()
cal.title("CALCULATOR")
cal.configure(background="light blue")

def evaluate(event):
    result.configure(font=("arial",10,"bold"),text = "RESULT: " + str(eval(entry.get())))

def Exit():
    qExit = messagebox.askyesno("PROGRAM CALCULATOR", "Do you what to exit the system")
    if qExit > 0:
        sys.exit()

Top=Frame(cal,width=200,height=70,bd=3,relief=GROOVE)
Top.pack(side=TOP)
Bottom=Frame(cal,width=300,height=30,bd=3,relief=GROOVE)
Bottom.pack(side=BOTTOM)

put = Label(Top, text="CALCULATOR")
put.config()
put.pack()
result = Label(Top,width=15)
result.pack(side=LEFT)
entry = Entry(Top,width=20,bd=5,font=("normal",13))
entry.pack(side=RIGHT)
entry.bind("<Return>", evaluate)

btnExt=Button(Bottom,text="EXIT",font=("arial",10,"bold"),bg="dim gray",command=Exit,relief=RAISED,width=8)
btnExt.grid(row=0,column=0)

cal.mainloop()