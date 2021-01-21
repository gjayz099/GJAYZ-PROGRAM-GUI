#CALCULATOR BY:GJAYZ

from tkinter import *

Calculator = Tk()
Calculator.geometry()
Calculator.title("Calculator By:Gjayz")
Calculator.configure()

#VARLABLE
text_Input = StringVar()
operator = ""

#FRAME CALCULATOR
Calculator_Function = Frame(Calculator, bg="plum4", bd=6, relief=GROOVE)
Calculator_Function.pack(side=BOTTOM)

#FUNCTION
def btnClick(NumbersCal):
    global operator
    operator = operator + str(NumbersCal)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("0")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

#ENTRY
txtDisplay = Entry(Calculator_Function, width=25, bg="white", bd=4, font=("arial",20,"bold"), justify=RIGHT, textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

#CALCULATOR BUTTONS
b7=Button(Calculator_Function, padx=16, pady=1, bd=7, fg="snow", font=('arial', 12, 'bold'), width=3, text="7",bg="gray25",command=lambda:btnClick(7))
b7.grid(row=2,column=0)
b8=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="8",bg="gray25",command=lambda:btnClick(8))
b8.grid(row=2,column=1)
b9=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="9",bg="gray25",command=lambda:btnClick(9))
b9.grid(row=2,column=2)
bAdd=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="+",bg="gray25",command=lambda:btnClick('+'))
bAdd.grid(row=2,column=3)
#CALCULATOR BUTTONS
b4=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="4",bg="gray25",command=lambda:btnClick(4))
b4.grid(row=3,column=0)
b5=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="5",bg="gray25",command=lambda:btnClick(5))
b5.grid(row=3,column=1)
b6=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="6",bg="gray25",command=lambda:btnClick(6))
b6.grid(row=3,column=2)
bSub=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="-",bg="gray25",command=lambda:btnClick('-'))
bSub.grid(row=3,column=3)
#CALCULATOR BUTTONS
b1=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="1",bg="gray25",command=lambda:btnClick(1))
b1.grid(row=4,column=0)
b2=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="2",bg="gray25",command=lambda:btnClick(2))
b2.grid(row=4,column=1)
b3=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="3",bg="gray25",command=lambda:btnClick(3))
b3.grid(row=4,column=2)
bMulti=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="*",bg="gray25",command=lambda:btnClick('*'))
bMulti.grid(row=4,column=3)
#CALCULATOR BUTTONS
b0=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="0",bg="gray25",command=lambda:btnClick(0))
b0.grid(row=5,column=0)
bClear=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="C",bg="gray25",command=btnClear)
bClear.grid(row=5,column=1)
bEqual=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="=",bg="gray25",command=btnEquals)
bEqual.grid(row=5,column=2)
bDiv=Button(Calculator_Function,padx=16,pady=1,bd=7,fg="snow", font=('arial', 12, 'bold'), width=3, text="/",bg="gray25",command=lambda:btnClick('/'))
bDiv.grid(row=5,column=3)

#LOOPS
Calculator.mainloop()