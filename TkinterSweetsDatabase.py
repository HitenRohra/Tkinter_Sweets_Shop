import tkinter as tk
import mysql.connector
from functools import partial


def validateLogin():
    passwordinfo = lsPassword.get()
    usernameinfo = lsUname.get()
    if usernameinfo=="admin" and passwordinfo=="admin":
        print("Welcome!!")
        btnADD['state'] = tk.NORMAL
        displaybutton['state'] = tk.NORMAL
        closebutton['state'] = tk.NORMAL
        root.destroy()
    else:
        tk.Label(root,text="").grid(row=8,column=3)
        tk.Label(root,text="Invalid Login",bg="Red", font=("Calibri",12),fg="black",width=15).grid(row=9,column=2,columnspan=2)
        print("Invalid Login")

def LoginPage():
    global txtUname
    global txtPass
    global lsUname
    global lsPassword
    global root

    root=tk.Toplevel(mw)


    root.geometry("380x230")
    root.title("Login")
    lsUname =tk.StringVar()
    lsPassword=tk.StringVar()

    tk.Label(root,text="Login",bg="SteelBlue",font=("Calibri",16), fg="white",width=35 ).grid(row=0,column=0,columnspan=6)
    tk.Label(root,text="").grid(row=1,column=0)

    tk.Label(root,text="User Name",bg="FloralWhite", font=("Calibri",12),fg="black",width=15).grid(row=3,column=0,columnspan=3,sticky="W")
    txtUname = tk.Entry(root,textvariable=lsUname).grid(row=3,column=3,sticky="W",columnspan=2)
    tk.Label(root,text="").grid(row=4,column=0)

    tk.Label(root,text="Password",bg="FloralWhite", font=("Calibri",12),fg="black",width=15).grid(row=5,column=0,columnspan=3,sticky="W")
    txtPass = tk.Entry(root,textvariable=lsPassword,show="*").grid(row=5,column=3,sticky="W",columnspan=2)
    tk.Label(root,text="").grid(row=6,column=0)

    tk.Button(root,text="Login",command=validateLogin).grid(row=7,column=3,columnspan=2)

    root.mainloop()

def addsql():
    mydb = mysql.connector.connect(host="localhost", user="root", password="admin", database="hiten")
    mycursor = mydb.cursor()
    name=iname.get()
    price=iprice.get()
    sql = "INSERT INTO Sweets (sweet, price) VALUES ('{0}',{1})".format(name,price)
    print(sql)
    mycursor.execute(sql)
    tk.Label(addw,text="").grid(row=8,column=3)
    tk.Label(addw,text="Added to database!!",bg="Coral", font=("Calibri",12),fg="black",width=15).grid(row=9,column=2,columnspan=3,sticky="w")
    mydb.commit()

def AddFunc():
    global iname
    global addw
    global iprice
    global txtiname
    global txtiprice

    addw=tk.Toplevel(mw)
    addw.title('Add Items')
    addw.geometry("420x250")
    iprice = tk.StringVar()
    iname = tk.StringVar()

    tk.Label(addw, text="Add Sweets", bg="SteelBlue", font=("Calibri", 16), fg="white", width=40).grid(row=0, column=0, columnspan=6)
    tk.Label(addw, text="").grid(row=1, column=0)
    tk.Label(addw, text="Item Name", bg="FloralWhite", font=("Calibri", 12), fg="black", width=15).grid(row=3, column=0, columnspan=3,sticky="W")
    tk.Entry(addw, textvariable=iname).grid(row=3, column=3, sticky="W", columnspan=2)
    tk.Label(addw, text="").grid(row=4, column=0)
    tk.Label(addw, text="Item Price", bg="FloralWhite", font=("Calibri", 12), fg="black", width=15).grid(row=5, column=0,columnspan=3, sticky="W")
    tk.Entry(addw, textvariable=iprice).grid(row=5, column=3, sticky="W", columnspan=2)
    tk.Label(addw, text="").grid(row=6, column=0)
    tk.Button(addw, text="ADD ITEM", command=addsql).grid(row=7, column=2, columnspan=4)
    addw.mainloop()

def DisplayFunc():
    global dp
    global n

    dp=tk.Toplevel(mw)
    dp.title("Display Items")
    dp.geometry("380x600")
    tk.Label(dp,text="S. No.",width=5,pady=10,bg="SteelBlue", font=("Calibri", 16), fg="white").grid(row=0,column=0,columnspan=3)
    tk.Label(dp,text=" ",width=1).grid(row=0,column=3)
    tk.Label(dp, text="Item Name", width=15, pady=10, bg="SteelBlue", font=("Calibri", 16), fg="white").grid(row=0,column=4,columnspan=3)
    tk.Label(dp,text=" ",width=1).grid(row=0,column=7)
    tk.Label(dp, text="Price", width=5, pady=10,padx=30, bg="SteelBlue", font=("Calibri", 16), fg="white").grid(row=0,column=8,columnspan=3)
    mydb = mysql.connector.connect(host="localhost", user="root", password="admin", database="hiten")
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM Sweets')
    myres=mycursor.fetchall()
    #x is a tuple: (sno,sweet,price)
    lst=[]
    for x in myres:
        lst.append(x)
    RealDispFunc(lst,pagenumber[0])
    Real= partial(RealDispFunc,lst,pagenumber[0])
    RealBack=partial(RealBackFunc,lst,pagenumber[0])
    tk.Button(dp,text="next",width=5,bg="Grey",font=("Calibri",14),fg="black",command=Real).grid(row=16,column=9,columnspan=1,sticky="e")
    tk.Button(dp, text="back", width=5, bg="Grey", font=("Calibri", 14), fg="black", command=RealBack).grid(row=16,column=8,columnspan=1,sticky="w")

def RealDispFunc(lst,l):
    ClearDisp()
    j=2
    l=pagenumber[0]
    x=[]
    for i in range(l,l+7):
        x=lst[i]
        tk.Label(dp, text=x[0], width=5, pady=10, bg="FloralWhite", font=("Calibri", 16), fg="black").grid(row=j, column=0, columnspan=3)
        tk.Label(dp, text=" ", width=1).grid(row=0, column=3)
        tk.Label(dp, text=x[1], anchor="w", width=15, pady=10, bg="FloralWhite", font=("Calibri", 16), fg="black").grid(row=j, column=4, columnspan=3)
        tk.Label(dp, text=" ", width=1).grid(row=0, column=7)
        tk.Label(dp, text=x[2], width=10, pady=10, bg="FloralWhite", font=("Calibri", 16), fg="black").grid(row=j,column=8,columnspan=3)
        tk.Label(dp, text="").grid(row=j + 1)
        j += 2
    pagenumber[0] += 7
    print(pagenumber[0])

def RealBackFunc(lst,l):
    ClearDisp()
    j=2
    l=pagenumber[0]
    x=[]
    for i in range(l-7,l):
        x=lst[i]
        tk.Label(dp, text=x[0], width=5, pady=10, bg="FloralWhite", font=("Calibri", 16), fg="black").grid(row=j, column=0, columnspan=3)
        tk.Label(dp, text=" ", width=1).grid(row=0, column=3)
        tk.Label(dp, text=x[1], anchor="w", width=15, pady=10, bg="FloralWhite", font=("Calibri", 16), fg="black").grid(row=j, column=4, columnspan=3)
        tk.Label(dp, text=" ", width=1).grid(row=0, column=7)
        tk.Label(dp, text=x[2], width=10, pady=10, bg="FloralWhite", font=("Calibri", 16), fg="black").grid(row=j,column=8,columnspan=3)
        tk.Label(dp, text="").grid(row=j + 1)
        j += 2
    if pagenumber[0]==7:
        pagenumber[0]=7
    else:
        pagenumber[0]-=7
    print(pagenumber[0])

def ClearDisp():
    j=2
    for i in range(0,7):
        tk.Label(dp, text=" ", width=5, pady=10, bg="FloralWhite", font=("Calibri", 16), fg="black").grid(row=j, column=0, columnspan=3)
        tk.Label(dp, text=" ", width=1).grid(row=0, column=3)
        tk.Label(dp, text=" ", anchor="w", width=15, pady=10, bg="FloralWhite", font=("Calibri", 16), fg="black").grid(row=j, column=4, columnspan=3)
        tk.Label(dp, text=" ", width=1).grid(row=0, column=7)
        tk.Label(dp, text=" ", width=10, pady=10, bg="FloralWhite", font=("Calibri", 16), fg="black").grid(row=j,column=8,columnspan=3)
        tk.Label(dp, text="").grid(row=j + 1)
        j += 2


#----------------------------Main Program-------------------------------
global pagenumber
global mw
global btnADD
global displaybutton
global closebutton
global lst

pagenumber=[0]

mw = tk.Tk()
mw.title('Sweets Shop System')
mw.geometry("500x650")
menu=tk.Menu(mw)
mw.config(menu=menu)
filemenu=tk.Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Login',command=LoginPage)
filemenu.add_command(label='Exit',command=mw.destroy)
helpmenu=tk.Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')

label = tk.Label(mw, text = "ANAND SWEETS SHOP", bg = "SteelBlue",width=32, bd = 30, fg = "white", font = ("Calibri",20)).grid(row=0,column=0)
tk.Label(mw,text="").grid(row=1,column=0)
tk.Label(mw,text="").grid(row=2,column=0)
tk.Label(mw,text="").grid(row=3,column=0)
tk.Label(mw,text="").grid(row=4,column=0)
btnADD = tk.Button(text="Add item",font=("Calibri",15),bg="SteelBlue",state=tk.DISABLED,width=30,pady=20,command=AddFunc)
btnADD.grid(row=5,column=0)
tk.Label(mw,text="").grid(row=6,column=0)
tk.Label(mw,text="").grid(row=7,column=0)
displaybutton= tk.Button(mw,text="Display Items",font=("Calibri",15),bg="SteelBlue",width=30,pady=20,state=tk.DISABLED,command=DisplayFunc)
displaybutton.grid(row=8,column=0)
tk.Label(mw,text="").grid(row=9,column=0)
tk.Label(mw,text="").grid(row=10,column=0)
closebutton= tk.Button(mw,text="Close Window",font=("Calibri",15),bg="SteelBlue",width=30,pady=20,command=mw.destroy,state=tk.DISABLED)
closebutton.grid(row=11,column=0)
mw.mainloop()