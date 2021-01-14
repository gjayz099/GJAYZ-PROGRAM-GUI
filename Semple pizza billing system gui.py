#BASIC PIZZA BILLING SYSTEM ####by-GJAYZ####

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import random
import sys

rot = Tk()
rot.geometry()
rot.title("PIZZA BILLING SYSTEM")
rot.configure(background="Light Pink1")

# variables
variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
variable4 = IntVar()
variable5 = IntVar()
variable6 = IntVar()
variable7 = IntVar()
variable8 = IntVar()
variable9 = IntVar()
variable10 = IntVar()

Date_of_Order = StringVar()
Receipt_Ref = StringVar()
Total_FoodAndDrinks= StringVar()

Date_of_Order.set(time.strftime("%y/%m/%d"))

pepperoni = StringVar()
hawaiian = StringVar()
chicken_bbq = StringVar()
super_chees = StringVar()
cheese_bacon = StringVar()
coca_cola = StringVar()
pepsi = StringVar()
royal = StringVar()
sprite = StringVar()
sparkle = StringVar()

pepperoni.set("0")
hawaiian.set("0")
chicken_bbq.set("0")
super_chees.set("0")
cheese_bacon.set("0")
coca_cola.set("0")
pepsi.set("0")
royal.set("0")
sprite.set("0")
sparkle.set("0")


#Function QTY
def FoodsPepperoni():
    if variable1.get() == 1:
        textPepperoni.configure(state=NORMAL)
        textPepperoni.focus()
        textPepperoni.delete('0', END)
        pepperoni.set("")
    elif variable1.get() == 0:
        textPepperoni.configure(state=DISABLED)
        pepperoni.set("0")

def FoodsHawaiian():
    if variable2.get() == 1:
        textHawaiian.configure(state=NORMAL)
        textHawaiian.focus()
        textHawaiian.delete('0', END)
        hawaiian.set("")
    elif variable2.get() == 0:
        textHawaiian.configure(state=DISABLED)
        hawaiian.set("0")

def FoodsChicken_BBQ():
    if variable3.get() == 1:
        textChicken_BBQ.configure(state=NORMAL)
        textChicken_BBQ.focus()
        textChicken_BBQ.delete('0', END)
        chicken_bbq.set("")
    elif variable3.get() == 0:
        textChicken_BBQ.configure(state=DISABLED)
        chicken_bbq.set("0")

def FoodsSuper_Chees():
    if variable4.get() == 1:
        textSuper_Chees.configure(state=NORMAL)
        textSuper_Chees.focus()
        textSuper_Chees.delete('0', END)
        super_chees.set("")
    elif variable4.get() == 0:
        textSuper_Chees.configure(state=DISABLED)
        super_chees.set("0")

def FoodsCheese_Bacon():
    if variable5.get() == 1:
        textCheese_Bacon.configure(state=NORMAL)
        textCheese_Bacon.focus()
        textCheese_Bacon.delete('0', END)
        cheese_bacon.set("")
    elif variable5.get() == 0:
        textCheese_Bacon.configure(state=DISABLED)
        cheese_bacon.set("0")

def DrinksCoca_Cola():
    if variable6.get() == 1:
        textCoca_Cola.configure(state=NORMAL)
        textCoca_Cola.focus()
        textCoca_Cola.delete('0', END)
        coca_cola.set("")
    elif variable6.get() == 0:
        textCoca_Cola.configure(state=DISABLED)
        coca_cola.set("0")

def DrinksPepsi():
    if variable7.get() == 1:
        textPepsi.configure(state=NORMAL)
        textPepsi.focus()
        textPepsi.delete('0', END)
        pepsi.set("")
    elif variable7.get() == 0:
        textPepsi.configure(state=DISABLED)
        pepsi.set("0")

def DrinksRoyal():
    if variable8.get() == 1:
        textRoyal.configure(state=NORMAL)
        textRoyal.focus()
        textRoyal.delete('0', END)
        royal.set("")
    elif variable8.get() == 0:
        textRoyal.configure(state=DISABLED)
        royal.set("0")

def DrinksSprite():
    if variable9.get() == 1:
        textSprite.configure(state=NORMAL)
        textSprite.focus()
        textSprite.delete('0', END)
        sprite.set("")
    elif variable9.get() == 0:
        textSprite.configure(state=DISABLED)
        sprite.set("0")

def DrinksSparkle():
    if variable10.get() == 1:
        textSparkle.configure(state=NORMAL)
        textSparkle.focus()
        textSparkle.delete('0', END)
        sparkle.set("")
    elif variable10.get() == 0:
        textSparkle.configure(state=DISABLED)
        sparkle.set("0")


#RESET FUNCTION
def Reset():
    totaltext.delete("1.0", END)

    Total_FoodAndDrinks.set("")
    pepperoni.set("0")
    hawaiian.set("0")
    chicken_bbq.set("0")
    super_chees.set("0")
    cheese_bacon.set("0")
    coca_cola.set("0")
    pepsi.set("0")
    royal.set("0")
    sprite.set("0")
    sparkle.set("0")

    variable1.set(0)
    variable2.set(0)
    variable3.set(0)
    variable4.set(0)
    variable5.set(0)
    variable6.set(0)
    variable7.set(0)
    variable8 .set(0)
    variable9 .set(0)
    variable10 .set(0)

    textPepperoni.configure(state=DISABLED)
    textHawaiian.configure(state=DISABLED)
    textChicken_BBQ.configure(state=DISABLED)
    textSuper_Chees.configure(state=DISABLED)
    textCheese_Bacon.configure(state=DISABLED)
    textCoca_Cola.configure(state=DISABLED)
    textPepsi.configure(state=DISABLED)
    textRoyal.configure(state=DISABLED)
    textSprite.configure(state=DISABLED)
    textSparkle.configure(state=DISABLED)

def TotalCost():
    Unit1 = int(pepperoni.get())
    Unit2 = int(hawaiian.get())
    Unit3 = int(chicken_bbq.get())
    Unit4 = int(super_chees.get())
    Unit5 = int(cheese_bacon.get())
    Unit6 = int(coca_cola.get())
    Unit7 = int(pepsi.get())
    Unit8 = int(royal.get())
    Unit9 = int(sprite.get())
    Unit10 = int(sparkle.get())

    Prices_Drinks_and_Foods = (Unit1 * 170) + (Unit2 * 160) + (Unit3 * 160) + (Unit4 * 150) + (Unit5 * 170) + (Unit6 * 80) + (Unit7 * 70) + (Unit8 * 70) + (Unit9 * 70) + (Unit10 * 50)

    Foods_Drinks = "\u20B1" + str(Prices_Drinks_and_Foods)
    Total_FoodAndDrinks.set(Foods_Drinks)


#TOTAL COST FUNCTION
def Resebo():
    totaltext.delete("1.0", END)
    x = random.randint(199000, 500876)
    randomRef = str(x)
    Receipt_Ref.set("Bill" + randomRef)

    totaltext.insert(END,"Receipt Ref:\t"+Receipt_Ref.get()+"\nDATE:"+Date_of_Order.get()+"\n")
    totaltext.insert(END,"PIZZA\t\t              QTY\n")
    totaltext.insert(END,"PEPPERONI:\t\t\t"+pepperoni.get()+"\n")
    totaltext.insert(END,"HAWAIIAN:\t\t\t"+hawaiian.get()+"\n")
    totaltext.insert(END,"CHICKEN BBQ:\t\t\t"+chicken_bbq.get()+"\n")
    totaltext.insert(END,"SUPER CHEES:\t\t\t"+super_chees.get()+"\n")
    totaltext.insert(END,"CHEESE BACON:\t\t\t"+cheese_bacon.get()+"\n")
    totaltext.insert(END,"COCA COLA:\t\t\t"+coca_cola.get()+"\n")
    totaltext.insert(END,"PEPSI:\t\t\t"+pepsi.get()+"\n")
    totaltext.insert(END,"ROYAL:\t\t\t"+royal.get()+"\n")
    totaltext.insert(END,"SPRITE:\t\t\t"+sprite.get()+"\n")
    totaltext.insert(END,"SPARKLE:\t\t\t"+sparkle.get()+"\n\n")

    totaltext.insert(END,"TOTAL:\t\t\t      "+Total_FoodAndDrinks.get()+"\n")

#EXIT FUNCTION
def Exit():
    QExit = messagebox.askyesno("PIZZA ORDERING SYSTEM", "Do you what to exit the system")
    if QExit > 0:
        sys.exit()

#FRAME AND LABEL NAME
optop = Frame(rot, bg="blue4", bd=5, pady=5, relief=GROOVE)
optop.pack(side=TOP)
PizzaTitle = Label(optop, font=("arial", 30, "bold"), text="Pizza Billing System", bd=10, bg="white",fg="gray15", justify=CENTER)
PizzaTitle.grid(row=0)
opbot = Frame(rot, bg="blue4", bd=10, pady=10, relief=GROOVE)
opbot.pack(side=BOTTOM)

#FRAME AND LABEL MENU
FRAME1 = Frame(opbot, bg="pink", bd=3, pady=3, relief=GROOVE)
FRAME1.pack()
PizzaMenu = LabelFrame(FRAME1, font=("arial", 15, "bold"),text="PIZZA'S")
PizzaMenu.grid(row=0,column=1)
Pepperoni = Checkbutton(PizzaMenu, text="Pepperoni", variable=variable1, onvalue=1, offvalue=0, font=("arial", 10, "bold"),command=FoodsPepperoni)
Pepperoni.grid(row=0, sticky=W)
Hawaiian = Checkbutton(PizzaMenu, text="Hawaiian", variable=variable2, onvalue=1, offvalue=0, font=("arial", 10, "bold"),command=FoodsHawaiian)
Hawaiian.grid(row=1, sticky=W)
Chicken_BBQ = Checkbutton(PizzaMenu, text="Chicken BBQ", variable=variable3, onvalue=1, offvalue=0, font=("arial", 10, "bold"),command=FoodsChicken_BBQ)
Chicken_BBQ.grid(row=2, sticky=W)
Super_Chees = Checkbutton(PizzaMenu, text="Super Cheese", variable=variable4, onvalue=1, offvalue=0, font=("arial", 10, "bold"),command=FoodsSuper_Chees)
Super_Chees.grid(row=3, sticky=W)
Cheese_Bacon = Checkbutton(PizzaMenu, text="Cheese Bacon", variable=variable5, onvalue=1, offvalue=0, font=("arial", 10, "bold"),command=FoodsCheese_Bacon)
Cheese_Bacon.grid(row=4, sticky=W)

textPepperoni = Entry(PizzaMenu, font=('arial', 10, 'bold'), bd=5, width=5, justify=LEFT, state=DISABLED, textvariable=pepperoni)
textPepperoni.grid(row=0,column=2)
textHawaiian = Entry(PizzaMenu, font=('arial', 10, 'bold'), bd=5, width=5, justify=LEFT, state=DISABLED, textvariable=hawaiian)
textHawaiian.grid(row=1,column=2)
textChicken_BBQ = Entry(PizzaMenu, font=('arial', 10, 'bold'), bd=5, width=5, justify=LEFT, state=DISABLED, textvariable=chicken_bbq)
textChicken_BBQ.grid(row=2,column=2)
textSuper_Chees = Entry(PizzaMenu, font=('arial', 10, 'bold'), bd=5, width=5, justify=LEFT, state=DISABLED, textvariable=super_chees)
textSuper_Chees.grid(row=3,column=2)
textCheese_Bacon = Entry(PizzaMenu, font=('arial', 10, 'bold'), bd=5, width=5, justify=LEFT, state=DISABLED, textvariable=cheese_bacon)
textCheese_Bacon.grid(row=4,column=2)


PizzaDrinks = LabelFrame(FRAME1, font=("arial", 15, "bold"),text="DRINK'S")
PizzaDrinks.grid(row=0,column=2)
Coca_Cola = Checkbutton(PizzaDrinks, text="Coca-Cola", variable=variable6, onvalue=1, offvalue=0, font=("arial", 10, "bold"),command=DrinksCoca_Cola)
Coca_Cola.grid(row=0, sticky=W)
Pepsi = Checkbutton(PizzaDrinks, text="Pepsi", variable=variable7, onvalue=1, offvalue=0, font=("arial", 10, "bold"),command=DrinksPepsi)
Pepsi.grid(row=1, sticky=W)
Royal = Checkbutton(PizzaDrinks, text="Royal", variable=variable8, onvalue=1, offvalue=0, font=("arial", 10, "bold"),command=DrinksRoyal)
Royal.grid(row=2, sticky=W)
Sprite = Checkbutton(PizzaDrinks, text="Sprite", variable=variable9, onvalue=1, offvalue=0, font=("arial", 10, "bold"),command=DrinksSprite)
Sprite.grid(row=3, sticky=W)
Sparkle = Checkbutton(PizzaDrinks, text="Sparkle", variable=variable10, onvalue=1, offvalue=0, font=("arial", 10, "bold"),command=DrinksSparkle)
Sparkle.grid(row=4, sticky=W)

textCoca_Cola = Entry(PizzaDrinks, font=('arial', 10, 'bold'), bd=5, width=5, justify=LEFT, state=DISABLED, textvariable=coca_cola)
textCoca_Cola.grid(row=0,column=2)
textPepsi = Entry(PizzaDrinks, font=('arial', 10, 'bold'), bd=5, width=5, justify=LEFT, state=DISABLED, textvariable=pepsi)
textPepsi.grid(row=1,column=2)
textRoyal = Entry(PizzaDrinks, font=('arial', 10, 'bold'), bd=5, width=5, justify=LEFT, state=DISABLED, textvariable=royal)
textRoyal.grid(row=2,column=2)
textSprite = Entry(PizzaDrinks, font=('arial', 10, 'bold'), bd=5, width=5, justify=LEFT, state=DISABLED, textvariable=sprite)
textSprite.grid(row=3,column=2)
textSparkle = Entry(PizzaDrinks, font=('arial', 10, 'bold'), bd=5, width=5, justify=LEFT, state=DISABLED, textvariable=sparkle)
textSparkle.grid(row=4,column=2)


#LABEL BUTTON
FRAME2 = Frame(opbot, bg="pink", bd=3, pady=3, relief=GROOVE)
FRAME2.pack()
buttonTotal=Button(FRAME2,padx=16,pady=1,bd=7,fg="old lace",font=("arial",8,"bold"),width=4,text="Total",command=TotalCost,bg='black')
buttonTotal.grid(row=0,column=0)
buttonSubmit=Button(FRAME2,padx=16,pady=1,bd=7,fg="old lace",font=("arial",8,"bold"),width=4,text="Submit",command=Resebo,bg='black')
buttonSubmit.grid(row=0,column=1)
buttonReset=Button(FRAME2,padx=16,pady=1,bd=7,fg="old lace",font=("arial",8,"bold"),width=4,text="Reset",command=Reset ,bg='black')
buttonReset.grid(row=0,column=3)
buttonExit=Button(FRAME2,padx=16,pady=1,bd=7,fg="old lace",font=("arial",8,"bold"),width=4,text="Exit",command=Exit,bg='black')
buttonExit.grid(row=0,column=4)


FRAME3 = Frame(opbot, bg="pink", bd=3, pady=3, relief=GROOVE)
FRAME3.pack()
TotalDFrame = Frame(FRAME3, bg="pink", relief=GROOVE)
TotalDFrame.grid(row=0,column=0)
TotalDFrame1 = Frame(FRAME3, bg="pink", relief=GROOVE)
TotalDFrame1.grid(row=1,column=0)

#TOTAL COST
LblTotalofFood_and_Drinks=Label(TotalDFrame,font=('arial',10,'bold'),text='Total of Drinks',bg='sky blue',fg='black',justify=CENTER)
LblTotalofFood_and_Drinks.grid(row=0,column=0,sticky=W)
textTotalofFood_and_Drinks=Entry(TotalDFrame,bg='white',font=('arial',10,'bold'),insertwidth=2,justify=RIGHT,textvariable=Total_FoodAndDrinks)
textTotalofFood_and_Drinks.grid(row=0,column=1)

FRAME4 = Frame(opbot, bg="pink", bd=6, pady=6, relief=GROOVE)
FRAME4.pack()
totaltext = Text(FRAME4,width=35,height=10,font=("arial",11,"bold"))
totaltext.grid(row=0,column=0)
            

#LOOPS
rot.mainloop()
