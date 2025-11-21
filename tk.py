import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry box
entry = tk.Entry(root, width=25, borderwidth=5, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button click function
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Clear function
def button_clear():
    entry.delete(0, tk.END)

# Equal function
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=30, pady=20, bg="lightgreen",
                  command=button_equal).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=30, pady=20,
                  command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Clear button
tk.Button(root, text='Clear', padx=120, pady=20, bg="lightcoral",
          command=button_clear).grid(row=5, column=0, columnspan=4)

# Run the window
root.mainloop()
