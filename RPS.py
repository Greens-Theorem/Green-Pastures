#author CMH 1/2/21
from tkinter import *
import random
human_score = 0
cpu_score = 0
#Rock Paper Scissors

#WINDOW GUI#

window = Tk()  # TK method that creates a windows objective
window.title("ROCK, PAPER, SCISSORS")

# lISTBOX/SCROLLBAR#

list1=Listbox(window, height=9, width=50, bg = 'yellow')
list1.grid(row=5, column=0, rowspan=6, columnspan=1 ) # we want to span across multiple rows and columns

sb1 = Scrollbar(window)
sb1.grid(row=5, column=2, rowspan=6, columnspan=1, sticky=N+S+W)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

#COMMANDS#


def rock_command():

    global human_score
    global cpu_score
    list1.insert(END, "Your choice: Rock")
    cpu_value = random.randint(0,2)

    if (cpu_value == 0):

        list1.insert(END, "Computer choice: Rock")
    
    elif(cpu_value == 1):

        list1.insert(END, "Computer choice: Paper")
        human_score = human_score - 1
        cpu_score = cpu_score + 1
        if(human_score < 0):
            human_score = 0
        if(cpu_score < 0):
            cpu_score = 0

    elif(cpu_value == 2):

        list1.insert(END, "Computer choice: Scissor")
        human_score = human_score + 1
        cpu_score = cpu_score - 1
        if(human_score < 0):
            human_score = 0
        if(cpu_score < 0):
            cpu_score = 0
     
    list1.insert(END, "HUMAN : " + str(human_score) + " " + "vs" + " " + "CPU : " + str(cpu_score))
    

def paper_command():
    global human_score
    global cpu_score

    list1.insert(END, "Your choice: Paper")
    cpu_value = random.randint(0,2)

    if (cpu_value == 0):

        list1.insert(END, "Computer choice: Rock")
        human_score = human_score + 1
        cpu_score = cpu_score - 1
        if(human_score < 0):
            human_score = 0
        if(cpu_score < 0):
            cpu_score = 0

    elif(cpu_value == 1):

        list1.insert(END, "Computer choice: Paper")

    elif(cpu_value == 2):

        list1.insert(END, "Computer choice: Scissor")
        human_score = human_score - 1
        cpu_score = cpu_score + 1
        if(human_score < 0):
            human_score = 0
        if(cpu_score < 0):
            cpu_score = 0

    list1.insert(END, "HUMAN : " + str(human_score) + " " + "vs" + " " + "CPU : " + str(cpu_score))

def scissor_command():
    global human_score
    global cpu_score

    list1.insert(END, "Your choice: Scissors")
    cpu_value = random.randint(0,2)

    if (cpu_value == 0):

        list1.insert(END, "Computer choice: Rock")
        human_score = human_score - 1
        cpu_score = cpu_score + 1
        if(human_score < 0):
            human_score = 0
        if(cpu_score < 0):
            cpu_score = 0

    elif(cpu_value == 1):

        list1.insert(END, "Computer choice: Paper")
        human_score = human_score + 1
        cpu_score = cpu_score - 1
        if(human_score < 0):
            human_score = 0
        if(cpu_score < 0):
            cpu_score = 0

    elif(cpu_value == 2):

        list1.insert(END, "Computer choice: Scissor")
        
    list1.insert(END, "HUMAN : " + str(human_score) + " " + "vs" + " " + "CPU : " + str(cpu_score))

#BUTTONS#

b1 = Button(window, text = "Rock", width = 9, bg = 'yellow', command = rock_command)
b1.grid(row=1,column =0);

b2 = Button(window, text = "Paper", width = 9, bg = "red", command = paper_command)
b2.grid(row=2,column =0);

b3 = Button(window, text = "Scissors", width = 9, bg = 'magenta', command = scissor_command)
b3.grid(row=3,column =0);

b4 = Button(window, text="Exit", width=12, command=window.destroy)
b4.grid(row=4, column=0)

window.mainloop()