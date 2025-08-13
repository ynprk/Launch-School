#Q1
# No, first() returns the expected value of 
# {'prop1': 'hi there'}, but second() returns None
# since the indented block after the return statement is unreachable.

#Q2
# Output:
# [1, 2]
# {'first': [1, 2]}

# Since num_list is a reference to the original list
# in the dictionary, appending to num_list modifies the list.
# Thus, the original dictionary is also updated.
# If we want to modify num_list but not dictionary, we could:
# a) initialize num_list with a reference to a copy of the original list
# num_list = dictionary['first'].copy()
# or b), use list slicing which returns a new list
# num_list = dictionary['first][:]

#Q3
# In all three scenarios, the variables one, two, and three
# inside the mess_with_vars function are local to the function.
# They are not the same as the variables one, two, and three
# defined outside the function. This is known as variable shadowing,
# where the local variables inside the function overshadow
# the variables outside the function with the same names.

# A) and B)
# The output is:
# one is: ['one']
# two is: ['two']
# three is: ['three']
# Since variables one, two, and three in the mess_with_vars
# function are local, reassigning them does not affect the original list.

# C)
# The output is:
# one is: ['two']
# two is: ['three']
# three is: ['one']
# In this case, the mess_with_vars function modifies the
# content of the lists directly. Since lists in Python
# are mutable and passed by reference, the changes are reflected
# outside the function.

# Bonus: I was curious and modified A) to print its parameters
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one
    print(f"one is: {one}")
    print(f"two is: {two}")
    print(f"three is: {three}")

one = 'one'
two = 'two'
three = 'three'

mess_with_vars(one, two, three)

# The output is:
# one is: two
# two is: three
# three is: two
# The output for three might be unexpected, but
# it's because we already assigned one = two.

# 4
def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")

    if len(dot_separated_words) != 4:
        return False
    
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

print(is_dot_separated_ip_address('10.4.5.11'))
print(is_dot_separated_ip_address('10.4.5'))
print(is_dot_separated_ip_address('257.4.5.11'))
print(is_dot_separated_ip_address(''))
print(is_dot_separated_ip_address('1.1.1.1'))

#Q5
# I expect a NameError as greeting as never been initalized
# since we never enter the if block due to the False condition.