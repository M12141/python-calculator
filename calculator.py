import tkinter as tk

# Creating a window

window = tk.Tk() ##Creates the calculator window
window.title("Calculator")
window.geometry("300x400")

## Display screen
##Creating the calculator screen
entry = tk.Entry(window, width=16, font=("Arial", 20), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, padx=10, columnspan=4)

##Button functions
def click(num):
    entry.delete(0, tk.END)
    entry.insert(0, num)

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        answer = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, answer)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")



