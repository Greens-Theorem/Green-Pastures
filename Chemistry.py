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

elements = ['Hydrogen','Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon',
                  'Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 
                  'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 
                  'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selnium', 'Bromine', 'Krypton', 'Rubidium',
                  'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium',
                  'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Caesium', 'Barium',
                  'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium',
                  'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten',
                  'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium',
                  'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium',
                  'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Califomium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium',
                  'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium',
                  'Roertgenium', 'Copemicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']

element_Symbol = {'Hydrogen' :'H', 'Helium' : 'He', 'Lithium' : 'Li', 'Beryllium' : 'Be', 'Boron' : 'B', 'Carbon' : 'C', 'Nitrogen' : 'N', 'Oxygen' : 'O', 'Fluorine' : 'F', 'Neon' : 'Ne',
                  'Sodium' : 'Na', 'Magnesium' : 'Mg', 'Aluminium' : 'Al', 'Silicon': 'Si', 'Phosphorus' : 'P', 'Sulfur' : 'S', 'Chlorine' : 'Cl', 'Argon' : 'Ar', 'Potassium' : 'K', 
                  'Calcium' : 'Ca', 'Scandium' : 'Sc', 'Titanium' : 'Ti', 'Vanadium' : 'V', 'Chromium' : 'Cr', 'Manganese' : 'Mn', 'Iron' : 'Fe', 'Cobalt' : 'Co', 'Nickel' : 'Ni', 
                  'Copper' : 'Cu', 'Zinc' : 'Zn', 'Gallium' : 'Ga', 'Germanium' : 'Ge', 'Arsenic' : 'As', 'Selnium' : 'Se', 'Bromine' : 'Br', 'Krypton' : 'Kr', 'Rubidium' : 'Rb',
                  'Strontium' : 'Sr', 'Yttrium' : 'Y', 'Zirconium' : 'Zr', 'Niobium' : 'Nb', 'Molybdenum' : 'Mo', 'Technetium' : 'Tc', 'Ruthenium' : 'Ru', 'Rhodium' : 'Rh', 'Palladium' : 'Pd',
                  'Silver' : 'Ag', 'Cadmium' : 'Cd', 'Indium' : 'In', 'Tin' : 'Sn', 'Antimony' : 'Sb', 'Tellurium' : 'Te', 'Iodine' : 'I', 'Xenon' : 'Xe', 'Caesium' : 'Cs', 'Barium' : 'Ba',
                  'Lanthanum' : 'La', 'Cerium' : 'Ce', 'Praseodymium': 'Pr', 'Neodymium' : 'Nd', 'Promethium' : 'Pm', 'Samarium' : 'Sm', 'Europium' : 'Eu', 'Gadolinium' : 'Gd', 'Terbium' : 'Tb',
                  'Dysprosium' : 'Dy', 'Holmium' : 'Ho', 'Erbium' : 'Er', 'Thulium' : 'Tm', 'Ytterbium' : 'Yb', 'Lutetium' : 'Lu', 'Hafnium' : 'Hf', 'Tantalum' : 'Ta', 'Tungsten' : 'W',
                  'Rhenium' : 'Re', 'Osmium' : 'Os', 'Iridium' : 'Ir', 'Platinum' : 'Pt', 'Gold' : 'Au', 'Mercury' : 'Hg', 'Thallium' : 'Tl', 'Lead' : 'Pb', 'Bismuth' : 'Bi', 'Polonium' : 'Po',
                  'Astatine' : 'At', 'Radon' : 'Rn', 'Francium' : 'Fr', 'Radium' : 'Ra', 'Actinium' : 'Ac', 'Thorium' : 'Th', 'Protactinium' : 'Pa', 'Uranium' : 'U', 'Neptunium' : 'Np',
                  'Plutonium' : 'Pu', 'Americium' : 'Am', 'Curium' : 'Cm', 'Berkelium' : 'Bk', 'Califomium' : 'Cf', 'Einsteinium' : 'Es', 'Fermium' : 'Fm', 'Mendelevium' : 'Md', 'Nobelium' : 'No',
                  'Lawrencium' : 'Lr', 'Rutherfordium' : 'Rf', 'Dubnium' : 'Db', 'Seaborgium' : 'Sg', 'Bohrium' : 'Bh', 'Hassium': 'Hs', 'Meitnerium' : 'Mt', 'Darmstadtium' : 'Ds',
                  'Roertgenium' : 'Rg', 'Copemicium' : 'Cn', 'Nihonium' : 'Nh', 'Flerovium' : 'Fl', 'Moscovium' : 'Mc', 'Livermorium' : 'Lv', 'Tennessine' : 'Ts', 'Oganesson' : 'Og'
                   }
element_Atomic_Number = {}
element_Period = {}
element_Group = {}


#method to show a graph comparing all 118 elements by their radiation levels

def get_Radiation_Comparison():
    pass

#main method

def main():
    window.mainloop()

#get properties method

def get_Chemical_Symbol():
    selection = variable.get()
    for key, value in element_Symbol.items():
        if selection == key:
            text_symbol.set(value)

def get_Chemical_Weight():
    pass

def get_Chemical_Group():
    pass

def get_Chemical_Period():
    pass

def get_Chemical_Weight():
    pass

def get_Chemical_Atomic_Number():
    pass

#GUI code

window = Tk()
window.title('Chemistry App')

variable = StringVar(window)
variable.set(elements[0]) # default value

om1 = OptionMenu(window, variable, *elements)
om1.grid(row=0, column = 2)

b1 = Button(window, text="Get Chemical Element Symbol", command=get_Chemical_Symbol)
b1.grid(row = 2, column = 2)

b2 = Button(window, text = "Get Chemical Element Weight", command = get_Chemical_Weight)
b2.grid(row=3,column=2)

b3 = Button(window, text = "Get Chemical Element Group", command = get_Chemical_Group)
b3.grid(row=4,column=2)

b4 = Button(window, text = "Get Chemical Element Period", command = get_Chemical_Period)
b4.grid(row=5,column=2)

b5 = Button(window, text = "Get Chemical Element Atomic Number", command = get_Chemical_Atomic_Number)
b5.grid(row=6,column=2)

b5 = Button(window, text = "Show Radioactivity Graph", command = get_Radiation_Comparison)
b5.grid(row=7,column=2)

b6 = Button(window, text = "Quit", command = window.destroy)
b6.grid(row=8,column=2)


l1 = Label(window, text = "Select an element from the menu and then choose an option!")
l1.grid(row=0, column = 0)

l2 = Label(window, text = "Element Symbol: ")
l2.grid(row = 1, column = 0)

l3 = Label(window, text = "Element Weight: ")
l3.grid(row = 2, column = 0)

l4 = Label(window, text = "Element Group: ")
l4.grid(row = 3, column = 0)

l5 = Label(window, text = "Element Period: ")
l5.grid(row = 4, column = 0)

l6 = Label(window, text = "Element Atomic Number: ")
l6.grid(row = 5, column = 0)

text_symbol = StringVar()
text_weight = StringVar()
text_group = StringVar()
text_period = StringVar()
text_AN = StringVar()

e1 = Entry(window,textvariable = text_symbol, state = 'readonly')
e1.grid(row = 1, column = 1)

e2 = Entry(window,textvariable = text_weight, state = 'readonly')
e2.grid(row = 2, column = 1)

e3 = Entry(window,textvariable = text_group, state = 'readonly')
e3.grid(row = 3, column = 1)

e4 = Entry(window,textvariable = text_period, state = 'readonly')
e4.grid(row = 4, column = 1)

e5 = Entry(window,textvariable = text_AN, state = 'readonly')
e5.grid(row = 5, column = 1)

#main


if __name__ == '__main__':
    main()
