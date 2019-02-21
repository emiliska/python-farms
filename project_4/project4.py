# define a function that display the output heading
def output_heading():
    print('Programmer:        Emily Eubanks')
    print('Course:            COSC146, Winter 2019')
    print('Lab#:              4')
    print('Due Date:          Feb. 20, 2019')

repeat = True # initalize while loop
output_heading() # print heading

# try again loop
while repeat:

    # create and set variables
    try:
        print()
        x = int(input('Enter a whole number: '))
        i = 1 # initialize count variable
        sumofNums = 0 # initialize sumofNums
        print()

    except:
        print('Error: You must enter a whole number. \n Exit Program.')
        exit(0)

    # 1 Output all of the numbers from 1 thourgh the given number
    #       with a couple of space between them (while-loop)

    print('Numbers from 1 through ', x,' are:', sep="")
    while i < (x + 1):
        print(i, end="  ")
        i += 1
    i = 1 # reset variable
    print(' ', end='\n')
    print()

    # 2 Output all odd numbers between 1 and the given number
    #      starts at 1, ends with odd number less than or equal to given
    #      (for-loop); do this with range()
    print('Odd numbers from 1 through ', x,' are:', sep="")
    for j in range(1, x+1, 2):
        print(j, end="  ")

    print('', end='\n')

    # 3 output every multiple of four b/w given number and 1
    # output will start with first multiple of four less than or equal to the
    # given number (for-loop)
    print('\nMultiple of fours from 1 ', x,' are:', sep="")
    for j in range(1, x+1):
        if (j % 4 == 0):
            print(j, end="  ")

    print('', end='\n')
    print()

    # 4 output the sum of all the even numbers from 1 through the given
    #       number (while-loop)
    
    print('Sum of even numbers from ', x,' are:', sep="")
    while i < (x + 1):
        if (i % 2 == 0):
            sumofNums = sumofNums + i
        i += 1
    print(sumofNums)
    
    print()

    # 5 output all of the numbers from 1 through the given number 
    #      display 5 numbers per line (using a single loop)
    #      (if-statement) used inside the loop
    i = 1
    print('Numbers from 1 through ', x,' (5 numbers per line):', sep="")
    (5 numbers per line)')
    while i < (x + 1):
        if (i % 5 == 0):    
            print(i, end="\n")
        else:
            print(i, end="\t")
        i += 1
    print()
    print()

    # check to see if the user want to repeat the program
    while True:
        checkUserRepeat = input('Do it again (yes or no)? ')
        if checkUserRepeat == 'yes':
            repeat=True
            break
        elif checkUserRepeat == 'no':
            repeat=False
            break
        else:
            print('You must enter yes or no')
            exit(0)
'''
OUTPUT
PS D:\github\python-farms\project_4> python .\project4.py
Programmer:        Emily Eubanks
Course:            COSC146, Winter 2019
Lab#:              4
Due Date:          Feb. 20, 2019

Enter a whole number: 17

Numbers from 1 through 17 are:
1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17

Odd numbers from 1 through 17 are:
1  3  5  7  9  11  13  15  17

Multiple of fours from 17 through 1 are:
4  8  12  16

Sum of even numbers from 1 through 17 is:
72

Numbers from 1 through 17 (5 numbers per line)
1       2       3       4       5
6       7       8       9       10
11      12      13      14      15
16      17

Do it again (yes or no)? yes

Enter a whole number: 10

Numbers from 1 through 17 are:


Odd numbers from 1 through 17 are:
1  3  5  7  9

Multiple of fours from 17 through 1 are:
4  8

Sum of even numbers from 1 through 17 is:
102

Numbers from 1 through 17 (5 numbers per line)
1       2       3       4       5
6       7       8       9       10


Do it again (yes or no)? no
PS D:\github\python-farms\project_4>
'''