#author Cowen Hames January 2021
from tkinter import *

window = Tk()
window.title("Is it a Prime Number?")

def is_Prime():
    for i in range (2, int(user_number.get())):
        if (int(user_number.get()) % i == 0):
            prime_result.set("No")
            break
        else:
            prime_result.set("Yes")

l1 = Label(window, text="Enter a number:")
l1.grid(row=0, column=0)

l2 = Label(window, text="Is it a Prime Number?: ")
l2.grid(row=1, column=0)

user_number = StringVar()
e1 = Entry(window, textvariable=user_number)
e1.grid(row=0, column=1)

prime_result = StringVar()
e4 = Entry(window, textvariable=prime_result, state='readonly')
e4.grid(row=1, column=1)

b1 = Button(window, text = "Check if Prime", width = 15, command = is_Prime)
b1.grid(row=0,column =3)

b2 = Button(window, text="Exit", width=15, command=window.destroy)
b2.grid(row=1, column=3)

window.mainloop()