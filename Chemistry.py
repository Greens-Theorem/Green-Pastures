#Author Cowen M. Hames | April 2021
#Periodic Table of the Elements Project: Elements, Facts, Symbols and Atomic Numbers
#This project will incoporate information about the elements into a graphical user interface for quick, easy access to an elements data
#It will also compare elemental radioactivity

#library imports

import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from tkinter import *

#variable declaration

element_Symbol = {}
element_Atomic_Number = {}
element_Period = {}
element_Group = {}

#method to capture chemical element data, including atomic number, symbol, period and group with the chemical elements name entered by the user

def get_Chemical_Properties():
    name = chemical.get()
    data = {}
    chemical_data.set(data)

#method to show a graph comparing all 118 elements by their radiation levels

def get_Radiation_Comparison():
    pass

#main method

def main():
    window.mainloop()

#GUI code

window = Tk()
window.title('Chemistry App')
l1 = Label(window, text="Element Name: ")
l1.grid(row=0, column=0)

l2 = Label(window, text="Element Properties: ")
l2.grid(row=0, column=2)

chemical = StringVar()
e1 = Entry(window, textvariable=chemical)
e1.grid(row=0, column=1)

chemical_data = StringVar()
e4 = Entry(window, textvariable=chemical_data, state='readonly')
e4.grid(row=0, column=3)

b1 = Button(window, text = "Quit", width = 12, command = window.destroy)
b1.grid(row=3,column=3)

b2 = Button(window, text = "Get Element Information", width = 18, command = get_Chemical_Properties)
b2.grid(row=3,column=0)

b3 = Button(window, text = "Radiation Comparsion", width = 18, command = get_Radiation_Comparison)
b3.grid(row=3,column=2)

#main

if __name__ == '__main__':
    main()