# 1 Isn't it Odd?
def is_odd(num: int) -> bool:
    return num % 2 != 0

# is_odd(5)
# is_odd(2)

# 2 Odd Numbers
def log_odd():
    for i in range(1, 100, 2):
        print(i)

# log_odd()

# 3 Even Numbers
def log_even():
    for i in range(2, 100, 2):
        print(i)

# log_even()

# 4 How big is the room?
def calculate_room_size():
    SQ_METER_TO_SQ_FEET = 10.7639
    length = get_positive_number('Enter the length of the room in meters: ')
    width = get_positive_number('Enter the width of the room in meters: ')
    area_sq_meters = length * width
    area_sq_feet = SQ_METER_TO_SQ_FEET * area_sq_meters
    print(f'The room is {area_sq_meters:.2f} sq meters ({area_sq_feet:.2f} sq feet).')

def is_positive_number(s: str) -> bool:
    try:
        return float(s) > 0
    except ValueError:
        return False

def get_positive_number(prompt: str) -> float:
    num = input(prompt)
    while not is_positive_number(num):
        num = input('Please enter a positive number: ')
    return float(num)

# calculate_room_size()

# 5 Tip calculator
def calculate_tip():
    # ignoring input validation; assumes the user will enter valid numbers
    bill = float(input('What is the bill? '))
    tip_percentage = float(input('What is the tip percentage? ')) / 100
    tip = bill * tip_percentage
    
    print()
    print(f'The tip is ${tip:.2f}')
    print(f'The total is ${bill + tip:.2f}')

# calculate_tip()

# 6 Sum or Product of Consecutive Integers
def sum_or_product():
    # ignoring input validation; assumes the user will enter valid inputs
    num = int(input('Please enter an integer greater than 0: '))
    op = input('Enter "s" to compute the sum, or "p" to compute the product: ')
    print()

    if op == 's':
        sum = 0
        for i in range(1, num + 1):
            sum += i
        print(f'The sum of the integers between 1 and {num} is {sum}.')
    elif op == 'p':
        product = 1
        for i in range(1, num + 1):
            product *= i
        print(f'The product of the integers between 1 and {num} is {product}.')
    else:
        print(f'Sorry, I did not understand your input.')

# sum_or_product()

# 7 Short Long Short
def short_long_short(s1: str, s2: str) -> str:
    if len(s1) < len(s2):
        return s1 + s2 + s1
    else:
        return s2 + s1 + s2

# These examples should all print True
# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

# 8 Leap Years (Part 1)
# def is_leap_year(year: int) -> bool:
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     else:
#         return year % 4 == 0

# These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == False)
# print(is_leap_year(1100) == False)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == False)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# 9 Leap Years (Part 2)
def is_leap_year(year: int) -> bool:
    if year < 1752:
        return year % 4 == 0
    else:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return year % 4 == 0

# These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == True)
# print(is_leap_year(1100) == True)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == True)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# 10 Multiples of 3 or 5
def multisum(num: int) -> int:
    total = 0
    for i in range(1, num + 1):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total

# These examples should all print True
# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(20) == 98)
# print(multisum(1000) == 234168)

# 11 UTF-16 String Value
def utf16_value(chars: str) -> int:
    total = 0
    for char in chars:
        total += ord(char)
    return total

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)