dictionary = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
A = 2
result = 0 
for key in dictionary:
    if dictionary[key] == A:
        result = result + 1
print('The frequency of A is', result)
