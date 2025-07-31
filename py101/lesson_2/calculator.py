import json

# open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

def perform_calculation():
    prompt(MESSAGES['first_number'])
    num1 = input()
    while invalid_number(num1):
        prompt(MESSAGES['invalid_number'])
        num1 = input()

    prompt(MESSAGES['second_number'])
    num2 = input()
    while invalid_number(num2):
        prompt(MESSAGES['invalid_number'])
        num2 = input()

    prompt(MESSAGES['which_operation'])
    operation = input()
    while operation not in ['1', '2', '3', '4']:
        prompt(MESSAGES['invalid_operation'])
        operation = input()

    match operation:
        case '1':
            output = int(num1) + int(num2)
        case '2':
            output = int(num1) - int(num2)
        case '3':
            output = int(num1) * int(num2)
        case '4':
            output = int(num1) / int(num2)

    prompt(f'{MESSAGES["result"]} {output}')

# main program
prompt(MESSAGES['welcome'])
again = 'y'
while again == 'y':
    perform_calculation()
    prompt(MESSAGES['new_calculation'])
    again = input().lower()
    while again not in ['y', 'n']:
        prompt(MESSAGES['invalid_new'])
        again = input().lower()
