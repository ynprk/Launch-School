# 1 Repeat Yourself
def repeat(word: str, count: int):
    for _ in range(count):
        print(word)

# repeat('Hello', 3)

# 2 ddaaiillyy ddoouubbllee
def crunch(text: str) -> str:
    if text == '':
        return ''
    
    result = text[0]
    for i in range(1, len(text)):
        if text[i] != text[i - 1]:
            result += text[i]

    return result

# These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

# 3 Bannerizer
def print_in_box(text: str):
    horizontal_row = f'+{"-" * (len(text) + 2)}+'
    empty_row = f'| {" " * len(text)} |'

    print(horizontal_row)
    print(empty_row)
    print(f'| {text} |')
    print(empty_row)
    print(horizontal_row)

# print_in_box('To boldly go where no one has gone before.')
# print_in_box('')

# 4 Stringy Strings
def stringy(num: int) -> str:
    result = ''
    for i in range(num):
        result += '1' if i % 2 == 0 else '0'
    return result

# print(stringy(6) == "101010")           # True
# print(stringy(9) == "101010101")        # True
# print(stringy(4) == "1010")             # True
# print(stringy(7) == "1010101")          # True

# 5 Right Triangles
def triangle(num: int):
    for i in range(num - 1, -1, -1):
        print(' ' * i + '*' * (num - i))

# triangle(5)
# triangle(9)

# 6 Madlibs
def madlibs():
    noun = input('Enter a noun: ')
    verb = input('Enter a verb: ')
    adj = input('Enter an adjective: ')
    adv = input('Enter an adverb: ')

    print(f"""\nDo you {verb} your {adj} {noun} {adv}? That's hilarious!
The {adj} {noun} {verb}s {adv} over the lazy {noun}.
The {noun} {adv} {verb}s up to Joe's {adj} turtle.""")
    
# madlibs()

# 7 Double Doubles
def twice(num: int) -> int:
    s = str(num)
    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]

    return num if left == right else num * 2

# print(twice(37) == 74)                  # True
# print(twice(44) == 44)                  # True
# print(twice(334433) == 668866)          # True
# print(twice(444) == 888)                # True
# print(twice(107) == 214)                # True
# print(twice(103103) == 103103)          # True
# print(twice(3333) == 3333)              # True
# print(twice(7676) == 7676)              # True

# 8 Grade Book
def get_grade(score1: int, score2: int, score3: int) -> str:
    avg = (score1 + score2 + score3) / 3
    if avg < 60:
        return 'F'
    elif avg < 70:
        return 'D'
    elif avg < 80:
        return 'C'
    elif avg < 90:
        return 'B'
    else:
        return 'A'

# print(get_grade(95, 90, 93) == "A")      # True
# print(get_grade(50, 50, 95) == "D")      # True
    
# 9 Clean up the words
def clean_up(text: str) -> str:
    result = ''
    for char in text:
        if char.isalpha():
            result += char
        elif result == '' or result[-1] != ' ':
                result += ' '
    return result

# print(clean_up("---what's my +*& line?") == " what s my line ")
# print(clean_up("    ") == " ")

# 10 What Century is That?
def century(year: int) -> str:
    num = (year - 1) // 100 + 1
    s_num = str(num)
    if num % 10 == 1 and num % 100 != 11:
        return s_num + 'st'
    elif num % 10 == 2 and num % 100 != 12:
        return s_num + 'nd'
    elif num % 10 == 3 and num % 100 != 13:
        return s_num + 'rd'
    else:
        return s_num + 'th'

# print(century(2000) == "20th")          # True
# print(century(2001) == "21st")          # True
# print(century(1965) == "20th")          # True
# print(century(256) == "3rd")            # True
# print(century(5) == "1st")              # True
# print(century(10103) == "102nd")        # True
# print(century(1052) == "11th")          # True
# print(century(1127) == "12th")          # True
# print(century(11201) == "113th")        # True
# print(century(111201) == "1113th")      # True
