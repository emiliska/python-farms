'''
# dictionary
# create empty dictionary
dic1 = {}
dic2 = dict()
print(dic1, '\t', dic2)
'''
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

'''
# add a new pair to the phone book
name = input('Enter a name: ')
number = input('Enter a phone number:')
phone[name] = number
'''
