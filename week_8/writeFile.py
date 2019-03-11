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
'''
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
    # 