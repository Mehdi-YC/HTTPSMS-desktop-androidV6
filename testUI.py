import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style

styles= ["minty","flatly","cosmo","litera"]
#-------------------------------FUNCTIONS---------------------- 
def SMStest(a):
    print("sms test")

def addStyle():
    tk.style=Style(e_numTest.get())
#--------------------------------------------------------------
#------------------------------UI----------------------------- 
root = tk.Tk()
tk.style = Style(styles[0])
root.title('To-Do List')
root.geometry("600x300+500+300")


#L1
label = ttk.Label(root, text = 'Groupes')
label.place(x=30, y=30)

groupes = tk.Listbox(root, height=12, selectmode='SINGLE')
groupes.bind('<<ListboxSelect>>', SMStest)
groupes.place(x=30, y = 60)


#L2
label2 = ttk.Label(root, text = 'Contactes')
label2.place(x=215, y=30)

contacts = tk.Listbox(root, height=9, selectmode='SINGLE')
contacts.bind('<<ListboxSelect>>', SMStest)
contacts.place(x=215, y = 60)

label3 = ttk.Label(root, text = 'Compteur')
label3.place(x=215, y=230)

e_counter = ttk.Entry(root, width=9)
e_counter.place(x=280, y=230)


#L3
label = ttk.Label(root, text = 'Num de test')
label.place(x=410, y=30)

e_numTest = ttk.Entry(root, width=20)
e_numTest.place(x=405, y=60)

b_test = ttk.Button(root, text='Test', width=20, command=SMStest)
b_test.place(x=400, y=95)

b_start = ttk.Button(root, text='Start', width=20)
b_start.place(x=400, y=150)

b_pause = ttk.Button(root, text='Pause', width=20)
b_pause.place(x=400, y=190)

b_resume = ttk.Button(root, text='Resume', width=20,command=addStyle)
b_resume.place(x=400, y=230)




root.mainloop()