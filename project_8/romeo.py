import io

print('''
Programmer: Emily Eubanks
Course:     COSC 146
Due date:   April 3, 2019
Lab#:       8, part 2
''')

shakespere = open("./romeo.txt", 'r')
totalW = 0
for line in shakespere:
    line = line.rstrip()
    # break up the line into a list of words
    words = line.split()
    print(words)

print('Distinct words in \'romeo.txt\':')