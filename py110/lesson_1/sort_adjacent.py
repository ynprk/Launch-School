"""
Sort Strings by Most Adjacent Consonants

Given a list of strings, sort the list based on the highest number of 
adjacent consonants a string contains and return the sorted list. 
If two strings contain the same highest number of adjacent consonants, 
they should retain their original order in relation to each other. 
Consonants are considered adjacent if they are next to each other in the same word 
or if there is a space between two consonants in adjacent words.

Tasks
You are provided with the problem description above. Your tasks for this step are:

Make notes of your mental model for the problem, including:
inputs and outputs.
explicit and implicit rules.
Write a list of clarifying questions for anything that isn't clear.

input: list of strings
output: sorted list of strings, based on highest number of adjacent consonants

explicit:
- If two strings contain the same highest number of adjacent consonants, 
they should retain their original order in relation to each other. 
- Consonants are considered adjacent if they are next to each other in the same word 
or if there is a space between two consonants in adjacent words.
    e.g. the two 'r's in 'for real' are adjacent 

implicit:
- strings can contain whitespace

questions:
1) sort in place or return a new list?
2) can I treat all 'y's as consonants?
3) can I assume the input strings will contain only spaces and alphabetic chars?
    or can they contain digits, for instance?
4) case sensitivity?
5) ascending or descending? descending

data structure:
i/o both lists, so a list should be useful
iterate through list

maybe a dictionary to keep track of # of adj consonants in each word
e.g. {'aa': 0, 'baa': 0}

1) iterate through list
2) for each string:
    - calculate the number of highest adj consonants
3) 

"""

# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# # ['dddaa', 'ccaa', 'aa', 'baa']

# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

# my_list = ['day', 'week', 'month', 'year']
# print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

# my_list = ['xxxa', 'xxxx', 'xxxb']
# print(sort_by_consonant_count(my_list))
# # ['xxxx', 'xxxb', 'xxxa']

"""
1. For each string in the input list, determine the highest number
   of adjacent consonants within that string.
2. Sort the input list based on the calculated highest number of
   consonants from step 1.
3. Return the sorted list.

- Remove the spaces from the "input string".
- Initialize a "maximum consonants count" to zero.
- Initialize an "adjacent consonants string" to an empty string.
- For each "letter" in the "input string":
    - If the "letter" is a consonant:
        - Concatenate it to the "adjacent consonants string".
    - If the "letter" is a vowel:
        - If the "adjacent consonants string" has a length
          greater than the current "maximum consonants count":
            - If the "adjacent consonants string" has a length
              greater than 1:
                - Set the "maximum consonants count" to the length
                  of the "adjacent consonants string".

        - Reset the "adjacent consonants string" to an empty string.

- Return the "maximum consonants count".
"""
def count_max_adjacent_consonants(s):
    s = ''.join(s.split())
    max_run = 0
    run = 0

    for c in s:
        if c not in 'aeiou':
            run += 1
            if run > 1:
                max_run = max(max_run, run)
        else:
            run = 0

    return max_run


def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']


# print(count_max_adjacent_consonants('  ddd  aa')) 
# print(count_max_adjacent_consonants('dddaa'))       # 3
# print(count_max_adjacent_consonants('ccaa'))        # 2
# print(count_max_adjacent_consonants('baa'))         # 0
# print(count_max_adjacent_consonants('aa'))          # 0
# print(count_max_adjacent_consonants('rstafgdjecc')) # 4