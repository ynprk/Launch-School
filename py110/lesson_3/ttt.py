import os, random

HUMAN, COMPUTER = 'X', 'O'
EMPTY = None
WINNING_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
    [0, 4, 8], [2, 4, 6]              # diags
]
MATCH_WINS = 3

def display_board(board):
    os.system('clear')
    symbols = [(c if c else " ") for c in board]

    for r in range(0, 9, 3):
        print('     |     |')
        print(f'  {symbols[r]}  |  {symbols[r+1]}  |  {symbols[r+2]}')
        print('     |     |')
        if r < 6:
            print('-----+-----+-----')
        print()

def get_empty_squares(board):
    return [i for i, c in enumerate(board) if c is EMPTY]

def determine_winner(board):
    for a, b, c in WINNING_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return HUMAN if board[a] == HUMAN else COMPUTER
    return None

def is_full(board):
    return all(board)

def ask_move(board):
    valid_choices = [str(i+1) for i in get_empty_squares(board)]

    while True:
        move = input(f'Choose a square ({join_or(valid_choices)}): ').strip()
        if move in valid_choices:
            return int(move) - 1
        print("Sorry, that's not a valid choice.")

def play_game():
    board = [EMPTY] * 9

    while True:
        display_board(board)

        board[ask_move(board)] = HUMAN
        if (winner := determine_winner(board)) or is_full(board): break

        board[random.choice(get_empty_squares(board))] = COMPUTER
        if (winner := determine_winner(board)) or is_full(board): break

    return winner

def print_scores(scores):
    print(f'SCORE - YOU ({HUMAN}): {scores[HUMAN]} | COMPUTER ({COMPUTER}): {scores[COMPUTER]}')

def play_match():
    scores = {HUMAN: 0, COMPUTER: 0}

    while True:
        print_scores(scores)

        winner = play_game()

        if winner:
            scores[winner] += 1
            print(f'{winner} wins the game!')
        else:
            print(f'It\'s a tie!')
        
        if scores[HUMAN] == MATCH_WINS or scores[COMPUTER] == MATCH_WINS:
            match_winner = HUMAN if scores[HUMAN] == MATCH_WINS else COMPUTER
            print(f'{match_winner} wins the match!')
            return match_winner

        input('Press enter for next game...')


def main():
    while True:
        print(f'Welcome to Tic Tac Toe! You = {HUMAN}, Computer = {COMPUTER}')
        print(f'First to {MATCH_WINS} wins takes the match.')
        
        play_match()

        while True:
            again = input('Start a new match? (y/n) : ').strip().lower()
            if again in ('y', 'n'):
                break
            print('Please enter y or n.')
        
        if again == 'n':
            print('Bye-bye.')
            break

# ---------- TTT BONUS FEATURES ----------
def join_or(seq, delimiter=', ', connector='or'):
    if len(seq) == 0:
        return ''
    elif len(seq) == 1:
        return str(seq[0])
    elif len(seq) == 2:
        return f'{str(seq[0])} {connector} {str(seq[1])}'
    else:
        leading_elements = delimiter.join(str(ele) for ele in seq[0:-1])
        return f'{leading_elements}{delimiter}{connector} {seq[-1]}'

if __name__ == '__main__':
    main()
    
    # print(join_or([1, 2, 3]))               # => "1, 2, or 3"
    # print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
    # print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
    # print(join_or([]))                      # => ""
    # print(join_or([5]))                     # => "5"
    # print(join_or([1, 2]))                  # => "1 or 2"
    # print(join_or([1, 2], ', ', 'and'))     # => "1 and 2"