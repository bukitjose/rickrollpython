import random
from tkinter import *
from random import randint
import time
import tkinter as tk
import threading
import webbrowser
from tkinter import messagebox
import webbrowser
import sys

def on_yes():
    # code to execute if user clicks "Yes"
    print("Program Executed")
    root.destroy()

def on_no():
    # code to execute if user clicks "No"
    print("Program Exited")
    root.destroy()
    sys.exit()

root = tk.Tk()
root.geometry("600x300")
root.title("Program Execution")

message = tk.Label(root, text="This Program is no joke (Made by Jose),continue running?, For emergency Press ctr + c on your terminal to exit!")
message.pack()

yes_button = tk.Button(root, text="Yes", command=on_yes)
yes_button.pack(padx=10, pady=10)
yes_button.config(width=20, height=5)
yes_button.config(bg='red')
yes_button.pack()

no_button = tk.Button(root, text="No", command=on_no)
no_button.pack(padx=10, pady=10)
no_button.config(width=20, height=5)
no_button.config(bg='blue')
no_button.pack()

root.mainloop()

webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
messagebox.showinfo("HaHa :)", "Bro Just got a Rick Roll, hahaha 😂 ")
root = Tk()
root.withdraw()
root.attributes("-alpha", 0)
root.overrideredirect(1)
root.attributes("-topmost", 1)

def placewindows():
    while True:
        win = Toplevel(root)
        win.geometry("300x60+" + str(randint(0, root.winfo_screenwidth() - 300)) + "+" + str(randint(0, root.winfo_screenheight() - 60)))
        win.overrideredirect(1)
        Label(win, text="You got hacked", fg="red").place(relx=.38, rely=.3)
        win.lift()
        win.attributes("-topmost", True)
        win.attributes("-topmost", False)
        root.lift()
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)
        time.sleep(.05)

threading.Thread(target=placewindows).start()

root.mainloop()


