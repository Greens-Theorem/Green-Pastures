#author C.M.H. quadratic calculator January 2022
#GUI program to solve quadratic equations
from math import sqrt
from tkinter import *
#Logic
def solver():

    equationx = equation.get()
    a = int(equationx[0])
    b = int(equationx[5])
    c = int(equationx[8])
  
    if(a==0):
        solution.set('DIV / 0 ERR')
        solution2.set('DIV / 0 ERR')
    else:
        solution.set((-b + sqrt((b**2) - (4 * a * c))) / (2*a))
        solution2.set((-b - sqrt((b**2) - (4 * a * c))) / (2*a))
#GUI
window = Tk()
window.title("Quadratic Equation Solver")

l1 = Label(window, text="Equation:")
l1.grid(row=0, column=0)

l2 = Label(window, text="Solution 1: ")
l2.grid(row=1, column=0)

l3 = Label(window, text="Solution 2: ")
l3.grid(row=2, column=0)

equation = StringVar()
e1 = Entry(window, textvariable=equation)
e1.grid(row=0, column=1)

solution = IntVar()
e2 = Entry(window, textvariable=solution, state='readonly')
e2.grid(row=1, column=1)

solution2 = IntVar()
e3 = Entry(window, textvariable=solution2, state='readonly')
e3.grid(row=2, column=1)

b1 = Button(window, text = "Solve", width = 15, bg = 'white', command = solver)
b1.grid(row=0,column =3)

b2 = Button(window, text="Exit", width=12, command=window.destroy)
b2.grid(row=1, column=3)

solution.set('Example: 5x^2+6x+1=0')
solution2.set('Example: 5x^2+6x+1=0')

window.mainloop()