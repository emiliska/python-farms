import random

print('''
Programmer: Emily Eubanks
Course:     COSC 146
Due date:   April 3, 2019
Lab#:       8, part 1
''')

playAgain = True

while playAgain:

    # create a list and fill it with n random whole numbers 10 - 100
    numList = []
    # the value of n is read from the keyboard
    n = int(input('How big is the list: '))

    # populate list n times with random numbers
    i = 0
    while n > i:
        numList.append(random.randint(10, 100))
        i += 1

    # output the elements of the list on the same line separated from each
    # other with a tab
    print('\nThe list contains: ')
    print(*numList, sep= '\t')

    # output the first and list list elements
    print('\nFirst and last elements are: ', numList[0], '\t', numList[-1], sep = '')

    # display the largest value in the list
    sortList = []
    for num in numList:
        sortList.append(num)
    sortList.sort(reverse=True)
    print('\nThe largest value is: ', sortList[0])

    # compute and display the average of all the numbers stored in the list
    sumList = 0
    for num in numList:
        sumList += num
    avgList = sumList/len(numList)
    print('\nAverage of the elements is: ', avgList)

    # list elements in descending order on the same line tab separated
    print('\nList elements in descending order are: ')
    print(*sortList, sep= '\t')

    # add 5 to every element of the original list and then print the list out
    fiveList = []
    for num in numList:
        fiveList.append(num+5)
    print('\nThe contents of the list after adding 5 to each element:')
    print(*fiveList, sep='\t')

    # add the following three numbers into the current list at the specified
    #     positions and then output the list.
    fiveList.insert(0, 1) # 1 at the beginning
    fiveList.append(2) # 2 at the end
    fiveList.insert(3, 5) # 5 at index position [3]
    print('\nThe contents of the list after adding 1, 2, and 5:')
    print(*fiveList, sep='\t')

    # delete the first four elements as well as the last element from the list
    #      and then print the list out
    del fiveList[:4]
    fiveList.pop()
    print('\nList after removing the first 4 and last elements:')
    print(*fiveList, sep='\t')

    # ask user to repeat
    repeat = input('\nDo it again? (yes or no):')
    while True:
        if repeat.lower() == 'yes':
            playAgain = True
            print()
            break
        elif repeat.lower() == 'no':
            playAgain = False
            print()
            break
        else:
            repeat = input('\nYou must answer \'yes\' or \'no\': ')

'''
PS D:\github\python-farms\project_8> python .\script.py

Programmer: Emily Eubanks
Course:     COSC 146
Due date:   April 3, 2019
Lab#:       8, part 1

How big is the list: 10

The list contains:
11      61      88      17      18      48      84      53
59      45

First and last elements are: 11 45

The largest value is:  88

Average of the elements is:  48.4

List elements in descending order are:
88      84      61      59      53      48      45      18
17      11

The contents of the list after adding 5 to each element:
16      66      93      22      23      53      89      58
64      50

The contents of the list after adding 1, 2, and 5:
1       16      66      5       93      22      23      53
89      58      64      50      2

List after removing the first 4 and last elements:
93      22      23      53      89      58      64      50

Do it again? (yes or no):j

You must answer 'yes' or 'no': yes

How big is the list: 10

The list contains:
60      26      37      58      22      33      68      100
32      12

First and last elements are: 60 12

The largest value is:  100

Average of the elements is:  44.8

List elements in descending order are:
100     68      60      58      37      33      32      26
22      12

The contents of the list after adding 5 to each element:
65      31      42      63      27      38      73      105
37      17

The contents of the list after adding 1, 2, and 5:
1       65      31      5       42      63      27      38
73      105     37      17      2

List after removing the first 4 and last elements:
42      63      27      38      73      105     37      17

Do it again? (yes or no):no

PS D:\github\python-farms\project_8>
'''