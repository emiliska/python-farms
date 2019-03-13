import random 

print('''
Programmer: Emily Eubanks
Course:     COSC 146, Winter 2019
Lab#:       5, part #1
Due Date:   March 6, 2019
''')

# 1. Write a script that simulates the flipping of a coin several
#       times to see how often it comes up heads or tails. Follow
#       the steps below to complete this task.

# define two variables named 'headCount' and 'tailCount' and 
#       initialize them to zero
headCount = 0
tailCount = 0
i = 0 # initialize counter var

# ask the user to type in the number of flips and store that number
#       into a variable 'flips'
flips = int(input('Enter the number of flips: '))

# set up a loop where the body of the loop will execute exactly
#       'flips' times and each time do the following:

while i < flips:
#       (1) generate a random number betwen 0 and 1 using random()
#           assume that a number less that 0.5 represents a tail
#           a number bigger than or equal to 0.5 represents heads
#       (2) increment 'tailCount' by 1 if random number is less 
#           than 0.5. Otherwise, increment 'headcount' by 1.
#           output the numbers of heads (headCount) and the number 
#           of tails 'tailCount' when the loop ends
    outcome = random.random()
    if outcome < 0.5:
        tailCount += 1
        outcome2 = "tails"
    else:
        headCount += 1
        outcome2 = "heads"
    i += 1
print('Number of heads:', headCount)
print('Number of tails:', tailCount)

# 2. Write a function called ‘coin_flip’ that takes the number of flips 
# as an argument. The function computes the number of heads and tails, 
# and returns those values back (Use the function randint() to generate 
# your random numbers). Place this function at the beginning of your 
# current script.

# Add a couple of line of code at the bottom of the script to read the
#   number of flips and then call the function 'coin_flip' to get the
#   number of heads and tails, and print them out.

# --