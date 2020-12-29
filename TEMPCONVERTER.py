#author CMH
from tkinter import *

#Program to convert temperatures between Fahrenheit, Celsius and Kelvin.

#COMMANDS#

def far_to_cel_command():
    temp = float(temp_entry.get())
    temp = (temp-32) / 1.8
    converted_temp.set(temp)
def far_to_kel_command():
    temp = float(temp_entry.get())
    temp = (temp-32) / 1.8 + 273.15
    converted_temp.set(temp)
    
def far_to_ran_command():
    temp = float(temp_entry.get())
    temp = temp + 459.67
    converted_temp.set(temp)

def cel_to_far_command():
    temp = float(temp_entry.get())
    temp = (temp * 1.8) + 32
    converted_temp.set(temp)

def cel_to_kel_command():
    temp = float(temp_entry.get())
    temp = temp + 273.15
    converted_temp.set(temp)
    
def cel_to_ran_command():
    temp = float(temp_entry.get())
    temp = (temp + 273.15) * 1.8
    converted_temp.set(temp)

def kel_to_far_command():
    temp = float(temp_entry.get())
    temp = (temp * 1.8) -459.67
    converted_temp.set(temp)

def kel_to_cel_command():
    temp = float(temp_entry.get())
    temp = temp - 273.15
    converted_temp.set(temp)
    
def kel_to_ran_command():
    temp = float(temp_entry.get())
    temp = temp * 1.8
    converted_temp.set(temp)

def ran_to_far_command():
    temp = float(temp_entry.get())
    temp = temp - 459.67
    converted_temp.set(temp)

def ran_to_cel_command():
    temp = float(temp_entry.get())
    temp = (temp - 491.67) / 1.8
    converted_temp.set(temp)
    
def ran_to_kel_command():
    temp = float(temp_entry.get())
    temp = temp / 1.8
    converted_temp.set(temp)

def clear_command():
    temp_entry.set("")
    converted_temp.set("")

#WINDOW GUI#

window = Tk()  # TK method that creates a windows objective
window.title("Temperature Converter")

#LABELS#

l1 = Label(window, text="Temperature Entry: ")
l1.grid(row=0, column=0)

l2 = Label(window, text="Converted Temperature: ")
l2.grid(row=0, column=2)

#TEXT ENTRY FIELDS#

temp_entry = StringVar()
e1 = Entry(window, textvariable=temp_entry)
e1.grid(row=0, column=1)

converted_temp = StringVar()
e4 = Entry(window, textvariable=converted_temp, state='readonly')
e4.grid(row=0, column=3)


#BUTTONS#

b1 = Button(window, text="Fahrenheit to Celsius", width=17, bg = 'red', command=far_to_cel_command)
b1.grid(row=3, column=0)

b2 = Button(window, text="Fahrenheit to Kelvin", width=17, bg = 'red', command=far_to_kel_command)
b2.grid(row=4, column=0)

b3 = Button(window, text="Fahrenheit to Rankine", width=17, bg = 'red', command=far_to_ran_command)
b3.grid(row=5, column=0)

b4 = Button(window, text="Celsius to Fahrenheit", width=17, bg = 'cyan', command=cel_to_far_command)
b4.grid(row=6, column=0)

b5 = Button(window, text="Celsius to Kelvin", width=17, bg = 'cyan', command=cel_to_kel_command)
b5.grid(row=7, column=0)

b6 = Button(window, text="Celsius to Rankine", width=17, bg = 'cyan', command=cel_to_ran_command)
b6.grid(row=8, column=0)

b7 = Button(window, text="Kelvin to Fahrenheit", width=17, bg = 'white', command=kel_to_far_command)
b7.grid(row=3, column=1)

b8 = Button(window, text="Kelvin to Celsius", width=17, bg = 'white', command=kel_to_cel_command)
b8.grid(row=4, column=1)

b9 = Button(window, text="Kelvin to Rankine", width=17, bg = 'white', command=kel_to_ran_command)
b9.grid(row=5, column=1)

b10 = Button(window, text="Rankine to Fahrenheit", width=17, bg = 'magenta', command=ran_to_far_command)
b10.grid(row=6, column=1)

b11 = Button(window, text="Rankine to Celsius", width=17, bg = 'magenta', command=ran_to_kel_command)
b11.grid(row=7, column=1)

b12 = Button(window, text="Rankine to Kelvin", width=17, bg = 'magenta', command=ran_to_kel_command)
b12.grid(row=8, column=1)

b13 = Button(window, text ="Clear", width =12, command =clear_command)
b13.grid(row =9, column = 0)

b14 = Button(window, text="Exit", width=12, command=window.destroy)
b14.grid(row=9, column=1)

window.mainloop()