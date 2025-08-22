import random
from datetime import datetime

# 1 Welcome Stranger
def greetings(names: list, titles: dict) -> str:
    return (
        f'Hello, {" ".join(names)}! Nice to have a ' 
        f'{titles["title"]} {titles["occupation"]} around.'
    )

# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )
# print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

# 2 Greeting a user
def greet():
    name = input('What is your name? ')
    if name.endswith('!'):
        print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
    else:
        print(f'Hello {name.capitalize()}.')

# greet()

# 3 Multiplying Two Numbers
def multiply(a, b):
    return a * b

# print(multiply(5, 3) == 15)  # True
# print(multiply('abc', 3) == 'abcabcabc')

# 4 Squaring an Argument
def square(num):
    return multiply(num, num)

# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

# 5 Floating Point Arithmetic
def prompt(message: str):
    print(f'==> {message}')

def perform_arithmetic():
    prompt('Enter the first number:')
    num1 = float(input())

    prompt('Enter the second number:')
    num2 = float(input())

    operations = ['+', '-', '*', '/', '//', '%', '**']
    for operation in operations:
        prompt(f'{num1} {operation} {num2} = {eval(f"{num1} {operation} {num2}")}')

    # prompt(f'{num1} + {num2} = {num1 + num2}')
    # prompt(f'{num1} - {num2} = {num1 - num2}')
    # prompt(f'{num1} * {num2} = {num1 * num2}')
    # prompt(f'{num1} / {num2} = {num1 / num2}')
    # prompt(f'{num1} // {num2} = {num1 // num2}')
    # prompt(f'{num1} % {num2} = {num1 % num2}')
    # prompt(f'{num1} ** {num2} = {num1 ** num2}')

# perform_arithmetic()

# 6 The End Is Near But Not Here
def penultimate(phrase: str) -> str:
    return phrase.split()[-2]

# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# 7 Exclusive Or
def xor(op1, op2) -> bool:
    return (op1 and not op2) or (op2 and not op1)
    # return bool(op) != bool(op2)
    
# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

# 8 Odd Lists
def oddities(my_list: list) -> list:
    # odds = []
    # for i in range (0, len(my_list), 2):
    #     odds.append(my_list[i])
    # return odds
    return my_list[::2]

# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

# 9 How Old is Teddy?
# print(f'Teddy is {random.randint(20, 100)} years old!')

# 10 When Will I Retire?
def retire():
    age = int(input('What is your age? '))
    retirement_age = int(input('At what age would you like to retire? '))
    years_remaining = retirement_age - age
    current_year = datetime.now().year

    print()
    print(f"""It's {current_year}. You will retire in {current_year + years_remaining}.
You have only {years_remaining} years of work to go!""")

# retire()

# 11 Get Middle Character
def center_of(my_string: str) -> str:
    length = len(my_string)
    if length % 2 == 0:
        return my_string[length // 2 - 1 : length // 2 + 1]
    else:
        return my_string[length // 2]

# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True

# 12 Always Return Negative
def negative(num):
    return num if num < 0 else -num

# print(negative(5) == -5)      # True
# print(negative(-3) == -3)     # True
# print(negative(0) == 0)       # True