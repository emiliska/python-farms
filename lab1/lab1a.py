# Triple-quoted string to output personal information
print('Programmer: NAME', 'Course:     COSC146, Winter 2019', 'Lab#:       1, part#1', 'Due date:   1-16-2019', sep='\n')

# Print "Roses are Red" to console
print('\nRoses are Red\n')

# Print Poem with Border
border = '+++++++++++++++++++++++++++'
poem   = '+  Roses are red          +\n+  Violets are blue       +\n+  "Chocolate" is better  +\n+ By a \'pound\' or two!!   +' 
display = border + '\n' + poem + '\n' + border
print(display)

# Replace '+' with '/'
print('\n', display.replace("+", "\\"), '\n', sep="")