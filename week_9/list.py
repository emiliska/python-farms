list1 = []
list2 = ()
list3 = list("Hello")
print(list1, list2, list3)

numbers = [1, 5, 10, 100, 18]
strings = ['Toyota', 'Honda', 'BMW', 'Chevy', 'Ford']
mixed = ['Tom', 12, 2.86, 'A']
nested = ['Hello', [2, 100], 12, 'a']
print(numbers)
print(strings)
print(mixed)

temp = [strings, 11, 12]
print(temp)

print(len(nested))

# access list elements

print(strings[2])
print(strings[:3])

# traversing a list
for elm in mixed:
    print(elm)

# output list elements that are in odd positions
for pos in range(5):
    if pos % 2 == 1:
        print(numbers[pos])

# do something with a while-loop
pos = 0
while pos < 5:
    if pos % 2 == 1:
        print(numbers[pos])
    pos += 1

# list build-in functions: len, max, min, sum
numbers = [1,2,3,4,10,50,5,6,100,20]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))