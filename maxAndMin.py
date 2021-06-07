#CMH June 2021
def findMax(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    print('The maximum number is' + ' ' + str(max))

def findMin(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    print('The minimum number is' + ' ' + str(min))

findMax([4,2,-2,9])
findMin([4,2,-2,9])