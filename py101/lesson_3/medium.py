#Q1
def flintstones():
    for i in range(10):
        print(f"{'-' * i}The Flintstones Rock!")

#flintstones()

#Q2
def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

#print(factors(12))
# Alan should change while divisor != 0 to
# while divisor > 0, so that a negative number
# never enters the loop.

# The purpose of number % divisor == 0 is to check if
# the divisor is indeed a factor of the number.
# For example, if the number is 12 and the divisor is 7,
# 12 % 7 is not 0, so we decrement the divisor by 1.
# 12 % 6 is 0, so we add 6 to result.

#Q3
# In the first appraoch, Alyssa mutated the buffer
# using the append method. In the second approach,
# she made a new list when adding a new element, then
# reassigned that list to the buffer variable.

#Q4
# It will be a number that is close to but not quite 0.9
# (something like 0.8999999) and False since floating point
# arithmetic is weird like that. Use math.isclose(0.3 + 0.6, 0.9) as a workaround.

#Q5
# The output is False. Python doesn't let you use ++
# to determine whether a value is nan. Instead, you can use
# the math.isnan(value) function.

#Q6
#The output is 34. The variable answer is never reassigned, nor is
# new_answer ever outputted.

#Q7
# Yup, it got ransacked alright. munsters is a dictionary
# which is a mutable data type. So when munsters was passed as an argument to
# mess_with_demographics, a reference to the dictionary was passed, not a copy.

#Q8
def rps(fist1, fist2):
    if fist1 == "rock":
        print("paper" if fist2 == "paper" else "rock")
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        print("scissors" if fist2 == "scissors" else "paper")
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        print("rock" if fist2 == "rock" else "scissors")
        return "rock" if fist2 == "rock" else "scissors"

rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock")
# The output is paper. The innermost calls
# rps("rock", "paper") evaluates to paper, and rps("rock", "scissors") evaluates to rock.
# The middle call rps("paper", "rock") evaluates to "paper".
# The outermost call, rps("paper", "rock") also evaluates to "paper".

#Q9
# bar(foo()) 
# Let's evaluate the argument first.
# foo() returns "yes"
# bar("yes")
# (param == "no") evaluates to False
# We could stop here since False and Something
# will always be False (short circuit evaluation), 
# but for the sake of completeness:
# foo() evaluates to "yes", a truthy value 
# "no" is also a truthy value
# so we have False and (True or True)
# which evaluates to False

#Q10
# True, a and c point to the same object in memory,
# since we assigned c = a
# and because of integer interning, all instances of 42
# (and other integers in the range -5 to 256)
# will be the same object, so b also has the same id as a and c
