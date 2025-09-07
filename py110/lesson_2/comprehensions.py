import random

# Problem 1
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# Using a loop
total_age = 0
for info in munsters.values():
    if info['gender'] == 'male':
        total_age += info['age']
print(total_age)

# Using a comprehension
all_ages = [info['age'] for info in munsters.values()
                            if info['gender'] == 'male']
print(sum(all_ages))

# Problem 2
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Manually
a = sorted(lst[0])
b = sorted(lst[1])
c = sorted(lst[2])
print([a, b, c])

# Using a loop
new_list = []
for sublist in lst:
    new_list.append(sorted(sublist))
print(new_list)

# Using a comprehension
new_list2 = [sorted(sublist) for sublist in lst]
print(new_list2)

# Problem 3
# Using a loop
new_list = []
for sublist in lst:
    new_list.append(sorted(sublist, key=str))
print(new_list)

#Using a comprehension
new_list2 = [sorted(sublist, key=str) for sublist in lst]
print(new_list2)

# Problem 4
lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

# Using a comprehension
d = {item[0]: item[1] for item in lst}
print(d)

# Using the dict constructor function
print(dict(lst))

# Problem 5
def total_odds(lst):
    return sum([ele for ele in lst if ele % 2 != 0])

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
new_list = sorted(lst, key=total_odds)
print(new_list)

# Problem 6
def increment_values(d):
    return {key: value + 1 for key, value in d.items()}

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
new_list = [increment_values(d) for d in lst]
print(new_list)

# one-liner
new_list = [{key: value + 1 for key, value in dictionary.items()}
                            for dictionary in lst]
print(new_list)

# Problem 7
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

new_list = []

for sublist in lst:
    new_sublist = []
    for num in sublist:
        if num % 3 == 0:
            new_sublist.append(num)
    new_list.append(new_sublist)

print(new_list)

def divisible_by_three(lst):
    return [ele for ele in lst if ele % 3 == 0]

new_list = [divisible_by_three(sublist) for sublist in lst]
print(new_list)

# one liner
new_list = [[ele for ele in sublist if ele % 3 == 0] 
            for sublist in lst]
print(new_list)

# Problem 8
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def transform(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    elif item['type'] == 'vegetable':
        return item['size'].upper()

lst = [transform(item) for item in dict1.values()]
print(lst)

# Problem 9
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def contains_all_evens(d):
    for values in d.values():
        for num in values:
            if num % 2 != 0:
                return False
    return True

evens = [d for d in lst if contains_all_evens(d)]
print(evens)

# Problem 10
def generate_uuid():
    chars = 'abcdef0123456789'
    sections = [8, 4, 4, 4, 12]
    uuid = []

    for section in sections:
        uuid.append(''.join([random.choice(chars) for _ in range(section)]))
    
    return '-'.join(uuid)

print(generate_uuid())

# Problem 11
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

lst = []
for value in dict1.values():
    for word in value:
        for char in word:
            if char in 'aeiou':
                lst.append(char)
print(lst)

list_of_vowels = [char for value in dict1.values()
                  for word in value
                  for char in word if char in 'aeiou']

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']