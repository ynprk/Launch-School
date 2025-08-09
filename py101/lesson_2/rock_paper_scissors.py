import random

VALID_CHOICES = ('rock', 'paper', 'scissors')
WINNING_COMBOS = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

def prompt(message: str):
    print(f'==> {message}')

def main():
    prompt('Welcome to Rock Paper Scissors!')

    while True:
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        choice = input().strip().lower()
        while choice not in VALID_CHOICES:
            prompt('Please enter a valid choice')
            choice = input().strip().lower()

        computer_choice = random.choice(VALID_CHOICES)

        prompt(f'You chose {choice}')
        prompt(f'Computer chose {computer_choice}')

        if choice == computer_choice:
            prompt('You tied.')
        elif WINNING_COMBOS[choice] == computer_choice:
            prompt('You won!')
        else:
            prompt('You lost...')
        
        prompt('Would you like to play again? (y/n)')
        again = input().strip().lower()
        while again not in ['y', 'n']:
            prompt('Please enter "y" or "n"')
            again = input().strip().lower()
        if again == 'n':
            break

if __name__ == '__main__':
    main()
