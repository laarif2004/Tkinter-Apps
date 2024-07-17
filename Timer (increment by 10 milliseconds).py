import tkinter as tk
from tkinter import ttk

def start_timer():
    global max_value
    global running
    running = True
    ti.set(0)
    max_value = int(ent.get())
    prog.configure(maximum=max_value)
    update_timer(max_value)
def rest():
    global running
    ti.set(0)
    num.set(0)
    running=False

def stop_timer():
    global max_value
    global running
    if running:
        running=False
        bt2.config(text="Resume")
    else:
        running=True
        bt2.config(text="Stop")
        update_timer(max_value)
        
def update_timer(max_value):
    if running:
        current_value = ti.get()
        if current_value < max_value:
            ti.set(current_value + 0.01)
            num.set(str(current_value)[0:4])
            window.after(10, update_timer, max_value)
window = tk.Tk()
ti = tk.DoubleVar()
num=tk.StringVar(value="0")
window.title('Timer')
fr = tk.Frame(window)
ent = tk.Entry(fr, text='Start',
               font=('Arial Black', 10),
               justify='center')
ent.grid(row=0, column=0, columnspan=2, rowspan=2, sticky='news')

bt1 = tk.Button(fr, text='Start',
                font=('arial black', 13),
                width=10,
                command=start_timer)
bt1.grid(row=2, column=0, pady=10)

bt2 = tk.Button(fr, text='Stop', font=('arial black', 13), width=10,command=stop_timer)
bt2.grid(row=2, column=1, pady=10)


bt3=tk.Button(fr,text='Reset',font=('arial black', 13), width=10,command=rest)
bt3.grid(row=3, column=0, columnspan=2, sticky='news')

prog = ttk.Progressbar(fr, variable=ti)
prog.grid(row=4, column=0, sticky='news', columnspan=2, pady=5, ipady=5)
lab=tk.Label(fr,font=('arial black',13),textvariable=num)
lab.grid(row=5,column=0,columnspan=2,sticky="news")
fr.pack()

window.mainloop()
