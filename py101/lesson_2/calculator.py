def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False

def perform_calculation():
    prompt("What's the first number? ")
    num1 = input()
    while invalid_number(num1):
        prompt('Please enter a valid number.')
        num1 = input()

    prompt("What's the second number? ")
    num2 = input()
    while invalid_number(num2):
        prompt('Please enter a valid number.')
        num2 = input()

    prompt('What operation would you like to perform?\n'
        '1) Add 2) Subtract 3) Multiply 4) Divide ')
    operation = input()
    while operation not in ['1', '2', '3', '4']:
        prompt('Please choose 1, 2, 3, or 4.')
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

    prompt(f'The result is: {output}')

prompt('Welcome to Calculator!')
again = 'y'
while again == 'y':
    perform_calculation()
    prompt(f'Would you like to perform a new calculation? (y/n)')
    again = input().lower()
    while again not in ['y', 'n']:
        prompt('Please type y or n')
        again = input().lower()
