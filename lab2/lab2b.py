# Description: The purpose of this Car Salesman program is to use a python script to generate an invoice.

# Output Heading
print('''
Programmer:     NAME
Course:         COSC 146, Winter 2019
Lab#            2, part #1
Due date:       2-4-19
''')

# ask user to enter the base price of the car

base_price = float(input('Enter the base price of the car: $'))

# calculate additional fees
tax = base_price * 0.06
carLicense = base_price * 0.005 # note license is reserved word
destination = 700
documentation = 200
dealerPrep = 50

# calculate cost
price = base_price + tax + carLicense + destination + documentation + dealerPrep

# format invoice
print('\nVehicle Base Price..........................', "${:.2f}".format(base_price))
print('Destination Charge..........................', "${:.2f}".format(destination))
print('Documentation...............................', "${:.2f}".format(documentation))
print('Prep........................................', "${:.2f}".format(dealerPrep))
print('License Plate...............................', "${:.2f}".format(carLicense))
print('Tax.........................................', "${:.2f}".format(tax), '\n')
print('Total.......................................', "${:.2f}".format(price))

'''
PS D:\github\python-farms\lab2> python .\lab2b.py

Programmer:     NAME
Course:         COSC 146, Winter 2019
Lab#            2, part #1
Due date:       2-4-19

Enter the base price of the car: $18375.00

Vehicle Base Price.......................... $18375.00
Destination Charge.......................... $700.00
Documentation............................... $200.00
Prep........................................ $50.00
License Plate............................... $91.88
Tax......................................... $1102.50

Total....................................... $20519.38
PS D:\github\python-farms\lab2>
'''