import tkinter as tk

# Creating a window

window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

## Display screen
entry = .tk.Entry(window, width=16, font=("Arial", 20), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, padx=10, columnspan=4)



