print('''
Programmer: Emily Eubanks
Course:     COSC 146
Lab#:       Candy
Due date:   4/17/2019
''')

# open the packet
# count the candies in each packet
# move each candy from bigger packets to smaller ones

while True:
    try: # input file
        inFile = input('Enter a filename: ')
        break
    except:
        inFile = input('File invalid. Try Again: ')

# open the file for reading
fileHandle = open(inFile, 'r')

# read in the number of candies per bag
lines=[]
for line in fileHandle:
    line = line.rstrip()
    lines.append(line)
lines.pop()# remove end of file delimiter

# turn list into dictionary
bags = {}
packets = []
count = 0
lastBag = 0
for line in lines:
    if count%2==0:
        bags[line]= line
        lastBag = line
    else:
        bags[lastBag] = line 
    count += 1

for key, value in bags.items():
    packets = value.split(" ")
    # check if the sum of the packets are divisible by the key
    sumPackets = 0
    evenSplit = 0

    for packet in packets:
        sumPackets += int(packet)

    if sumPackets % int(key) == 0:
        evenSplit = int(sumPackets/int(key)) # what each bag gets
        cppackets = sorted(packets, reverse = True)
        #print('cppackets', cppackets)
        
        i = 0
        for packet in cppackets:    
            packet = int(packet)
            #print('packet', packet)
            diffpacket = evenSplit - int(packet)
            if packet > evenSplit:
                # if the packet has more than what is fair
                newpacket = int(packet) - diffpacket
                #print('newpacket', newpacket)
                i += 1 # note that a change has been made
            elif packet < evenSplit:
                # if the packet has less than what is fair
                newpacket = int(packet) + diffpacket
                #print('newpacket', newpacket)
                i += 1 # note that a change has been made
            else: # the packets are the same
                break
                #print('These packets are the same')
        print(i)
    else: # can't be evenly distributed
        print('-1')

'''
OUTPUT:
PS D:\EMU\python> python .\candy.py

Programmer: Emily Eubanks
Course:     COSC 146
Lab#:       Candy
Due date:   4/17/2019

Enter a filename: candy1.txt
5
-1
PS D:\EMU\python> python .\candy.py

Programmer: Emily Eubanks
Course:     COSC 146
Lab#:       Candy
Due date:   4/17/2019

Enter a filename: candy2.txt
0
-1
-1
Traceback (most recent call last):
  File ".\candy.py", line 51, in <module>
    if sumPackets % int(key) == 0:
ValueError: invalid literal for int() with base 10: '23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42'
PS D:\EMU\python>
'''