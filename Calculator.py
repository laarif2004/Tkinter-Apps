#Flaws of this Calculator are at the end of the code
from tkinter import*
from tkinter import ttk
e=0
math=""
st=True
def ini_(x):
    return(x==0)
def calc(a):
    global st
    if st==False:
        s.delete(0,END)
    s.insert(END,f"{a}")
    st=True
    
def adding():
    global e
    global math
    math="add"
    opre.set("+")
    try:
        e=e+int(s.get())
    except ValueError:
        pass
    s.delete(0,END)
def sub():
    global e
    global math
    math="sub"
    opre.set("-")
    try:
        if ini_(e):
            e=int(s.get())
            s.delete(0,END)
            return
        e=e-abs(int(s.get()))
    except ValueError:
        pass
    s.delete(0,END)
def mult():
    global e
    global math
    math="mult"
    opre.set("*")
    try:
        if ini_(e):
            e=int(s.get())
            s.delete(0,END)
            return
        e=e*int(s.get())
    except ValueError:
        pass
    s.delete(0,END)
def divi():
    global e
    global math
    math="divi"
    opre.set("/")
    if ini_(e):
        e=int(s.get())
        s.delete(0,END)
        return
    
    e=e/int(s.get())
    s.delete(0,END)
def show():
    global e
    global math
    global st
    if s.get()=="" or s.get()=="0":
        pass
    else:
        if math=="add":
            e=e+int(s.get())
            s.delete(0,END)
            s.insert(0,e)
        elif math=="sub":
            e=e-abs(int(s.get()))
            s.delete(0,END)
            s.insert(0,e)
        elif math=="mult":
            e=e*int(s.get())
            s.delete(0,END)
            s.insert(0,e)
        elif math=="divi":
            e=e/int(s.get())
            s.delete(0,END)
            s.insert(0,e)
        st=False
        e=0
def clear():
    global st
    global e
    s.delete(0,END)
    e=0
def backspace():
    s.delete(len(s.get())-1)
def theme():
    if  not(n1.cget("bg")=="Black"):
        n1.config(bg="Black",fg="white")
        n2.config(bg="Black",fg="white")
        n3.config(bg="Black",fg="white")
        n4.config(bg="Black",fg="white")
        n5.config(bg="Black",fg="white")
        n6.config(bg="Black",fg="white")
        n7.config(bg="Black",fg="white")
        n8.config(bg="Black",fg="white")
        n9.config(bg="Black",fg="white")
        n0.config(bg="Black",fg="white")
        na.config(bg="Black",fg="white")
        no.config(bg="Black",fg="white")
        nr.config(bg="Black",fg="white")
        det.config(bg="Black",fg="white")
        ns.config(bg="Black",fg="white")
        opeo.config(bg="Black",fg="white")
        s.config(bg="Black",fg="white")
        nm.config(bg="Black",fg="white")
        nd.config(bg="Black",fg="white")
        them.config(bg="Black",fg="white",text="N")
        frame.config(background="Black")
    else:
        n1.config(bg="SystemButtonFace",fg="Black")
        n2.config(bg="SystemButtonFace",fg="Black")
        n3.config(bg="SystemButtonFace",fg="Black")
        n4.config(bg="SystemButtonFace",fg="Black")
        n5.config(bg="SystemButtonFace",fg="Black")
        n6.config(bg="SystemButtonFace",fg="Black")
        n7.config(bg="SystemButtonFace",fg="Black")
        n8.config(bg="SystemButtonFace",fg="Black")
        n9.config(bg="SystemButtonFace",fg="Black")
        n0.config(bg="SystemButtonFace",fg="Black")
        na.config(bg="SystemButtonFace",fg="Black")
        no.config(bg="SystemButtonFace",fg="Black")
        nr.config(bg="SystemButtonFace",fg="Black")
        det.config(bg="SystemButtonFace",fg="Black")
        ns.config(bg="SystemButtonFace",fg="Black")
        opeo.config(bg="SystemButtonFace",fg="Black")
        s.config(bg="SystemButtonFace",fg="Black")
        nm.config(bg="SystemButtonFace",fg="Black")
        nd.config(bg="SystemButtonFace",fg="Black")
        them.config(bg="SystemButtonFace",fg="Black",text="D")
        frame.config(background="SystemButtonFace")

a=Tk()
a.title("Calculator")
frame=Frame()
a.resizable(0,0)
opre=StringVar()
opre.set(math)
s=Entry(frame,relief="sunken",bd=10,justify="right",font=("Arial Black",10))
s.grid(row=0,column=0,columnspan=3,sticky="news")
n1=Button(frame,text="1",font=("Arial Black",10),command=lambda:calc(1))
n1.grid(row=1,column=0,sticky="news",ipadx=20,ipady=10)
n2=Button(frame,text="2",font=("Arial Black",10),command=lambda:calc(2))
n2.grid(row=1,column=1,sticky="news",ipadx=20,ipady=10)
n3=Button(frame,text="3",font=("Arial Black",10),command=lambda:calc(3))
n3.grid(row=1,column=2,ipadx=20,ipady=10,sticky="news")
n4=Button(frame,text="4",font=("Arial Black",10),command=lambda:calc(4))
n4.grid(row=2,column=0,ipadx=20,ipady=10,sticky="news")
n5=Button(frame,text="5",font=("Arial Black",10),command=lambda:calc(5))
n5.grid(row=2,column=1,ipadx=20,ipady=10,sticky="news")
n6=Button(frame,text="6",font=("Arial Black",10),command=lambda:calc(6))
n6.grid(row=2,column=2,ipadx=20,ipady=10,sticky="news")
n7=Button(frame,text="7",font=("Arial Black",10),command=lambda:calc(7))
n7.grid(row=3,column=0,ipadx=20,ipady=10,sticky="news")
n8=Button(frame,text="8",font=("Arial Black",10),command=lambda:calc(8))
n8.grid(row=3,column=1,ipadx=20,ipady=10,sticky="news")
n9=Button(frame,text="9",font=("Arial Black",10),command=lambda:calc(9))
n9.grid(row=3,column=2,ipadx=20,ipady=10,sticky="news")
n0=Button(frame,text="0",font=("Arial Black",10),command=lambda:calc(0))
n0.grid(row=4,column=0,ipadx=20,ipady=10,sticky="news")
na=Button(frame,text="+",font=("Arial Black",10),command=adding)
na.grid(row=4,column=1,ipadx=20,ipady=10,sticky="news")
ns=Button(frame,text="-",font=("Arial Black",10),command=sub)
ns.grid(row=4,column=2,ipadx=20,ipady=10,sticky="news")
nm=Button(frame,text="*",font=("Arial Black",10),command=mult)
nm.grid(row=5,column=0,ipadx=20,ipady=10,sticky="news")
nd=Button(frame,text="/",font=("Arial Black",10),command=divi)
nd.grid(row=5,column=1,ipadx=20,ipady=10,sticky="news")
no=Button(frame,text="C",font=("Arial Black",8),command=clear)
no.grid(row=5,column=2,ipadx=20,ipady=10,sticky="news")
nr=Button(frame,text="=",font=("Arial Black",10),command=show)
nr.grid(row=6,column=0,columnspan=3,ipadx=20,ipady=10,sticky="news")
det=Button(frame,text="DEL",font=("Arial Black",8),command=backspace)
det.grid(row=1,column=3,ipadx=20,ipady=10,padx=5,sticky="news")
opeo=Label(frame,textvariable=opre,font=("Arial Blck",10))
opeo.grid(row=0,column=3,ipadx=20,ipady=10)
them=Button(frame,command=theme,bg="gray",text="D",font=("Arial Black",10))
them.grid(row=2,column=3,sticky="news",rowspan=5,padx=5)
frame.pack(expand=True)

a.mainloop()

#Flaws:
#The entry allows letters
#You have to show the result before changing the operation