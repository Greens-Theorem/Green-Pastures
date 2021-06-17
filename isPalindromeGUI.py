#Author Cowen M. Hames | June 2021 | Project #13: Palindrome GUI | Version 0.2

from tkinter import *

def isPalindrome():
    val = word_entry.get()
    val.strip()
    forward_val = []
    rval = ''
    for i in val:
        forward_val.append(i)
    forward_val.reverse()
    for i in forward_val:
        rval += i
    if val == rval:
        result.set('Yes!')
    else:
        result.set('No!')

window = Tk()
window.title('Is it Palindrome?')
word_entry = StringVar()
result = StringVar()
l1 = Label(window, text = "Your word: ",bg='lime')
l1.grid(row = 0, column = 0)
e1 = Entry(window, textvariable = word_entry,bg='lime')
e1.grid(row = 0, column = 1)
l2 = Label(window,text = 'Is it Palindrome?', bg='lime')
l2.grid(row=1, column = 0)
e2 = Entry(window, textvariable = result, state = 'readonly')
e2.grid(row=1,column = 1)
b1 = Button(window, text="Check if Palindrome", command=isPalindrome, width = 15, bg= 'lime')
b1.grid(row = 0, column = 4)
b2 = Button(window, text = "Quit", command = window.destroy, width=12, bg = 'lime')
b2.grid(row = 1, column = 4)
window.mainloop()
