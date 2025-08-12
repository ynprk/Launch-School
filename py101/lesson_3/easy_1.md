Practice Problems: Easy 1

Q1: Yes, the code will raise an IndexError as numbers has a length of 3, but we're trying to reassign the 7th element with numbers[6] = 5.

Q2: 
`
def ends_with_exclamation(s: str) -> bool:
    if s[len(s) - 1] == '!':
        return True
    else
        return False
    
    # return True if s[len(s) - 1] == '!' else False

    
ends_with_exclamation(s1)
ends_with_exclamation(s1)

# Or...
s1.endswith('!')
s2.endswith('!')

`

Q3:
# string concatenation
gettysburg = 'Four score and ' + famous_words

# string interpolation
gettysburg = f'Four score and {famous_words}'

Q4:
print(munsters_description.capitalize())

Q5:
print(munsters_description.swapcase())

Q6:
'Dino' in str1
'Dino' in str2

Q7:
flintstones.append('Dino')

Q8:
flintstones.extend(['Dino', 'Hoppy'])

Q9:
print(advice.split('house')[0])

Q10:
advice.replace('important', 'urgent')

---
string methods
str.endswith(suffix, start, end)
str.replace(old, new, count)

list methods
ls.append(element)
ls.extend(another_list)
ls.insert(element, index)

collection
value in sequence (membership testing)