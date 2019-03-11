# topic: text files: reading from and writing to text files.

# description

# open the file
fin = open('ex.txt')

'''
# read 6 characters from 'today.txt'
text = fin.read(6)
print(text)

print(fin.read(4))

# read a whole line
print(fin.readline())
print(fin.readline())

print(fin.readline().rstrip())


# read datafile line by line
for line in fin:
    line = line.strip()
    if line.find('This') != -1:
        line = line.upper()
    print(line)


# read entire file into a string
mydata = fin.read()
print(mydata.rstrip())

# read entire file into a list of lines
myList=fin.readlines()
print(myList)
'''

# read a data file specific at the keyboard

# ask the user for the file name
name = input('Enter a file name: ')

# open the file for input
fin = open(name)

# echo the contents of the file by reading it line-by-line
for line in fin:
    print(line.rstrip())