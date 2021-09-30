#Author CMH...basic Palindrome program 9/29/21
while(True):
    word = input('Welcome to isPlaindrome! Press Q to quit at any time, or enter a word: ')
    if word == 'Q' or word == 'q':
        print('Terminating program...')
        break
    reversed = ''
    arr = []
    for i in word:
        arr.append(i)
    arr.reverse()
    for i in arr:
        reversed += i
    if word == reversed:
        print('Your word is palindrome!')
    else:
        print('Your word is not palindrome!')