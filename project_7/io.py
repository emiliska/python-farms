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
print()
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

# open file and calculate sum
fileR = open(fname, 'r')
total = 0
count = 0
avgc = 0
for line in fileR:
    total += int(line)
    if int(line)>15:
        count += 1
    avgc += 1
avgc = total/avgc
fileR.close()
print('\nAverage of the numbers in \'', fname,'\': %.1f' % avgc, sep='')
print('Count of the numbers > 15:', count, '\n')

# open file and append summaries
fileR = open(fname, 'a')
fileR.write(str('\nAverage of the numbers in \''+ fname+'\': %.1f' % avgc+'\n'))
fileR.write('Count of the numbers > 15:'+str(count)+'\n')
fileR.close()

'''
PS D:\github\python-farms\project_7> python .\io.py

Programmer: Emily Eubanks
Course:     COSC 146, Winter 2019
Lab#:       7
Due date:   March 27, 2019

Enter a file name:lab7.txt

Contents of the input file 'lab7.txt':
15
14
16
19
11
13
13
11
16
10

Average of the numbers in 'lab7.txt': 13.8
Count of the numbers > 15: 3

Copy the contents of 'lab7.txt' and paste it below:
15
14
16
19
11
13
13
11
16
10

Average of the numbers in 'lab7.txt': 13.8
Count of the numbers > 15:3
'''