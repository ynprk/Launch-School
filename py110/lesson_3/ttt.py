import os, random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def display_board(board):
    os.system('clear')

    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')
    print('')

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_turn(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        square = input(f'Choose a square ({", ".join(valid_choices)}): ')

        if square.strip().isdigit() and int(square.strip()) in empty_squares(board):
            square = int(square.strip())
            break

        print("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def computer_turn(board):
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
        [1, 5, 9], [3, 5, 7]             # diagonials
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
        
    return None


def board_full(board) -> bool:
    return len(empty_squares(board)) == 0

def set_flag():
    while True:
        keep_going = input('Would you like to play again? (y/n): ')
        if keep_going.strip().lower() in ('y', 'n'):
            break
        print('Please enter y or n')
    return keep_going

def main():
    while True:
        print('Welcome to Tic Tac Toe')
        print(f'You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.')

        board = initialize_board()

        while True:
            display_board(board)

            player_turn(board)
            if detect_winner(board) or board_full(board):
                display_board(board)
                break

            computer_turn(board)
            if detect_winner(board) or board_full(board):
                display_board(board)
                break
            
        if detect_winner(board):
            print(f'{detect_winner(board)} won!')
        else:
            print("It's a tie!")


        if set_flag() == 'n':
            print('Bye Bye')
            break

if __name__ == '__main__':
    main()