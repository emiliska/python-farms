# define a function that display the output heading
def output_heading():
    print('Programmer:        Emily')
    print('Course:            COSC146')
    print('Lab#:              0')
    print('Due Date:          02-19-2019')

#define a function that takes a number and returns that number + 10
def plus10(value):
    value = value + 10
    return value

#call function print_heading
output_heading()

#call function plus10
print(plus10(1000))

# define a function that takes in two parameters and return their sum
def sumoftwo(x, y):
    return x + y

print(sumoftwo(5,10))
print(sumoftwo('lil','phil'))