import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys

def update_progressbar():
    if progressbar["value"] < 100:
        progressbar["value"] +=1
        progressbar.update()
        root.after(600, update_progressbar)
    else:
        tk.messagebox.showerror("Error", "An error has occurred!, System32 Not Found!")
        sys.exit()

root = tk.Tk()
root.geometry("500x200")
root.title("Processing...")
root.protocol("WM_DELETE_WINDOW", lambda: None)

label = tk.Label(root, text="Processing...")
label.pack()

progressbar = ttk.Progressbar(root, length=400, mode='determinate')
progressbar.pack()

root.after(0, update_progressbar)
root.mainloop()
