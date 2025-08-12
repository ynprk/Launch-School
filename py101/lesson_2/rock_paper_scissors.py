import random

WINNING_COMBOS = {
    "rock": {"scissors": "crushes", "lizard": "crushes"},
    "paper": {"rock": "covers", "spock": "disproves"},
    "scissors": {"paper": "cuts", "lizard": "decapitates"},
    "lizard": {"spock": "poisons", "paper": "eats"},
    "spock": {"scissors": "smashes", "rock": "vaporizes"}
}

VALID_CHOICES = list(WINNING_COMBOS.keys())

def prompt(message: str):
    print(f'==> {message}')

def get_choice() -> str:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    while True:
        user_input = input().strip().lower()

        # exact match
        if user_input in VALID_CHOICES:
            return user_input

        # find matches by prefix
        matches = [choice for choice in VALID_CHOICES if choice.startswith(user_input)]

        if len(matches) == 1:
            return matches[0]
        elif len(matches) > 1:
            prompt(f'Ambiguous input "{user_input}". Did you mean one of: {", ".join(matches)}?'
                   'Please type more letters.')
        else:
            prompt('Please enter a valid choice.')

def determine_winner(player: str, computer: str) -> str:
    if player == computer:
        return "tie"
    elif computer in WINNING_COMBOS[player]:
        return "player"
    elif player in WINNING_COMBOS[computer]:
        return "computer"
    else:
        raise ValueError(f"Unexpected choices: {player}, {computer}")

def play_round():
    player = get_choice()
    computer = random.choice(VALID_CHOICES)
    winner = determine_winner(player, computer)

    if winner == "tie":
        prompt("It's a tie!")
    elif winner == "player":
        reason = WINNING_COMBOS[player][computer]
        prompt(f"You win! {player.title()} {reason} {computer.title()}.")
    else:
        reason = WINNING_COMBOS[computer][player]
        prompt(f"You lose! {computer.title()} {reason} {player.title()}.")

    return winner

def main():
    prompt('Welcome to Rock Paper Scissors Lizard Spock!')
    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        winner = play_round()

        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1

        prompt(f"You: {player_score} -- Computer: {computer_score}")
        prompt(f"-------------------------------------------------")

    if player_score > computer_score:
        prompt("You win the best of five!")
    else:
        prompt("Computer wins the best of five!")

if __name__ == '__main__':
    main()
