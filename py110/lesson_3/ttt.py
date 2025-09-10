import os, random

HUMAN, COMPUTER = 'X', 'O'
EMPTY = None
WINNING_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
    [0, 4, 8], [2, 4, 6]              # diags
]

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

def empty_squares(board):
    return [i for i, c in enumerate(board) if c is EMPTY]

def determine_winner(board):
    for a, b, c in WINNING_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return HUMAN if board[a] == HUMAN else COMPUTER
    return None

def full(board):
    return all(board)

def ask_move(board):
    valid_choices = [str(i+1) for i in empty_squares(board)]

    while True:
        move = input(f'Choose a square ({", ".join(valid_choices)}): ').strip()
        if move in valid_choices:
            return int(move) - 1
        print("Sorry, that's not a valid choice.")

def play():
    board = [EMPTY] * 9
    while True:
        display_board(board)

        board[ask_move(board)] = HUMAN
        if (winner := determine_winner(board)) or full(board): break

        board[random.choice(empty_squares(board))] = COMPUTER
        if (winner := determine_winner(board)) or full(board): break

    display_board(board)
    print(f'{winner} wins!' if winner else "It's a tie!")

def main():
    while True:
        print(f'Welcome to Tic Tac Toe! You = {HUMAN}, Computer = {COMPUTER}')
        play()
        if input('Play again? (y/n) : ').strip().lower() != 'y':
            print('Bye-bye')
            break

if __name__ == '__main__':
    main()