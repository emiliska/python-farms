# content: explore writing to files
'''
# open a file to write to it
fout = open('ex.txt', 'w')

fout.write('This is another line.')

# close the open file
fout.close()


# create a data file containing numbers 1 through 10 each on a seprarate line

# ask the user to type in a flie name
name = input('Enter a file name:')

# open the file to write to it
fout = open(name, 'w')

for num in range(10):
    fout.write(str(num + 1)+ '\n')

fout.close()

while True:
    # ask the user for a file name
    name = input('Enter a file name: ')
    try:
        # open the file to read from it
        fin = open(name, 'r')
        for line in fin:
            print(line.rstrip())
        break
    except:
        print('File doesn\'t exist, TRY AGAIN LATER')
'''

# ask the user to type in a flie name
name = input('Enter a file name:')
sum = 0 

# open the file to write to it
fout = open(name, 'w')

# write numbers one through 10
for num in range(10):
    fout.write(str(num + 1)+ '\n')
    sum += int(num)
fout.write('Total: ' + str(sum))
print('Total: ' + str(sum))
# read the data file, add all the numbers in the file, 
#     and output the total

# fin = open(name)
total = 0
for line in fin:
    line = line.rstrip()
    total = total + int(line)
    print ('')


# close the file
fout.close()