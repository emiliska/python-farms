import random
'''
# prompt for and read in the file name
name = input('Enter a file name:')
#fileH =open(name, 'r')
fileH =open(name)

# print out each line in a file
for line in fileH:
    line = line.rstrip()
    firstW = line [:line.find(' ')]
    lastW = line [line.rfind(' ')+1:]
    print (firstW, '\t', lastW)
'''
'''
totalW = 0
for line in fileH:
    line = line.rstrip()

    # break up the line into a list of words
    words = line.split()
    totalW = len(words) + totalW
    #firstW = line [:line.rfind(' ')]
    #lastW = line[line.rfind(' ')+1:]

    print(words)
'''
# create an output file containing 100 random integers between 5 and 10
# prompt for and read in the file name, and open the file for write
name = input('Enter the file name:')
fileW = open (name, 'w')
'''
# set up a while that iterates 100 times
count = 0
while count < 100:
    fileW.write( str (random.randint(5,10)))
    count = count + 1
'''
# set up a while that iterates 100 times
count = 0
while count < 100:
    fileW.write( str (random.randint(5,10) )+ '\n')
    count = count + 1
fileW.close()