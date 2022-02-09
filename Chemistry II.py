#Author Cowen M. Hames | April - May 2021. Version 2: February 2022.
#Periodic Table of the Elements Project: Elements, Facts, Symbols and Atomic Numbers
from matplotlib import pyplot as plt
from tkinter import *
#Variables
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
                   
element_Weight = {'Hydrogen' : 1.008, 'Helium' : 4.0026, 'Lithium' : 6.94, 'Beryllium' : 9.0122, 'Boron' : 10.81, 'Carbon' : 12.011, 'Nitrogen' : 14.007, 'Oxygen' : 15.999, 'Fluorine' : 18.998,
                  'Neon' : 20.180, 'Sodium' : 22.990, 'Magnesium' : 24.305, 'Aluminium' : 26.982, 'Silicon' : 28.085, 'Phosphorus' : 30.974, 'Sulfur' : 32.06, 'Chlorine' : 35.45, 'Argon' : 39.948,
                  'Potassium' : 39.098, 'Calcium' : 40.078, 'Scandium' : 44.956, 'Titanium' : 47.867, 'Vanadium' : 50.942, 'Chromium' : 51.996, 'Manganese' : 54.938, 'Iron' : 55.845, 
                  'Cobalt' : 58.933, 'Nickel' : 58.693, 'Copper' : 63.546, 'Zinc' : 65.38, 'Gallium' : 69.723, 'Germanium' : 72.630, 'Arsenic' : 74.922, 'Selnium' : 78.971, 'Bromine' : 79.904,
                  'Krypton' : 83.798, 'Rubidium' : 85.468, 'Strontium' : 87.62, 'Yttrium' : 88.906, 'Zirconium' : 91.244, 'Niobium' : 92.906, 'Molybdenum' : 95.95, 'Technetium' : '(98)', 
                  'Ruthenium' : 101.07, 'Rhodium' : 102.91, 'Palladium' : 106.42, 'Silver' : 107.87, 'Cadmium' : 112.41, 'Indium' : 114.82, 'Tin' : 118.71, 'Antimony' : 121.76, 
                  'Tellurium' : 127.60, 'Iodine' : 126.90, 'Xenon' : 131.29, 'Caesium' : 132.91, 'Barium' : 137.33, 'Lanthanum' : 138.91, 'Cerium' : 140.12, 'Praseodymium' : 140.91, 
                  'Neodymium' : 144.24, 'Promethium' : 145, 'Samarium' : 150.36, 'Europium' : 151.96, 'Gadolinium' : 157.25, 'Terbium' : 158.93, 'Dysprosium' : 162.50, 'Holmium' : 164.93, 
                  'Erbium' : 167.26, 'Thulium' : 168.93, 'Ytterbium' : 173.05, 'Lutetium' : 174.97, 'Hafnium' : 178.49, 'Tantalum' : 180.95, 'Tungsten' : 183.84, 'Rhenium' : 186.21, 
                  'Osmium' : 190.23, 'Iridium' : 192.22, 'Platinum' : 195.08, 'Gold' : 196.97, 'Mercury' : 200.59, 'Thallium' : 204.38, 'Lead' : 207.2, 'Bismuth' : 208.98, 'Polonium' : '(209)',
                  'Astatine' : '(210)', 'Radon' : '(222)', 'Francium' : '(223)', 'Radium' : '(226)', 'Actinium' : '(227)', 'Thorium' : '(232.04)', 'Protactinium' : '(231.04)', 'Uranium' : '(238.03)', 
                  'Neptunium' : '(237)', 'Plutonium' : '(244)', 'Americium' : '(243)', 'Curium' : '(247)', 'Berkelium' : '(247)', 'Califomium' : '(251)', 'Einsteinium' : '(252)', 'Fermium' : '(257)', 
                  'Mendelevium' : '(258)', 'Nobelium' : '(259)', 'Lawrencium' : '(266)', 'Rutherfordium' : '(267)', 'Dubnium' : '(268)', 'Seaborgium' : '(269)', 'Bohrium' : '(270)', 'Hassium' : '(277)', 
                  'Meitnerium' : '(278)', 'Darmstadtium' : '(281)','Roertgenium' : '(282)', 'Copemicium' : '(285)', 'Nihonium' : '(286)', 'Flerovium' : '(289)', 'Moscovium' : '(290)', 'Livermorium' : '(293)', 
                  'Tennessine' : '(294)', 'Oganesson' : '(294)'}

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

element_Period = {'Hydrogen' :1, 'Helium' : 1, 'Lithium' : 2, 'Beryllium' : 2, 'Boron' : 2, 'Carbon' : 2, 'Nitrogen' : 2, 'Oxygen' : 2, 'Fluorine' : 2, 'Neon' : 2,
                  'Sodium' : 3, 'Magnesium' : 3, 'Aluminium' : 3, 'Silicon': 3, 'Phosphorus' : 3, 'Sulfur' : 3, 'Chlorine' : 3, 'Argon' : 3, 'Potassium' : 4, 
                  'Calcium' : 4, 'Scandium' : 4, 'Titanium' : 4, 'Vanadium' : 4, 'Chromium' : 4, 'Manganese' : 4, 'Iron' : 4, 'Cobalt' : 4, 'Nickel' : 4, 
                  'Copper' : 4, 'Zinc' : 4, 'Gallium' : 4, 'Germanium' : 4, 'Arsenic' : 4, 'Selnium' : 4, 'Bromine' : 4, 'Krypton' : 4, 'Rubidium' : 5,
                  'Strontium' : 5, 'Yttrium' : 5, 'Zirconium' : 5, 'Niobium' : 5, 'Molybdenum' : 5, 'Technetium' : 5, 'Ruthenium' : 5, 'Rhodium' : 5, 'Palladium' : 5,
                  'Silver' : 5, 'Cadmium' : 5, 'Indium' : 5, 'Tin' : 5, 'Antimony' : 5, 'Tellurium' : 5, 'Iodine' : 5, 'Xenon' : 5, 'Caesium' : 6, 'Barium' : 6,
                  'Lanthanum' : 6, 'Cerium' : 6, 'Praseodymium': 6, 'Neodymium' : 6, 'Promethium' : 6, 'Samarium' : 6, 'Europium' : 6, 'Gadolinium' : 6, 'Terbium' : 6,
                  'Dysprosium' : 6, 'Holmium' : 6, 'Erbium' : 6, 'Thulium' : 6, 'Ytterbium' : 6, 'Lutetium' : 6, 'Hafnium' : 6, 'Tantalum' : 6, 'Tungsten' : 6,
                  'Rhenium' : 6, 'Osmium' : 6, 'Iridium' : 6, 'Platinum' : 6, 'Gold' : 6, 'Mercury' : 6, 'Thallium' : 6, 'Lead' : 6, 'Bismuth' : 6, 'Polonium' : 6,
                  'Astatine' : 6, 'Radon' : 6, 'Francium' : 7, 'Radium' :  7, 'Actinium' :  7, 'Thorium' :  7, 'Protactinium' :  7, 'Uranium' :  7, 'Neptunium' :  7,
                  'Plutonium' :  7, 'Americium' :  7, 'Curium' :  7, 'Berkelium' :  7, 'Califomium' :  7, 'Einsteinium' :  7, 'Fermium' :  7, 'Mendelevium' :  7, 'Nobelium' :  7,
                  'Lawrencium' :  7, 'Rutherfordium' :  7, 'Dubnium' :  7, 'Seaborgium' :  7, 'Bohrium' :  7, 'Hassium':  7, 'Meitnerium' :  7, 'Darmstadtium' :  7,
                  'Roertgenium' :  7, 'Copemicium' :  7, 'Nihonium' :  7, 'Flerovium' :  7, 'Moscovium' :  7, 'Livermorium' :  7, 'Tennessine' :  7, 'Oganesson' :  7}

element_Type = {'Hydrogen': 'Reactive Non-Metal','Helium' : 'Noble Gas', 'Lithium' : 'Alkali Metal', 'Beryllium' : 'Alkaline Earth Metal', 'Boron' : 'Metalloid', 'Carbon' : 'Reactive Non-Metal',
                  'Nitrogen' : 'Reactive Non-Metal', 'Oxygen' : 'Reactive Non-Metal', 'Fluorine' : 'Reactive Non-Metal', 'Neon' : 'Noble Gas', 'Sodium' : 'Alkali Metal', 
                  'Magnesium' : 'Alkaline Earth Metal', 'Aluminium' : 'Post-Transition Metal', 'Silicon' : 'Metalloid', 'Phosphorus' : 'Reactive Non-Metal', 'Sulfur' : 'Reactive Non-Metal', 
                  'Chlorine' : 'Reactive Non-Metal', 'Argon' : 'Noble Gas', 'Potassium' : 'Alkali Metal', 'Calcium' : 'Alkaline Earth Metal', 'Scandium' : 'Transition Metal', 
                  'Titanium' : 'Transition Metal', 'Vanadium' : 'Transition Metal', 'Chromium' : 'Transition Metal', 'Manganese' : 'Transition Metal', 'Iron' : 'Transition Metal',
                  'Cobalt' : 'Transition Metal', 'Nickel' : 'Transistion Metal', 'Copper' : 'Transition Metal', 'Zinc' : 'Transition Metal', 'Gallium' : 'Post-Transition Metal', 
                  'Germanium' : 'Metalloid', 'Arsenic' : 'Metalloid', 'Selnium' : 'Reactive Non-Metal', 'Bromine' : 'Reactive Non-Metal', 'Krypton' : 'Noble Gas', 'Rubidium' : 'Alkali Metal',
                  'Strontium' : 'Alkaline Earth Metal', 'Yttrium' : 'Transition Metal', 'Zirconium' : 'Transition Metal', 'Niobium' : 'Transition Metal', 'Molybdenum' : 'Transition Metal',
                  'Technetium' : 'Transition Metal', 'Ruthenium' : 'Transition Metal', 'Rhodium' : 'Transition Metal', 'Palladium' : 'Transition Metal', 'Silver' : 'Transition Metal',
                  'Cadmium' : 'Transition Metal', 'Indium' : 'Post-Transition Metal', 'Tin' : 'Post-Transition Metal', 'Antimony' : 'Metalloid', 'Tellurium' : 'Metalloid', 
                  'Iodine' : 'Reactive Non-Metal', 'Xenon' : 'Noble Gas', 'Caesium' : 'Alkali Metal', 'Barium' : 'Alkaline Earth Metal', 'Lanthanum' : 'Lanthanoid', 'Cerium' : 'Lanthanoid', 
                  'Praseodymium' : 'Lanthanoid', 'Neodymium' : 'Lanthanoid', 'Promethium' : 'Lanthanoid', 'Samarium' : 'Lanthanoid', 'Europium' : 'Lanthanoid', 'Gadolinium' : 'Lanthanoid', 
                  'Terbium' : 'Lanthanoid', 'Dysprosium' : 'Lanthanoid', 'Holmium' : 'Lanthanoid', 'Erbium' : 'Lanthanoid', 'Thulium' : 'Lanthanoid', 'Ytterbium' : 'Lanthanoid', 
                  'Lutetium' : 'Lanthanoid', 'Hafnium' : 'Transition Metal', 'Tantalum' : 'Transition Metal', 'Tungsten' : 'Transition Metal', 'Rhenium' : 'Transition Metal', 
                  'Osmium' : 'Transition Metal', 'Iridium' : 'Transition Metal', 'Platinum' : 'Transition Metal', 'Gold' : 'Transition Metal', 'Mercury' : 'Transition Metal', 
                  'Thallium' : 'Post-Transition Metal', 'Lead' : 'Post-Transition Metal', 'Bismuth' : 'Post-Transition Metal', 'Polonium' : 'Post-Transition Metal', 'Astatine' : 'Metalloid',
                  'Radon' : 'Noble Gas', 'Francium' : 'Alkali Metal', 'Radium' : 'Alkaline Earth Metal', 'Actinium' : 'Actinoid', 'Thorium' : 'Actinoid', 'Protactinium' : 'Actinoid', 
                  'Uranium' : 'Actinoid', 'Neptunium' : 'Actinoid', 'Plutonium' : 'Actinoid', 'Americium' : 'Actinoids', 'Curium' : 'Actinoids', 'Berkelium' : 'Actinoid', 
                  'Califomium' : 'Actinoid', 'Einsteinium' : 'Actinoid', 'Fermium' : 'Actinoid', 'Mendelevium' : 'Actinoid', 'Nobelium' : 'Actinoid', 'Lawrencium' : 'Actinoid', 
                  'Rutherfordium' : 'Transition Metal', 'Dubnium' : 'Transition Metal', 'Seaborgium' : 'Transition Metal', 'Bohrium' : 'Transition Metal', 'Hassium' : 'Transition Metal',
                  'Meitnerium' : 'Unknown', 'Darmstadtium' : 'Unknown', 'Roertgenium' : 'Unknown', 'Copemicium' : 'Unknown', 'Nihonium' : 'Unknown', 'Flerovium' : 'Unknown', 
                  'Moscovium' : 'Unknown', 'Livermorium' : 'Unknown', 'Tennessine': 'Unknown','Oganesson' : 'Unknown'}

element_Atomic_Number = dict(zip(elements,range(len(elements))))
for key in element_Atomic_Number:
    element_Atomic_Number[key] += 1

#Logic Methods

def main():
    window.mainloop()

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
    
    for key, value in element_Type.items():
        if selection == key:
            text_type.set(value)

def clear():
    text_AN.set("")
    text_period.set("")
    text_group.set("")
    text_weight.set("")
    text_symbol.set("")
    text_type.set("")

#GUI

window = Tk()
window.geometry('650x400')
cv = Canvas(window,width = 650, height = 400, bg = 'silver')
cv.pack(fill='both',expand=True)
window.title('Chemistry App')
variable = StringVar(window)
variable.set(elements[0])
text_symbol = StringVar()
text_weight = StringVar()
text_group = StringVar()
text_period = StringVar()
text_AN = StringVar()
text_type = StringVar()

om1 = OptionMenu(window, variable, *elements)
om1_cv = cv.create_window(600,25,anchor='ne',window=om1)

b1 = Button(window, text="Get Chemical Element Properties", command=get_Chemical_Properties, bg= 'white')
b1_cv = cv.create_window(630,100,anchor='ne',window=b1)
b2 = Button(window, text = "Clear", command = clear, bg = 'white')
b2_cv = cv.create_window(630,130,anchor='ne',window=b2)
b3 = Button(window, text = "Quit", command = window.destroy, bg= 'white')
b3_cv = cv.create_window(630,160,anchor='ne',window=b3)

cv.create_text(200,75,text="Select an element from the menu and then choose an option.", font = 'Arial 9 bold')

l1 = Label(window, text = "Element Symbol: ",bg='white')
l1_cv = cv.create_window(75,100,anchor='nw',window=l1)
l2 = Label(window, text = "Element Weight: ",bg='white')
l2_cv = cv.create_window(75,130,anchor='nw',window=l2)
l3 = Label(window, text = "Element Group: ",bg='white')
l3_cv = cv.create_window(75,160,anchor='nw',window=l3)
l4 = Label(window, text = "Element Period: ",bg='white')
l4_cv = cv.create_window(75,190,anchor='nw',window=l4)
l5 = Label(window, text = "Element Atomic Number: ",bg='white')
l5_cv = cv.create_window(75,220,anchor='nw',window=l5)
l6 = Label(window, text = "Element Type: ",bg='white')
l6_cv = cv.create_window(75,250,anchor='nw',window=l6)

e1 = Entry(window,textvariable = text_symbol, state = 'readonly',bg='white')
e1_cv = cv.create_window(250,100,anchor='nw',window=e1)
e2 = Entry(window,textvariable = text_weight, state = 'readonly',bg='white')
e2_cv = cv.create_window(250,130,anchor='nw',window=e2)
e3 = Entry(window,textvariable = text_group, state = 'readonly',bg='white')
e3_cv = cv.create_window(250,160,anchor='nw',window=e3)
e4 = Entry(window,textvariable = text_period, state = 'readonly',bg='white')
e4_cv = cv.create_window(250,190,anchor='nw',window=e4)
e5 = Entry(window,textvariable = text_AN, state = 'readonly',bg='white')
e5_cv = cv.create_window(250,220,anchor='nw',window=e5)
e6 = Entry(window,textvariable = text_type, state = 'readonly',bg='white')
e6_cv = cv.create_window(250,250,anchor='nw',window=e6)

if __name__ == '__main__':
    main()