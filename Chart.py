import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

# root window
root = tk.Tk()
root.geometry("600x500")
root.resizable(False, False)
root.title('Sign In')

# store email address and password
name = tk.StringVar()
sot = tk.StringVar()

lstx = []
lsty= []

def Add_List():
    x=name.get()
    y=sot.get()
    lstx.append(x)
    lsty.append(y)
    
def ShowChart():
    x = np.array (lstx)
    y = np.array(lsty)
    plt.bar(x,y)
    plt.show()


# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# name
name_label = ttk.Label(signin, text="Name:")
name_label.pack(fill='x', expand=True)

name_entry = ttk.Entry(signin, textvariable=name)
name_entry.pack(fill='x', expand=True)
name_entry.focus()

# sot
sot_label = ttk.Label(signin, text="y:")
sot_label.pack(fill='x', expand=True)

sot_entry = ttk.Entry(signin, textvariable=sot)
sot_entry.pack(fill='x', expand=True)

# Add button
add_button = ttk.Button(signin, text="Add To Chart", command=Add_List)
add_button.pack(expand=True, pady=10)

# Show Chart button
show_button = ttk.Button(signin, text="Show Chart", command=ShowChart)
show_button.pack(expand=True, pady=10)


root.mainloop()