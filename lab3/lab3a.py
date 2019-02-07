# Description: Write a python script that prompts the user for a whole 
#   number representing time in seconds, and converts that time from 
#   seconds to its equivalent time in hours, minutes, and seconds in 
#   the HH:MM:SS format.

# Output Heading
print('''
Programmer:     NAME
Course:         COSC 146, Winter 2019
Lab#            3, part #1
Due date:       2-6-19
''')

try:
    # ask user for time
    time = int(input('Enter time in seconds:'))

    # parse time from seconds into HH:MM:SS
    hours = time //3600
    minutes = (time % 3600)//60
    seconds = (time % 3600) % 60

    # print out time
    print(time, 'in seconds is: ', sep=" ", end="")

    if hours < 10:
        hours = '0' + str(hours)
    elif hours == 0:
        hours = '00'
    
    if minutes < 10:
        minutes = '0' + str(minutes)
    elif minutes == 0:
        minutes = '00'

    if seconds < 10:
        seconds = '0' + str(seconds)
    elif seconds == 0:
        seconds == '00'

    print(hours, minutes, seconds, sep=":", end="")

except:
    print('Time must be a whole number.')
    exit(0)

'''
PS D:\github\python-farms\lab3> python .\lab3a.py

Programmer:     NAME
Course:         COSC 146, Winter 2019
Lab#            3, part #1
Due date:       2-6-19

Enter time in seconds:18540
18540 in seconds is: 05:09:00
PS D:\github\python-farms\lab3> python .\lab3a.py

Programmer:     NAME
Course:         COSC 146, Winter 2019
Lab#            3, part #1
Due date:       2-6-19

Enter time in seconds:36012
36012 in seconds is: 10:00:12
PS D:\github\python-farms\lab3> python .\lab3a.py

Programmer:     NAME
Course:         COSC 146, Winter 2019
Lab#            3, part #1
Due date:       2-6-19

Enter time in seconds:7382
7382 in seconds is: 02:03:02
PS D:\github\python-farms\lab3> python .\lab3a.py

Programmer:     NAME
Course:         COSC 146, Winter 2019
Lab#            3, part #1
Due date:       2-6-19

Enter time in seconds:36610
36610 in seconds is: 10:10:10
PS D:\github\python-farms\lab3>
'''