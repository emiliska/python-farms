'''
number = input('Enter a whole number:')
number = int(number)
print(number + 10)

number = int(input('Enter a whole number:'))
print(number + 10)
'''

# ask user for temp in Fahrenheit
fahrenheit = float(input('Enter temp in Fahrenheit:'))

# Convert temperature from Fahrenheit to Celsius
celcius = (fahrenheit - 32) * (5/9)

# Display celcius temperature to the nearest tenth
print('Celcius Temperature: {:.1f}'.format(celcius))