#Author C.M.H. Feb 2022 Reading/Writing/Appending Text Files

#Read
file = open(r'C:\Users\cowen\Desktop\VSC\yeah.txt', 'r')
data = file.readlines()

#Write
with open('yeah2.txt', 'w') as file2:
    for line in data:
        file2.write(line)
        file2.write('Isnt this fun?')
        file2.write('\n')

#Append
with open('yeah2.text', 'a') as file2:
    oops = ['forgot this']
    file2.writelines('\n'.join(oops))
