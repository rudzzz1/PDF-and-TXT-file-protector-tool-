import tkinter as tk
from tkinter import messagebox
from pdf_protector import pdf_protect
from text_protector import *


def option_1():
    global fname
    global pwd
    win = tk.Toplevel()
    win.title("PDF protector")
    tk.Label(win, text="Enter file name:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(win, text="Enter password:").grid(row=1, column=0, padx=5, pady=5)
    file_entry = tk.Entry(win)
    file_entry.grid(row=0, column=1, padx=5, pady=5)
    pass_entry = tk.Entry(win, show="*")
    pass_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(win, text="Submit", command=lambda: store_values(file_entry, pass_entry)).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    


def store_values(file_entry, pass_entry):
    global fname
    global pwd
    fname = file_entry.get()
    pwd = pass_entry.get()
    messagebox.showinfo("Success", "File name and password stored successfully")
    pdf_protect(fname, pwd)

def option_2():
    global fname1
    global pwd1
    win = tk.Toplevel()
    win.title("PDF protector")
    tk.Label(win, text="Enter file name:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(win, text="Enter password:").grid(row=1, column=0, padx=5, pady=5)
    file_entry = tk.Entry(win)
    file_entry.grid(row=0, column=1, padx=5, pady=5)
    pass_entry = tk.Entry(win, show="*")
    pass_entry.grid(row=1, column=1, padx=5, pady=5)
    tk.Button(win, text="Submit", command=lambda: store_values1(file_entry, pass_entry)).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

def store_values1(file_entry, pass_entry):
    global fname1
    global pwd1
    fname = file_entry.get()
    pwd = pass_entry.get()
    messagebox.showinfo("Success", "File name and password stored successfully")
    text_protect(fname, pwd)    

root = tk.Tk()
root.title("Option Selector")

fname = ""
pwd = ""
fname1 = ""
pwd1 = ""

tk.Button(root, text="PDF protect", command=option_1).pack(padx=5, pady=5)
tk.Button(root, text="TXT protect", command=option_2).pack(padx=5, pady=5)

root.mainloop()
