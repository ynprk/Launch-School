# numbers = [1, 2, 3, 4]
# numbers[0] = numbers[0] + 1
# print(numbers)

# for i in range(1, 4):
#     numbers[i] += 1

# print(numbers)

# colors = ["red", "blue", "green"]
# for color in colors:
#     color += "s"

# print(colors)

def sum_factors(target: int, factors: list[int]) -> int:
    if len(factors) == 0:
        factors = [3, 5]
    
    result = set()
    for factor in factors:
        result.update(range(factor, target, factor))
    
    return sum(result)

print(sum_factors(20, [3,5]))

dict1 = {
'apple': 'Produce',
'carrot': 'Produce',
 'pear': 'Produce',
 'broccoli': 'Produce',
}

word = "hello"
letter_counts = {}
for letter in word:
    letter_counts.setdefault(letter, 0)
    letter_counts[letter] += 1

print(letter_counts)

for letter in word:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1

print(letter_counts)

words = ['apple', 'ant', 'banana', 'bat', 'cat', 'car']
grouped_words = {}

# for word in words:
#     first_letter = word[0]
#     # If first_letter is not a key, set it to an empty list.
#     # Then, get the list (either the new empty one or the existing one).
#     word_list = grouped_words.setdefault(first_letter, [])
#     word_list.append(word)

# print(grouped_words)

for word in words:
    first_letter = word[0]
    # If first_letter is not a key, set it to an empty list.
    # Then, get the list (either the new empty one or the existing one).
    word_list = grouped_words.get(first_letter, [])
    word_list.append(word)
    grouped_words[first_letter] = word_list

print(grouped_words)


def change_me(s: str) -> str:
    words = s.split()
    new_words = []

    for word in words:
        if word == word[::-1]:
            new_words.append(word.upper())
        else:
            new_words.append(word)

    return ' '.join(new_words)

# Comments show expected return values
print(change_me("We will meet at noon"))       # "We will meet at NOON"
print(change_me("No palindromes here"))        # "No palindromes here"
print(change_me(""))                           # ""
print(change_me("I LOVE mom and dad equally")) # "I LOVE MOM and DAD equally"

"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.

Input: string
Output: list of strings

Rules:
- Given a string, return all substrings (size >= 2) that are palindromes
- Case sensitive (e.g. Dad is not a palindrome)

Questions:
- can a string contain whitespace? for example, is "ab  ba" a palindrome?
"""

def substrings(string):
    result = []
    start_index = 0

    while start_index <= len(string) - 2:
        num_chars = 2
        while num_chars <= len(string) - start_index:
            substring = string[start_index:start_index + num_chars]
            result.append(substring)
            num_chars += 1

        start_index += 1

    return result

def is_palindrome(string):
    reversed_string = string[::-1]
    if reversed_string == string:
        return True
    else:
        return False

def palindrome_substrings(s):
    result = []
    substrings_list = substrings(s)

    for substring in substrings_list:
        if is_palindrome(substring):
            result.append(substring)

    return result

print(palindrome_substrings("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
print(palindrome_substrings("palindrome")) # []
print(palindrome_substrings(""))           # []
print(palindrome_substrings("repaper"))
# ['repaper', 'epape', 'pap']

print(palindrome_substrings("supercalifragilisticexpialidocious"))
# ["ili"]
print(palindrome_substrings("abb  bba"))