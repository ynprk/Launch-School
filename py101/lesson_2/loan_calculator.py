def prompt(message: str):
    print(f'==> {message}')

def is_valid_number(s: str) -> bool:
    try:
        return float(s) > 0
    except ValueError:
        return False

def get_valid_number(message: str) -> float:
    prompt(message)
    while True:
        s = input().strip()
        if is_valid_number(s):
            return float(s)
        prompt('Please enter a positive number.')

def calculate_monthly_payment(loan_amount: float, apr: float, loan_duration: float) -> float:
    interest_rate = apr / 12
    return loan_amount * (interest_rate / (1 - (1 + interest_rate) ** -loan_duration))

def perform_calculation():
    loan_amount = get_valid_number('Enter the loan amount.')
    apr = get_valid_number(
        'Enter the Annual Percentage Rate (APR).\n' \
        'For an APR of 5%, enter 5 not 0.05.'
        ) / 100
    loan_duration = get_valid_number('Enter the loan duration in months.')
    monthly_payment = calculate_monthly_payment(loan_amount, apr, loan_duration)
    prompt(f"Your monthly payment is ${monthly_payment:,.2f}")

def main():
    prompt('Welcome to Mortgage / Car Loan Calculator!')
    again = 'y'
    while again == 'y':
        perform_calculation()
        prompt('Would you like to perform a new calculation? (y/n)')
        again = input().strip().lower()
        while again not in ('y', 'n'):
            prompt("Please type 'y' or 'n'")
            again = input().strip().lower()

if __name__ == '__main__':
    main()
