import tkinter
from tkinter import *

root = Tk()
root.title('Weight converter')

frame = LabelFrame(root, padx = 10, pady= 10)
frame.pack(padx = 10, pady = 10)

label = Label(frame, text = 'Enter weight in ')
label.grid(row = 0, column = 0, pady =5)

label2 = Label(frame, text = 'here:')
label2.grid(row = 0, column = 2)

weight_list = ['KG', 'Stone', 'Pounds']

#dropdown menu to choose the weight you want to enter
var = StringVar()
var.set(weight_list[0])

drop_enter= OptionMenu(frame, var, *weight_list)
drop_enter.grid(row = 0, column = 1)

#dropdown menu to choose the weight you want the conversion in
label3 = Label(frame, text = 'What should we convert this into?')
label3.grid(row = 1, column = 0)

var2 = StringVar()
var2.set(weight_list[1])

drop_choice=OptionMenu(frame, var2, *weight_list)
drop_choice.grid(row=1, column = 1)

#where the user will enter the weight
w_entry = Entry(frame, width=7)
w_entry.grid(row=0, column=3, padx = 5)
w_entry.insert(0, "weight")

#conversion function

button = Button(frame, text = 'Convert', command = lambda: convert(w_entry.get()))
button.grid(row = 2, column = 1)

final_weight = Label(frame, text = '')
final_weight.grid(row = 3, column = 1)

def convert(w):

    if final_weight.cget('text') != '':
        final_weight['text'] = ''
    if var.get() == 'KG' and var2.get() == 'Stone':
        metric = round(float(w)/6.35029318, 2)
    elif var.get() == 'KG' and var2.get() == 'Pounds':
        metric = round(float(w) * 2.20462, 2)
    elif var.get() == 'Stone' and var2.get() == 'Pounds':
        metric = round(float(w) * 14, 2)
    elif var.get() == 'Stone' and var2.get() == 'KG':
        metric = round(float(w) * 6.35029318, 2)
    elif var.get() == 'Pounds' and var2.get() == 'KG':
        metric = round(float(w)/2.20462, 2)
    elif var.get() == 'Pounds' and var2.get() == 'Stone':
        metric = round(float(w)/14, 2)
    elif var.get() == var2.get():
        metric = 'Try again'

    final_weight.configure(text = str(metric))

root.mainloop()