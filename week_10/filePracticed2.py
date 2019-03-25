# prompt for and read in the file name
name = input('Enter a file name:')
#fileH =open(name, 'r')
fileH =open(name)
'''
# print out each line in a file
for line in fileH:
    line = line.rstrip()
    firstW = line [:line.find(' ')]
    lastW = line [line.rfind(' ')+1:]
    print (firstW, '\t', lastW)

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

    