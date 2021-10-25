import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style
import time
import os
from os.path import isfile, join
import subprocess

styles= ["minty","flatly","cosmo","litera"]
#-------------------------------FUNCTIONS---------------------- 
def fillGroupes():
    files = [f for f in os.listdir(G_path) if isfile(join(G_path, f))]
    for f in files:
        counter[f.split(".")[0]] = 0
        groupes.insert('end',f.split(".")[0])

def fillContacts(e):
    
    selectedGroupe = groupes.get(groupes.curselection()[0])
    e_counter_var.set(counter[selectedGroupe])

    with open(f'{G_path+selectedGroupe}.txt', 'r',encoding='utf-8')as SMSfile:
        lines = SMSfile.readlines()

    message = lines[0]
    e_message.delete(1.0,'end')
    e_message.insert(1.0,message)

    contacts.delete(0,'end')
    for line in lines[1::]:
        contacts.insert('end',line)


def sender(secs):

    secs += 1
    counter["Appartaffaire"]+=1
    print(counter["Appartaffaire"])
    if secs % 2 == 0:  # Every other second.
        time.sleep(1)
        print("sleeping")
    print("test")
    after_id = root.after(100, sender,secs)  # Check again in 1 second.

def start():
    e_message["state"] = "disabled"
    contacts["state"] = "disabled"
    groupes["state"] = "disabled"
    e_numTest["state"] = "disabled"
    b_resume["state"] = "normal"
    secs = 0
    sender(secs)  # Start repeated checking.


def pause():
    if after_id:
        root.after_cancel(after_id)
        after_id = None

def SMStest():
    message=e_message.get("1.0","end").replace("'","\\'").replace("'","'\\").replace(" ","\ ")
    proc = subprocess.Popen(f'adb shell service call isms 7 i32 2 s16 "com.android.mms" s16 "{e_numTest.get()}" s16 "null" s16 "{message.rstrip()}" s16 "null" s16 "null"',shell=True,stdout=subprocess.PIPE)
    result = proc.stdout.read()
    if result == b"Result: Parcel(00000000    '....')\r\r\n":
        print("sent")
    else:
        print('error : ',result) 
def contactSelected(e):
    e_numTest_var.set(contacts.get(contacts.curselection()[0]))

def addStyle():
    tk.style=Style(e_numTest.get(0))
#--------------------------------------------------------------


#------------------------------UI----------------------------- 
root = tk.Tk()
tk.style = Style(styles[0])
root.title('Bulk SMSing')
root.geometry("600x500+500+300")


#L1
label = ttk.Label(root, text = 'Groupes')
label.place(x=30, y=30)

groupes = tk.Listbox(root, height=12, selectmode='SINGLE')
groupes.bind('<<ListboxSelect>>', fillContacts)
groupes.place(x=30, y = 60)


#L2
label2 = ttk.Label(root, text = 'Contacts')
label2.place(x=215, y=30)

contacts = tk.Listbox(root, height=9, selectmode='SINGLE')
contacts.bind('<<ListboxSelect>>', contactSelected)
contacts.place(x=215, y = 60)

label3 = ttk.Label(root, text = 'Compteur')
label3.place(x=215, y=230)

e_counter_var = tk.StringVar()
e_counter = ttk.Entry(root, width=9,textvariable=e_counter_var)
e_counter.place(x=280, y=230)


#L3
label = ttk.Label(root, text = 'Num de test')
label.place(x=410, y=30)
e_numTest_var = tk.StringVar()
e_numTest = ttk.Entry(root, width=20,textvariable=e_numTest_var)
e_numTest.place(x=405, y=60)

b_test = ttk.Button(root, text='Test', width=20, command=SMStest)
b_test.place(x=400, y=95)

b_start = ttk.Button(root, text='Start', width=20,command=start)
b_start.place(x=400, y=150)

b_pause = ttk.Button(root, text='Pause', width=20)
b_pause.place(x=400, y=190)

b_resume = ttk.Button(root, text='Resume', width=20,command=addStyle)
b_resume.place(x=400, y=230)

#LX-2
label4 = ttk.Label(root, text = 'Message')
label4.place(x=30, y=300)

e_message = tk.Text(root, width=75,height=8)
e_message.place(x=30, y=320)

#------Vars----------
message=""
counter={}
G_path = f'{str(os.path.dirname(__file__))}/groupes/'
b_resume["state"] = "disabeled"
fillGroupes()
secs=0
#contacts.itemconfig(1, {'bg':'#e36b6f','fg':'white'})
root.mainloop()