#Python collections tutorial and refresher
#This program explores Pythons four collection types for data storage (Lists, Sets, Tuples and Dictionaries)
#Of course, these data storage tools are critical especially for those of us specializing in data management
#Author Cowen M. Hames 2/23/21

#Lists

def listTutorial():
    #First, create an empty list:
    myList = []

    #Add an item
    myList.append("Tacos")
    print(myList)

    #Remove an item
    myList.remove("Tacos")
    print(myList)

    #Add multiple items
    myList.append("Burrito")
    myList.append("Chalupa")
    print(myList)

    #Get the length of the list
    print(len(myList))

    #Remove an element based off index
    myList.pop(1)
    print(myList)

    #Delete the entire list:
    myList.append("Tacos")
    myList.append("Nachos")
    print(myList)
    myList.clear()
    print(myList)

    #For loops in lists:

    #Old school way:
    myList = ['Steve','John','Alex','Allison','Hope']
    for i in myList:
        print(i)

    #A better way with list comprehension:
    [print(i) for i in myList]    

    #An even better way:
    for i, ele in enumerate(myList):
        print(i, ",",ele)

    #While loops in lists:
    i = 0
    while i < len(myList):
        print(myList[i])
        i+=1

#Sets

def setTutorial():
    #Create a set:
    mySet = set()

    #Add an element to a set:
    mySet.add('Jake')
    print(mySet)

    #Get the length of a set:
    print(len(mySet))

    #Remove an element from a set:
    mySet.remove('Jake')
    print(mySet)

    #Add multiple items to a set:
    mySet.update(['Jacob', 'Steve', 'Mary', 'Michelle', 'Adam'])
    print(mySet)

    #For loop over a set:
    for value in mySet:
        print(value)

    #Delete entire set
    mySet.clear()
    print(mySet)

#Tuples

def tupleTutorial():
    #Create an empty Tuple:
    myTuple = ()

    #Add an element to the tuple:
    #Tuples are immutable, so they cannot be modified after creation. 
    #You can only create new tuples or use "workarounds" such as list appending:
    list1 = [2, 5, 1, 10, 522]
    myTuple = tuple(list1)
    print(myTuple)

    #You cannot delete items from a Tuple, instead simply create a new one with the values needed
    myTuple2 = ('John', 'Mary', 3, 25, list1)
    print(myTuple2)

    #Get the length of a tuple:
    print(len(myTuple2))

    #For loop through a Tuple:
    for val in myTuple2:
        print(val)

#Dictionaries

def dictionaryTutorial():
    #Create an empty Dictionary:
    myDict = {}

    #Add values (Immutable, must create new instance):
    myDict = {'Nintendo':'Switch', 'Sony':'PS5', 'Microsoft':'XSX'}
    
    #For loop a Dictionary's keys and values:
    for key in myDict.keys():
        print(key)
    for val in myDict.items():
        print(val)

    #Get the length:
    print(len(myDict))

    #Duplicate the dictionary:
    currentConsoles = myDict.copy()
    print(currentConsoles)

    #Clear the dictionary:
    myDict.clear()

#Below, remove the # character to run a specific tutorial method:

#listTutorial()
#setTutorial()
#tupleTutorial()
#dictionaryTutorial()