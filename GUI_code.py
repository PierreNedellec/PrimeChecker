"""
Created on Sat Sep 16 17:39:51 2023

@author: PierreNedellec
"""
import time
import tkinter as tk
from main_code import testresult

def pressed():
    primetxt.place_forget()
    start_time = time.time()
    
    p = text.get()
    p = int(''.join(p.split()))
    
    primetxt.config(text = testresult(p))
    primetxt.place(x=10,y=60)

    print("--- %s seconds ---" % (time.time() - start_time))
        
root = tk.Tk()
root.geometry('400x100')
root.title('Prime checker')
root.resizable(False,False)

text = tk.StringVar()

label = tk.Label(root, text='Enter number here: ',font=('Arial',12))
label.place(x=10,y=10)

primetxt = tk.Label(root, text='This number is PRIME',font=('Arial',12))

e = tk.Entry(root,textvariable=text,font=('Arial', 10))
e.place(x=10,y=30,height=20,width=360)

button = tk.Button(root, text='Check', font=('Arial', 12),command=pressed)
button.place(x=300,y=10, height=20, width=70)
                   
root.mainloop()