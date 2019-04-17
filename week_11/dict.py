'''
# dictionary
# create empty dictionary
dic1 = {}
dic2 = dict()
print(dic1, '\t', dic2)

#create a phone book
phone = {'Tom':'487-2314', 'Ed':'434-2387', 'Kimmy':'879-4356'}
# output phonebook
for key in phone:
    print(key,'\t', phone[key])

try:
    # find someone's phone number
    if x in phone:
        print(phone[x])
    else:
        print('Name not found in phone book.')
except:
    print(Warning)


# add a new pair to the phone book
name = input('Enter a name: ')
number = input('Enter a phone number:')
phone[name] = number

# list values in dictionary
for number in list(phone.values()):
    print(number)

# list keys in dictionary
for name in list (phone.keys()):
    print(name)

# print dictionary in order
names = list(phone.keys())
names.sort()
for key in names:
    print(key,'\t', phone[key])

name = input ('Remove name from phone book:')
del phone[name]
print(phone)
'''
'''
# frequency of char occurance
#stringT = 'Here is a line of text'
stringT = input('Enter a string: ')

freq = {}

for x in stringT:
    if x in freq:
        freq[x.lower()] += 1
    else:
        freq[x.lower()] = 1

print('Frequency of Chars in String:\n'+ str(freq))

'''

'''
from collections import Counter
test_str = "LadyofPython"
res = Counter(test_str)
print(str(res))
'''
'''
test_str = "LadyofPython"
res = {}
for keys in test_str:
    res[keys] = res.get(keys, 0) + 1
print(str(res))
'''
test_str = "LadyofPython"
for char in test_str:
    freqq[char] = freqq.get(char,0) +1
print(freqq)

'''
test_str = "LadyofPython"
res = {i.lower() : test_str.count(i) for i in set(test_str)}
print(str(res))
'''