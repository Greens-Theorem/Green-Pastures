#Author C.M.H.
#Compound Interest GUI Calculator February 2022
from tkinter import *

#Logic
def calculator():

    d = float(Principal.get())
    i = float(Interest.get()) * .01
    t = float(Years.get())
    f = int(Frequency.get())
    result.set(round(d*(1+(i/f))**(f*t)))
   
#GUI
window = Tk()
window.title("Compound Interest Calculator")

l1 = Label(window, text="Principal Deposit:")
l1.grid(row=0, column=0)

l2 = Label(window, text="Interest Rate: ")
l2.grid(row=1, column=0)

l3 = Label(window, text="Years")
l3.grid(row=2, column = 0)

l4 = Label(window, text = "Frequency (Times a year)")
l4.grid(row=3, column = 0)

l5 = Label(window, text = "Result")
l5.grid(row=4, column = 0)


Principal = StringVar()
e1 = Entry(window, textvariable=Principal)
e1.grid(row=0, column=1)

Interest = StringVar()
e2 = Entry(window, textvariable=Interest)
e2.grid(row=1, column=1)

Years = StringVar()
e3 = Entry(window, textvariable=Years)
e3.grid(row=2, column=1)

Frequency = StringVar()
e4 = Entry(window, textvariable=Frequency)
e4.grid(row=3, column=1)

result = StringVar()
e5 = Entry(window, textvariable=result, state='readonly')
e5.grid(row=4, column=1)


b1 = Button(window, text = "Calculate", width = 15, bg = 'white', command = calculator)
b1.grid(row=0,column =3)

b2 = Button(window, text="Exit", width=12, command=window.destroy)
b2.grid(row=1, column=3)

window.mainloop()