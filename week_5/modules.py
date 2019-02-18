# viewing imported modules
# python
# >> import math
# >> dir(math)

# to ask for help
# help(math.sqrt)

# import math
# number = float(input('Enter num:'))
# print('square root of', number, 'is:', math.sqrt(number))
'''
import math
number = float(input('Enter num:'))

print('square root of', number, 'is: %.1f' % math.sqrt(number))

print('log base 10 of', number, 'is:', math.log10(number))

'''

#print out 10 random fractions
#import random
#for number in range(10):
    ##print(random.random())
    #print('%.2f' % random.random())

#print out 10 random numbers between 10 and 20, inclusive
import random
for number in range(10,20):
    #print(random.random())
    print(random.randint(10,20), end=" ")
