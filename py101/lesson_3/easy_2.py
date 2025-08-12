# Q1
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
reversed_numbers1 = numbers[::-1]
reversed_numbers2 = list(reversed(numbers))

# numbers.reverse() mutates the list

# Q2
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)
print(number2 in numbers)

# Q3
# range includes the start value but excludes the end value
42 in range(10, 101)
100 in range(10, 101)
101 in range(10, 101)

# Q4
numbers = [1, 2, 3, 4, 5]

# using the pop method
numbers.pop(2)

# using the del keyword
del numbers[2]

# removing the value 3 w/ the remove method
numbers.remove(3)

# Q5
#preferred solution
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
isinstance(numbers, list)
isinstance(table, list)

# this works too, but has potential issues
type(numbers) is list
type(table) is list

# type() is strict identity
# isintance() respects inheritance
# usually isintance() is more flexible and usually preferred

# Q6
title = "Flintstone Family Members"
centered_title = title.center(40)

#str.center(width[, fillchar])

# Centering with default space padding
s1 = "hello"
s2 = s1.center(15)
print(s2)

# Centering with a custom fill character
s3 = "Python"
s4 = s3.center(20, '-')
print(s4)

# Output
#      hello     
# -------Python-------

# Q7
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

statement1.count('t')
statement2.count('t')

# Q8
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
ages.get('Spot')
'Spot' in ages

# Q9
additional_ages = {'Marilyn': 22, 'Spot': 237}
ages.update(additional_ages)



