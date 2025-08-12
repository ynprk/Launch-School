#Q1
numbers = [1, 2, 3, 4]
numbers.clear()
while numbers:
    numbers.pop()

#Q2
# The code will output [1, 2, 3, 4, 5]. In Python, you can 
# use the + operator to join two lists.

#Q3
# The code will output "hello there". On line 2, we assigned str1 the value of "hello there".
# On lines 2 and 3, we assign the value of str2 then reassign it, but we never change the value of str1.

#Q4
# The code will output [{"first": 42}, {"second": "value2"}, 3, 4, 5].
# list.copy() performs a shallow copy, meaning that my_list1 and my_list2 are
# separate objects, nested collections refer to the same object. 
# So when we modify a collection in my_list2, the same collection is my_list1 is also modified
# since they point to the same collection.

# Q5
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

def is_color_valid_short(color):
    return color == "blue" or color == "green"

def is_color_valid_short_alt(color):
    return color in ["blue", "green"]