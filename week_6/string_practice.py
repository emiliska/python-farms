# ask user to type a phrase

phrase = input('Enter a phrase:')
'''
#print the last character of the phrase
phrase_length = len(phrase)
print(phrase[phrase_length-1])

#print the last character of the phrase
print(phrase[-1])

# use a while loop to traverse the string
loop_var = 0 # controlling the loop
count = 0 # counting number of blanks
while loop_var < phrase_length:
    if phrase[loop_var] == " ":
        count = count + 1
    loop_var = loop_var + 1

print('There are', count, 'blanks in phrase')

# use a while-loop to traverse the string
loop_var = 0 # controlling the loop
count = 0 # counting number of blanks
for char in phrase:
    if char == ' ':
        count = count + 1
    loop_var = loop_var + 1
print('There are', count, 'blanks in phrase')


# return the length of the string
def length (myString):
    count = 0
    for char in myString:
        count = count + 1
    return count

print(length(phrase))


print(phrase.upper())


print(phrase.find('is'))

print(phrase.find('is',3))

print(phrase.replace(' ', ':'))


print(phrase[2:7])
print(phrase[2:])
print(phrase[:7])

'''

#encode
for char in phrase:
    # print (char, 'its ASCII code', ord(char))
    value =ord(char)
    print(chr(value+5), end=' ')

print()

phrase = input('Enter a phrase:')
#decode
for char in phrase:
    # print (char, 'its ASCII code', ord(char))
    value =ord(char)
    print(chr(value-5), end=' ')