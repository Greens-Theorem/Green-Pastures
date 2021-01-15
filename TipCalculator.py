#author Cowen Hames January 2021
from tkinter import *

window = Tk()  # TK method that creates a windows objective
window.title("Tip Calculator")

def bad_service():
    with_tip.set((float(without_tip.get()) * .10 + float(without_tip.get())))
def average_service():
    with_tip.set((float(without_tip.get()) * .15 + float(without_tip.get())))
def good_service():
    with_tip.set((float(without_tip.get()) * .20 + float(without_tip.get())))
def excellent_service():
    with_tip.set((float(without_tip.get()) * .25 + float(without_tip.get())))

l1 = Label(window, text="Pre-Tax Bill without Tip:")
l1.grid(row=0, column=0)

l2 = Label(window, text="Pre-Tax Bill with Tip: ")
l2.grid(row=0, column=2)

without_tip = StringVar()
e1 = Entry(window, textvariable=without_tip)
e1.grid(row=0, column=1)

with_tip = StringVar()
e4 = Entry(window, textvariable=with_tip, state='readonly')
e4.grid(row=0, column=3)

b1 = Button(window, text = "Service: Bad", width = 15, bg = 'red', command = bad_service)
b1.grid(row=1,column =0)

b2 = Button(window, text = "Service: Average", width = 15, bg = 'yellow', command = average_service)
b2.grid(row=1,column =1)

b3 = Button(window, text = "Service: Good", width = 15, bg = 'green', command = good_service)
b3.grid(row=1,column =2)

b4 = Button(window, text = "Service: Excellent", width = 15, bg = 'gold', command = excellent_service)
b4.grid(row=1,column =3)

b5 = Button(window, text="Exit", width=12, command=window.destroy)
b5.grid(row=4, column=3)

window.mainloop()