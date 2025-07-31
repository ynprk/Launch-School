import json

# open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

LANGUAGE = 'en'

def prompt(key: str, **kwargs):
    message = MESSAGES[LANGUAGE][key].format(**kwargs)
    print(f'=> {message}')

def get_valid_number(prompt_key: str) -> float:
    prompt(prompt_key)
    num = input()
    while not is_valid_number(num):
        prompt('invalid_number')
        num = input()
    return float(num)

def is_valid_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def get_operation() -> str:
    prompt('which_operation')
    op = input()
    while op not in ['1', '2', '3', '4']:
        prompt('invalid_operation')
        op = input()
    return op

def perform_calculation():
    x = get_valid_number('first_number')
    y = get_valid_number('second_number')
    op = get_operation()

    match op:
        case '1':
            output = x + y
        case '2':
            output = x - y
        case '3':
            output = x * y
        case '4':
            try:
                output = x / y
            except ZeroDivisionError:
                prompt('zero_division')
                return

    if output.is_integer():
        output = int(output)

    prompt('result', output=output)

def main():
    prompt('welcome')
    again = 'y'
    while again == 'y':
        perform_calculation()
        prompt('new_calculation')
        again = input().strip().lower()
        while again not in ['y', 'n']:
            prompt('invalid_new')
            again = input().strip().lower()

if __name__ == '__main__':
    main()
