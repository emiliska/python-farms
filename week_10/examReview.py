'''
def vowels (s):
    count = 0
    for char in s:
        lChar = char.lower()
        if (lChar =='a' or lChar =='e' or lChar =='i' or lChar =='o' or lChar =='u'):
            count += 1
    return count

string = input('Enter a line of text:')

print('Number of vowels', vowels(string))
'''
'''
def vowels (s):
    count = 0
    myVowels = ['a','e','i','o','u']
    for char in s:
        if char.lower() in myVowels:
            count += 1
    return count

string = input('Enter a line of text:')

print('Number of vowels', vowels(string))
'''
'''
def vowels (s):
    count = 0
    myVowels = ['a','e','i','o','u']
    for char in s.lower():
        if char in myVowels:
            count += 1
    return count

string = input('Enter a line of text:')

print('Number of vowels', vowels(string))
'''

