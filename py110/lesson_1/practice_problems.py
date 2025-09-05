import pprint

# Problem 1
fruits = ("apple", "banana", "cherry", "date", "banana")
print(fruits.count("banana"))

# Problem 2
numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers)) # expect 5
print(numbers) # expect {1, 2, 3, 4, 5} in some order

# Problem 3
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
union = a | b
print(union)

# Problem 4
names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)

# The code creates a dictionary where the names are keys 
# and their positions in the original list are the values.

# Problems 5 & 6
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}
print(f'Sum: {sum(ages.values())}')
print(f'Min: {min(ages.values())}')

# Problem 7
words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words) # ['bear']

# Problem 8
statement = "The Flintstones Rock"
char_freq = {}
for ch in statement.replace(' ', ''):
    char_freq[ch] = char_freq.get(ch, 0) + 1
pprint.pp(char_freq)

# Problem 9
print([num for num in [1, 2, 3] if num > 1]) # [2, 3]

# Problem 10
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem()) # ('b', 'bear')
# removes and returns the last key-value pair as a tuple
# since dictionaries are "ordered" based on creation order
# as of Python 3.7, we know that 'b': 'bear' is the last pair.

# Problem 11
lst = [1, 2, 3, 4, 5]
print(lst[:2]) # [1, 2]
# equivalent to lst[0:2]
# returns a new list starting from 0th element (incl)
# and ending at 2nd element (excl)

# Problem 12
frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)

# We would get an AttributeError as we can't use the add method
# on a frozenset, as it is immutable.