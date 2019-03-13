# help(str.rfind)

# description: The goal of this project is to learn more about strings
#           and how to manipulate strings using string operations, string
#           functions, and string methods
print('''
Programmer: Emily Eubanks
Course:     COSC 146, Winter 2019
Lab#:       6
Due date:   March 13, 2019
''')
while True:
    # Write a script that prompts for and reads in a phrase from the keyboard
    phrase = input('Enter a phrase: ')
    #        and then does the following:

    # prints out the first char, the last char, and the num of chars in the phrase

    print('First=', phrase[0],'\tLast=', phrase[len(phrase)-1],'\tlength=', len(phrase))

    # prints out the phrase twice in a row on the same line with no blanks in between
    print('\nPhrase printed twice:')
    print(phrase.upper(), phrase.lower(), sep="")

    # prints out how many blanks there are in the phrase
    print('\nNumber of blanks in the phrase:', phrase.count(" "))

    # prints out the phrase where every occurrence of the word 'the' has been
    #       replaced with 'THE'
    print('\nWord \'the\' is replace with \'THE\':')
    print(phrase.replace('the', 'THE'))

    # prints out the phrase where the last word is capatalized if it is made up
    #       of more than three letters. Otherwise, prints out the original phrase
    print('\nCapatalize the last word, if>3:')
    #       use rfind() to find pos of right most blank in phrase
    #       use string slice operator and pos of last blank to break up phrase
    #       into two parts
    phrase_part1 = phrase[0:phrase.rfind(" ")]
    phrase_part2 = phrase[phrase.rfind(" "):len(phrase)]
    #       capatalize the last word if it has more than 3 chars
    if len(phrase_part2)-1>3:
        phrase_part2 = phrase_part2.upper()
    #       combine the first part and the second part back into one string and print
    newPhrase = phrase_part1 + phrase_part2
    print(newPhrase)

    # encrypts the phrase by performing character substitutions and prints out
    #       the encrypted phrase
    #       write a function called 'encrypt' that takes a string as an arg
    #       encrypts the string using char substitution
    #       and returns the encrypted string
    #       this function does not print anything
    #       this function does not modify the argument
    #       the function creates a new string where each char in this string is
    #               distance 4 away from the corresponding char (char in same pos)
    #       EX: input: ABC output: EFG
    def encrypt(m):
    #       encrypts the string using char substitution
        encodedStr = "" #initalize newPhrase
        for char in m:
            value = ord(char)
            value =chr(value+4)
            encodedStr = encodedStr + value
    #       and returns the encrypted string
        return encodedStr

    # call function encrypt with the inputted phrase as its arg and then 
    # print returned value, an encrypted string
    print('\nEncrypted phrase:')
    print(encrypt(phrase))

    # add a loop to your scrip that allows the user to repeat the above 
    # steps as often as she wishes
    userRepeat = input('\nDo it again, (yes or no)? ')
    if userRepeat.lower() == 'no':
        break
    elif not userRepeat.lower() == 'yes':
        print('Error: User must enter \'yes\' or \'no\'.')
    print()

'''
OUTPUT:
PS D:\github\python-farms\project_6> python .\manipulatingStrings.py

Programmer: Emily Eubanks
Course:     COSC 146, Winter 2019
Lab#:       6
Due date:   March 13, 2019

Enter a phrase: This is a test!
First= T        Last= !         length= 15

Phrase printed twice:
THIS IS A TEST!this is a test!

Number of blanks in the phrase: 3

Word 'the' is replace with 'THE':
This is a test!

Capatalize the last word, if>3:
This is a TEST!

Encrypted phrase:
Xlmw$mw$e$xiwx%

Do it again, (yes or no)? yes

Enter a phrase: the fat cat sat on the mat
First= t        Last= t         length= 26

Phrase printed twice:
THE FAT CAT SAT ON THE MATthe fat cat sat on the mat

Number of blanks in the phrase: 6

Word 'the' is replace with 'THE':
THE fat cat sat on THE mat

Capatalize the last word, if>3:
the fat cat sat on the mat

Encrypted phrase:
xli$jex$gex$wex$sr$xli$qex

Do it again, (yes or no)? no
PS D:\github\python-farms\project_6>
'''