'''
# make a decision using a simple conditional statement
number = int(input('Enter a whole number: '))

if number > 5:
    print('number is bigger than 5')
    print(number + 10)
print('done')

# check for evenness
if number % 2 == 0:
    print(number, 'is even')
    print(number + 1, 'is odd')
    print(number + 1)
print('done!')

# check for oddness
if number % 2 != 0:
    print(number, 'is Odd')
print('done!')


if number %2 == 0:
    print(number, 'is even')
else:
    print(number, 'is odd')


# multi-way conditional statement
if number == 0:
    print('number is zero')
elif number < 0:
    print('number is negative')
else:
    print('number is positive')
print('done!')

'''
score = int(input(('Enter your score:')))
if score >=  90:
    print('You earned an A')
elif score >= 80:
    print('You earned an B')
elif score >= 70:
    print('You earned an C')
elif score >= 60:
    print('You earned an D')
else:
    print('You earned an F')