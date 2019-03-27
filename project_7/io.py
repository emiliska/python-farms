# description: learn more about text file IO and random numbers
import random

# label project
print('''
Programmer: Emily Eubanks
Course:     COSC 146, Winter 2019
Lab#:       7
Due date:   March 27, 2019
''')
# ask for and open file
fname = input('Enter a file name:')
fileW = open (fname, 'w')
# set up a while that iterates 100 times
count = 0
while count < 10:
    fileW.write( str (random.randint(10,20) )+ '\n')
    count = count + 1
fileW.close()

# open and read out contents
fileR = open(fname, 'r')
print('Contents of the input file \'', fname,'\':', sep='')
for line in fileR:
    print(line, end='')
fileR.close()

