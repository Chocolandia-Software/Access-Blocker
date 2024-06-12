from tkinter import ttk
import tkinter as tk
import pyautogui
import time

size = pyautogui.size()

def proceed_with():
    root.destroy()

def redirect_menu(event):
    time.sleep(0.5)
    pyautogui.click(x=int(size.width / 2), y =int(size.height / 2))
    log.insert(tk.END, "So you think you can just exit this using the Win key? Nah. I already thought of that. Don't be STUPID. \n")
    log.insert(tk.END, "The only way to exit this is to either input the credentials if you know it or to go away if you are not the user. Or just restart using the power button :) \n")

def do_exit():
    log.insert(tk.END, "You think that works? Don't be STUPID. \n")

def alt_f4(event):
    log.insert(tk.END, "Oh, so you think Alt F4 will work, huh? Don't you think that would be too easy? \n")

def activate_system():
    root.protocol("WM_DELETE_WINDOW", do_exit)
    root.bind("<Alt-F4>", alt_f4)
    root.state('zoomed')
    root.overrideredirect(True)
    root.attributes('-topmost', True)
    root.after(500, root.lift())
    root.bind('<Win_L>', redirect_menu)
    root.bind('<Win_R>', redirect_menu)

def activate():
    activate_system()
    log.insert(tk.END, "Security Vault Activated.\n")
    CredBox.grid(row=1, column=0, padx=10, pady=10)
    PasswordSetBox.grid_forget()
    SetPhase.config(text="Please enter the correct credentials.")
    SetPassword.grid_forget()
    checkPassword.grid(row=1, column=1, padx=10, pady=10)
    

def check():
    if str(CredBox.get()) == str(PasswordSetBox.get()):
        log.insert(tk.END, "Correct credentials confirmed. Welcome.\n")
        log.insert(tk.END, "Please click the Proceed button to proceed. \n")
        proceed.grid(row=2, column=0, padx=10, pady=10)
    else:
        log.insert(tk.END, "Incorrect credentials.\n")

root = tk.Tk()

root.title("Security Vault")
root.geometry(str(size.width) + "x" + str(size.height) + "+0+0")

SetPhase = tk.Label(root, text="Please set a Password")
SetPhase.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

PasswordSetBox = ttk.Entry(root)
PasswordSetBox.grid(row=1, column=0, padx=10, pady=10)

SetPassword = ttk.Button(root, text="Set", command=activate)
SetPassword.grid(row=1, column=1, padx=10, pady=10)

CredBox = ttk.Entry(root)
# CredBox.grid(row=1, column=0, padx=10, pady=10)

log = tk.Text(root)
log.grid(row=0, column=2, padx=10, pady=10)

checkPassword = ttk.Button(root, text="Submit", command=check)
# checkPassword.grid(row=1, column=1, padx=10, pady=10)

proceed = ttk.Button(root, text="Proceed", command=proceed_with)

root.mainloop()