import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number System Converter")
        #self.geometry("346x210")
        self.st=tk.StringVar(value="bin")
        
        self.menu=Menu(self)
        self.mainloop()
class Menu(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.pack(expand=True)
        tk.Label(self,font=("TkDefaultFont",15),text="Number System Converter").grid(row=0,column=0,
                                                                                     columnspan=2,sticky="news",
                                                                                     pady=2)
        self.entry_(parent,13)
        self.entry_display()
    def entry_(self,parent,z):
        self.entry=tk.Entry(self,font=("TkDefaultFont",15),width=10)
        self.entry.insert(0,"Enter in Decimal")
        self.entry.focus_set()
        self.entry.select_adjust ("end")
        self.chb=tk.Radiobutton(self,variable=parent.st,value="bin",text="Binary",font=("TkDefaultFont",z))
        self.chh=tk.Radiobutton(self,variable=parent.st,value="hex",text="Hexdecimal",font=("TkDefaultFont",z))
        self.butto=tk.Button(self,text="Convert",command=lambda :cal(self,parent),font=("TkDefaultFont",round(z*1.2)))
        self.butto1=tk.Button(self,text="Decode",command=lambda :decode(self,parent),font=("TkDefaultFont",round(z*1.2)))
    def entry_display(self):
        self.columnconfigure((0,1),weight=1,uniform="a")
        self.rowconfigure((0,1,2,3),weight=1,uniform="a")
        self.entry.grid(column=0,row=1,sticky="ew",columnspan=2,padx=12,pady=3)
        self.chb.grid(column=0,row=2,stick="w",padx=13)
        self.chh.grid(column=1,row=2,stick="w",padx=13)
        self.butto.grid(column=0,row=3,columnspan=1,sticky="news",ipady=12)
        self.butto1.grid(column=1,row=3,columnspan=1,sticky="news",ipady=12)
#Command Functions
def cal(self,parent):
    try:
        nb=self.entry.get()
        self.entry.delete(0,"end")
        if parent.st.get()=="hex":
            self.entry.insert(0,hex(int(nb))[2:].upper())
        elif parent.st.get()=="bin":
            self.entry.insert(0,bin(int(nb))[2:])
    except ValueError:
        self.entry.insert(0,"Error")
        self.entry.icursor ("end")
        self.entry.select_adjust ("end")
def decode(self,parent):
    try: 
        nb=self.entry.get()
        self.entry.delete(0,"end")
        if parent.st.get()=="bin":
            self.entry.insert(0,int(nb,2))
        else:
            self.entry.insert(0,int(nb,16))
    except ValueError:
        self.entry.insert(0,"Error")
        self.entry.icursor ("end")
        self.entry.select_adjust ("end")
App()      

