print('Welcome to Calculator!')
num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))
operation = input('What operation would you like to perform?\n'
                  '1) Add 2) Subtract 3) Multiply 4) Divide ')

if operation == '1':
    output = num1 + num2
elif operation == '2':
    output = num1 - num2
elif operation == '3':
    output = num1 * num2
elif operation == '4':
    output = num1 / num2

print(f'The result is: {output}')