'''
# get a number from the keyboard, increment it by 1, and then display it
try:
    number = int(input('Enter a whole number: '))
    number = number + 1
    print(number)
except:
    print('You didn\'t type in a whole number, try again later.')
    number = int(input('Enter a whole number: '))
    number = number + 1
    print(number)
    '''

x = int (input('Enter the first number:'))
y = int (input('Enter the second number:'))
if x < y:
    print('y is bigger than x.')
else:    
    if x == y:
        print('x is equal to y.')
    else:
        print('x is bigger that y.')

# end of chapter 3
# next week chapter 5