#Author Cowen M. Hames | April 2021
#Periodic Table of the Elements Project: Elements, Facts, Symbols and Atomic Numbers
#This project will incoporate information about the elements into a graphical user interface for quick, easy access to an elements data
#It will also compare elemental radioactivity

#library imports

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
                   
element_Weight = {'Hydrogen' : 1.008, 'Helium' : 'He', 'Lithium' : 'Li', 'Beryllium' : 'Be', 'Boron' : 'B', 'Carbon' : 'C', 'Nitrogen' : 'N', 'Oxygen' : 'O', 'Fluorine' : 'F', 'Neon' : 'Ne',
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
                  'Roertgenium' : 'Rg', 'Copemicium' : 'Cn', 'Nihonium' : 'Nh', 'Flerovium' : 'Fl', 'Moscovium' : 'Mc', 'Livermorium' : 'Lv', 'Tennessine' : 'Ts', 'Oganesson' : 'Og'}

element_Group = {'Hydrogen' :1, 'Helium' : 18, 'Lithium' : 1, 'Beryllium' : 2, 'Boron' : 13, 'Carbon' : 14, 'Nitrogen' : 15, 'Oxygen' : 16, 'Fluorine' : 17, 'Neon' : 18,
                  'Sodium' : 1, 'Magnesium' : 2, 'Aluminium' : 13, 'Silicon': 14, 'Phosphorus' : 15, 'Sulfur' : 16, 'Chlorine' : 17, 'Argon' : 18, 'Potassium' : 1, 
                  'Calcium' : 2, 'Scandium' : 3, 'Titanium' : 4, 'Vanadium' : 5, 'Chromium' : 6, 'Manganese' : 7, 'Iron' : 8, 'Cobalt' : 9, 'Nickel' : 10, 
                  'Copper' : 11, 'Zinc' : 12, 'Gallium' : 13, 'Germanium' : 14, 'Arsenic' : 15, 'Selnium' : 16, 'Bromine' : 17, 'Krypton' : 18, 'Rubidium' : 1,
                  'Strontium' : 2, 'Yttrium' : 3, 'Zirconium' : 4, 'Niobium' : 5, 'Molybdenum' : 6, 'Technetium' : 7, 'Ruthenium' : 8, 'Rhodium' : 9, 'Palladium' : 10,
                  'Silver' : 11, 'Cadmium' : 12, 'Indium' : 13, 'Tin' : 14, 'Antimony' : 15, 'Tellurium' : 16, 'Iodine' : 17, 'Xenon' : 18, 'Caesium' : 1, 'Barium' : 2,
                  'Lanthanum' : 4, 'Cerium' : 5, 'Praseodymium': 6, 'Neodymium' : 7, 'Promethium' : 8, 'Samarium' : 9, 'Europium' : 10, 'Gadolinium' : 11, 'Terbium' : 12,
                  'Dysprosium' : 13, 'Holmium' : 14, 'Erbium' : 15, 'Thulium' : 16, 'Ytterbium' : 17, 'Lutetium' : 18, 'Hafnium' : 4, 'Tantalum' : 5, 'Tungsten' : 6,
                  'Rhenium' : 7, 'Osmium' : 8, 'Iridium' : 9, 'Platinum' : 10, 'Gold' : 11, 'Mercury' : 12, 'Thallium' : 13, 'Lead' : 14, 'Bismuth' : 15, 'Polonium' : 16,
                  'Astatine' : 17, 'Radon' : 18, 'Francium' : 1, 'Radium' : 2, 'Actinium' : 4, 'Thorium' : 5, 'Protactinium' : 6, 'Uranium' : 7, 'Neptunium' : 8,
                  'Plutonium' : 9, 'Americium' : 10, 'Curium' : 11, 'Berkelium' : 12, 'Califomium' : 13, 'Einsteinium' : 14, 'Fermium' : 15, 'Mendelevium' : 16, 'Nobelium' : 17,
                  'Lawrencium' : 18, 'Rutherfordium' : 4, 'Dubnium' : 5, 'Seaborgium' : 6, 'Bohrium' : 7, 'Hassium': 8, 'Meitnerium' : 9, 'Darmstadtium' : 10,
                  'Roertgenium' : 11, 'Copemicium' : 12, 'Nihonium' : 13, 'Flerovium' : 14, 'Moscovium' : 15, 'Livermorium' : 16, 'Tennessine' : 17, 'Oganesson' : 18}

element_Period = {'Hydrogen' :1, 'Helium' : 'He', 'Lithium' : 'Li', 'Beryllium' : 'Be', 'Boron' : 'B', 'Carbon' : 'C', 'Nitrogen' : 'N', 'Oxygen' : 'O', 'Fluorine' : 'F', 'Neon' : 'Ne',
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
                  'Roertgenium' : 'Rg', 'Copemicium' : 'Cn', 'Nihonium' : 'Nh', 'Flerovium' : 'Fl', 'Moscovium' : 'Mc', 'Livermorium' : 'Lv', 'Tennessine' : 'Ts', 'Oganesson' : 'Og'}


element_Atomic_Number = dict(zip(elements,range(len(elements))))
for key in element_Atomic_Number:
    element_Atomic_Number[key] += 1

#main method

def main():
    window.mainloop()

#get properties method

def get_Chemical_Properties():
    selection = variable.get()
    for key, value in element_Symbol.items():
        if selection == key:
            text_symbol.set(value)

    for key, value in element_Weight.items():
        if selection == key:
            text_weight.set(value)

    for key, value in element_Group.items():
        if selection == key:
            text_group.set(value)

    for key, value in element_Period.items():
        if selection == key:
            text_period.set(value)

    for key, value in element_Atomic_Number.items():
        if selection == key:
            text_AN.set(value)

#method to show a graph comparing all 118 elements by their radiation levels

def get_Radiation_Comparison():
    x = [] * len(elements)
    y = ['low'] * 118
    y[42] = 'high'
    y[60] = 'very high'
    y[82] = 'high'
    y[83] = 'very high'
    y[84] = 'extremely high'
    y[85] = 'very high'
    y[86] = 'extremely high'
    y[87] = 'high'
    y[88] = 'very high'
    y[89] = 'high'
    y[90] = 'high'
    y[91] = 'high'
    y[92] = 'high'
    y[93] = 'high'
    y[94] = 'high'
    y[95] = 'high'
    y[96] = 'high'
    y[97] = 'high'
    y[98] = 'very high'
    y[99] = 'very high'
    y[100] = 'very high'
    y[101] = 'extremely high'
    y[102] = 'extremely high'
    y[103] = 'extremely high'
    y[104] = 'very high'
    y[105] = 'extremely high'
    y[106] = 'extremely high'
    y[107] = 'extremely high'
    y[108] = 'critically high'
    y[109] = 'critically high'
    y[110] = 'critically high'
    y[111] = 'critically high'
    y[112] = 'critically high'
    y[113] = 'critically high'
    y[114] = 'critically high'
    y[115] = 'critically high'
    y[116] = 'critically high'
    y[117] = 'critically high'

    plt.bar(x,y,color='aqua')
    plt.xlabel('Radioactivity')
    plt.ylabel('Atomic Number')
    plt.title('Chemical Element Radioactivity')
    plt.xticks(x,x)
    plt.show()

def clear():
    text_AN.set("")
    text_period.set("")
    text_group.set("")
    text_weight.set("")
    text_symbol.set("")

#GUI code

window = Tk()
window.geometry('650x400')
background = PhotoImage(file = '912022.PNG')
cv = Canvas(window,width = 650, height = 400)
cv.pack(fill='both',expand=True)
cv.create_image(0,0,image=background,anchor='nw')
window.title('Chemistry App')
variable = StringVar(window)
variable.set(elements[0]) # default value
text_symbol = StringVar()
text_weight = StringVar()
text_group = StringVar()
text_period = StringVar()
text_AN = StringVar()

#drop-down

om1 = OptionMenu(window, variable, *elements)
om1_cv = cv.create_window(600,25,anchor='ne',window=om1)

#buttons

b1 = Button(window, text="Get Chemical Element Properties", command=get_Chemical_Properties, bg= 'aqua')
b1_cv = cv.create_window(630,100,anchor='ne',window=b1)
b2 = Button(window, text = "Show Radioactivity Graph", command = get_Radiation_Comparison, bg = 'aqua')
b2_cv = cv.create_window(630,130,anchor='ne',window=b2)
b3 = Button(window, text = "Clear", command = clear, bg = 'aqua')
b3_cv = cv.create_window(630,160,anchor='ne',window=b3)
b4 = Button(window, text = "Quit", command = window.destroy, bg = 'aqua')
b4_cv = cv.create_window(630,190,anchor='ne',window=b4)

#labels

cv.create_text(200,75,text="Select an element from the menu and then choose an option! :)", font = 'Arial 9 bold')

l1 = Label(window, text = "Element Symbol: ",bg='aqua')
l1_cv = cv.create_window(75,100,anchor='nw',window=l1)
l2 = Label(window, text = "Element Weight: ",bg='aqua')
l2_cv = cv.create_window(75,130,anchor='nw',window=l2)
l3 = Label(window, text = "Element Group: ",bg='aqua')
l3_cv = cv.create_window(75,160,anchor='nw',window=l3)
l4 = Label(window, text = "Element Period: ",bg='aqua')
l4_cv = cv.create_window(75,190,anchor='nw',window=l4)
l5 = Label(window, text = "Element Atomic Number: ",bg='aqua')
l5_cv = cv.create_window(75,220,anchor='nw',window=l5)

#Entries

e1 = Entry(window,textvariable = text_symbol, state = 'readonly',bg='aqua')
e1_cv = cv.create_window(250,100,anchor='nw',window=e1)
e2 = Entry(window,textvariable = text_weight, state = 'readonly',bg='aqua')
e2_cv = cv.create_window(250,130,anchor='nw',window=e2)
e3 = Entry(window,textvariable = text_group, state = 'readonly',bg='aqua')
e3_cv = cv.create_window(250,160,anchor='nw',window=e3)
e4 = Entry(window,textvariable = text_period, state = 'readonly',bg='aqua')
e4_cv = cv.create_window(250,190,anchor='nw',window=e4)
e5 = Entry(window,textvariable = text_AN, state = 'readonly',bg='aqua')
e5_cv = cv.create_window(250,220,anchor='nw',window=e5)

#main

if __name__ == '__main__':
    main()
