import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style

root = tk.Tk()
tk.style = Style('journal')
root.title('To-Do List')
root.geometry("400x250+500+300")


task = []
#------------------------------- Functions--------------------------------
def SMStest():
    word = e1.get()
    if len(word)==0:
        messagebox.showinfo('Empty Entry', 'Enter task name')
    else:
        task.append(word)
        listUpdate()
        e1.delete(0,'end')

def addStyle():
    tk.style=Style(e1.get())
def listUpdate():
    clearList()
    for i in task:
        contacts.insert('end', i)

def delOne():
    try:
        val = contactsget(contactscurselection())
        if val in task:
            task.remove(val)
            listUpdate()
    except:
        messagebox.showinfo('Cannot Delete', 'No Task Item Selected')
    
def deleteAll():
    mb = messagebox.askyesno('Delete All','Are you sure?')
    if mb==True:
        while(len(task)!=0):
            task.pop()
        listUpdate()

def clearList():
    contacts.delete(0,'end')

def bye():
    print(task)
    root.destroy()

task=[]

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print (f'You selected item {index}: {value}')

def periodically_called():
    print("test")
    root.after(1, periodically_called)
#------------------------------- Functions--------------------------------

label = ttk.Label(root, text = 'To-Do List')
e1 = ttk.Entry(root, width=21)

contacts = tk.Listbox(root, height=20, selectmode='SINGLE')
contacts.bind('<<ListboxSelect>>', onselect)
test = ttk.Button(root, text='test', width=20, command=SMStest)
send = ttk.Button(root, text='send', width=20, command=delOne)
b3 = ttk.Button(root, text='loop', width=20, command=periodically_called)
b4 = ttk.Button(root, text='Exit', width=20, command=bye)
b4 = ttk.Button(root, text='Style', width=20, command=addStyle)
b4.pack(pady=10)
listUpdate()

#Place geometry
label.place(x=50, y=50)
e1.place(x=50, y=80)
test.place(x=40, y=120)
send.place(x=50, y=140)
b3.place(x=50, y=170)
b4.place(x=50, y =200)
label.place(x=50, y=10)
contacts.place(x=220, y = 50)
root.mainloop()
