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