# list methods

# add new elemts to a list
numbers = [1,2,3,4,10,50,5,6,100,20]
# add to the end
numbers = numbers + [3]

print(numbers)

numbers.append(1000)
print(numbers)

#numbers.insert(2000, 12)
numbers.insert(len(numbers), 2000)
print(numbers)

numbers.insert(0, -125)
print(numbers)

# delete a list element(s)
print(numbers.pop())
print(numbers)

numbers.remove(100)
print(numbers)

del numbers[5]
print(numbers)

del numbers [:5]
print(numbers)

# order a list in ascending order
copy = numbers[:]
numbers.sort()
print(numbers)

# order a list in descending order
copy.sort(reverse = True)
print(copy)