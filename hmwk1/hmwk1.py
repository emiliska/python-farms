# Description: Homework Assignment #1
'''
# Output Heading
#print(
#Programmer:     Emily
#Course:         COSC 146, Winter 2019
#Homework#       1
#Due date:       2-9-19
#)

#1. Write a print statement that displays the following phrase on the screen using a
#   double-quoted string (A string that begins and ends with a double quote), and do it
#   again using a single-quoted string (A string that begins and ends with a single quote).

print("Python is a good \"scripting\" language, and it's easy to learn")
print('Python is a good "scripting" language, and it\'s easy to learn')

#2. What does the following print statement display? (Be precise!)
#print (‘Question 2\n’ , 12+3)

# ANSWER: The print statement displays the following 

x = 12.765;
n = 3;
word = 'hello\n';
print ('x =%.2f\nn =%d\nword =%s' % (x, n, word))
print ('x ={0:.2f}\nn ={1:d}\nword ={2:s}'.format(x,n,word))
print ('{1:d}\t{2:s}\t{0:.1f}'.format(x,n,word))


num = 10
is_bigger = num < 3
if is_bigger:
 print ("Hello!")
print ("almost done! ")

for value in range (1, 50, 3):
 print (value)
 if value % 2 == 0:
    print (value , 'is even')
print ('that is al')
'''
try:
    num = float(input('Enter a number between 1.0 and 3.0: '))
    if num > 1.0 and num < 3.0:
        num += 10
        print(num)
    else:
        print('Error: Number is not in range.')
except:
    print('Error: Input must be a number.')
    exit(0)