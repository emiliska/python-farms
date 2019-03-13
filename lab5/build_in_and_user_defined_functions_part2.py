import random

print('''
Programmer: Emily Eubanks
Course:     COSC 146, Winter 2019
Lab#:       5, part #2
Due Date:   March 6, 2019
''')

# description: The goal of this project is to learn more about built-in f(x)

# 1. Write a function called 'roll_a_die1' that simulates rolling a 6-side die
#       This function takes no arg and returns a randome number b/w 1,6

def roll_a_die1():
    return random.randint(1,6)

# 2. Write a function call 'sum_of_rolls' that simlulates rolling of an n-
#       sided die 'm' times and returns the sum of all landings
def sum_of_rolls(m, n):
    i = 0 # counter var
    sum = 0 # sum of rolls vars
#       set a loop inside the function that iterates exactly m times
    while i < m+1:
#       and each time the loop generates a number between 1 and n
        result = random.randint(1, n)
#       prints that number out
        print(result, end=" ")
#       and also adds it to the running total
        sum += result
#       when the loop ends, return the running total
        i += 1
    return sum

# complete the script by writing a few lines of code that does the following:
#       roll the 6-side die 10 times and output the result each time
#       write a loop that iterates exactly 10 times and each time
#       through the loop call f(x) roll_a_die1 and output the value returned
print('Rolling a 6-sided die 10 times:')
for x in range(10):
    print(roll_a_die1(), end=" ")

print("\n")

# prompt for and read in the number of sides in a die, set up a loop that
# iterates exactly 10 times, each time through the loop function call 
# roll_a_die2 with the inputted value as its arg and print out value returned
n = int(input('Enter the number of sides: '))
m = int(input('Enter the number of rolls: '))
print('Rolling an ', n, '-sided die ', m, ' times:', sep="")
sum = sum_of_rolls(m, n)
print('\nSum of rolls =', sum)