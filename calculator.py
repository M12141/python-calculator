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

#Function when button is pressed
def click(num):
    entry.delete(0, tk.END)
    entry.insert(0, num) #Adds number/operator to the screen

#Clears the display on the calculator when C button is pressed
def clear():
    entry.delete(0, tk.END)

#Runs when = button is pressed
def equal():
    try:
        answer = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, answer)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

## Button layout on calculator

buttons = [
    ('7', 1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

#Creates buttons
for (text,row,col) in buttons:
    if text =="=":
        tk.Button(window, text=text, width = 5, height=2, command = equal).grid(row=row, column=col)
    else:
        tk.Button(window, text=text, width =5, height = 2, command = lambda t =text: click(t)).grid(row=row, column=col)





