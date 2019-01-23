'''
n=2
m=3
print(n/m)
print(n/m + 1)
print('n/m + 1 =' , n/m + 1)
#print('n/m + 1 =' , n/m + 1, sep='     ' )
print('n/m + 1 =' ,'\n' , n/m + 1)
print('n/m + 1 =' , n/m + 1, sep='\n' )
print('n/m + 1 =' , n/m + 1, 125, sep='\n')
'''

#how to format my output
x = 2
y = 3
result = x/y
print('result =', result)
# format using string format operator %
'''
print('text' % result) text
print('    ' % result) escape sequence
print('%[]' % result) format specification %[flag][width][letter]
    f | float number
    d | whole number
    s | string
'''
print('result = %f' % result)
print('result = %.2f' % result)
print('result = %5.2f' % result)
print('%d\n%.2f' % (12 , 2.765))
print('%05d\n%.2f' % (12 , 2.765))