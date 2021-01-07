#GJAYZ PROGRAM
#ACCOUNT SAVING

from tkinter import *
from tkinter import messagebox
import sys

win=Tk()
win.geometry()
win.title("SAVE USER AND PASS")
win.configure(background="dim gray")

#SAVE FUNCTION
def SAVE():
    SAVE_DATA = "YOUR DATA" + ".txt"
    with open(SAVE_DATA, "a") as fh:
        fh.write("ACCONT FOR: "+Eacnt.get()+"\n")
        fh.write("USERNAME: "+Euser.get()+"\n")
        fh.write("USERNAME: "+Epass.get()+"\n")
        fh.write("\n")
    Exit = messagebox.askyesno("SAVE...", "Do you what to exit the system")
    if Exit > 0:
        sys.exit()

#SUBMIT FUNCTION
def SUBMIT():
    subuser.configure(font=("normal",11),text="User: "+Euser.get())
    subpass.configure(font=("normal",11),text="Pass: "+Epass.get())


#EXIT FUNCTION
def Exit():
    qExit = messagebox.askyesno("PROGRAM", "Do you what to exit the system")
    if qExit > 0:
        sys.exit()


#LEFT FRAME
LF=Frame(win,width=450,height=200,bd=5,relief=GROOVE)
LF.pack(side=LEFT)
TPP=Frame(LF,width=450,height=200,bd=2,relief=GROOVE)
TPP.pack(side=TOP)
BTT=Frame(LF,width=450,height=60,bd=2,relief=GROOVE)
BTT.pack(side=BOTTOM)

#RIGHT FRAME
RF=Frame(win,width=250,height=200,bd=5,relief=GROOVE)
RF.pack(side=RIGHT)
TP=Frame(RF,width=250,height=70,bd=2,relief=GROOVE)
TP.pack(side=TOP)
BT=Frame(RF,width=250,height=60,bd=2,relief=GROOVE)
BT.pack(side=BOTTOM)

#USER AND PASS
user=Label(TPP,font=("arial",15),text="USERNAME",relief=SUNKEN,width=17)
user.grid(row=0,column=0)
pas=Label(TPP,font=("arial",15,),text="PASSWORD",relief=SUNKEN,width=17)
pas.grid(row=1,column=0)
Euser=Entry(TPP,width=30,font=("normal",12))
Euser.grid(row=0,column=1)
Epass=Entry(TPP,width=30,font=("normal",12))
Epass.grid(row=1,column=1)
Eacnt=Entry(TP,width=30,font=("normal",13))
Eacnt.pack()
subuser = Label(TP,width=30,font=("normal",13))
subuser.pack()
subpass = Label(TP,width=30,font=("normal",13))
subpass.pack()

#LABEL TEXT
pas=Label(BTT,font=("arial",10),text="REGISTERED PROGRAM SAVE TEXT FILE GUI",width=40)
pas.grid(row=0,column=1)
user=Label(BT,font=("arial",8),text="ACCOUNT",width=17)
user.grid(row=0,column=4)

#BOTTON
btnSub=Button(BTT,text="SUBMIT",font=("arial",10,"bold"),bg="azure",command=SUBMIT,relief=RAISED,width=8)
btnSub.grid(row=0,column=2)
btnExt=Button(BTT,text="EXIT",font=("arial",10,"bold"),bg="azure",command=Exit,relief=RAISED,width=8)
btnExt.grid(row=0,column=3)
btnSve=Button(BT,text="SAVE",font=("arial",10,"bold"),bg="azure",command=SAVE,relief=RAISED,width=8)
btnSve.grid(row=0,column=3)


win.mainloop()