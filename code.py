
from __future__ import print_function
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
def player_input():
    
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: Do you want to be X or O?').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,marker):
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or # across the top
    (board[4] == marker and board[5] == marker and board[6] == marker) or # across the middle
    (board[1] == marker and board[2] == marker and board[3] == marker) or # across the bottom
    (board[7] == marker and board[4] == marker and board[1] == marker) or # down the middle
    (board[8] == marker and board[5] == marker and board[2] == marker) or # down the middle
    (board[9] == marker and board[6] == marker and board[3] == marker) or # down the right side
    (board[7] == marker and board[5] == marker and board[3] == marker) or # diagonal
    (board[9] == marker and board[5] == marker and board[1] == marker)) # diagonal

import random
def choose_first():
    if random.randint(0,1)==0:
        return 'player1'
    else:
        return 'player2'
        

        
def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True    

def player_choice(board):
    # Using strings because of raw_input
    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        
        position = raw_input('Choose your next position: (1-9) ')
    return int(position)


def replay():
    
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')    
    
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    Board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(Board)
            position = player_choice(Board)
            place_marker(Board, player1_marker, position)

            if win_check(Board, player1_marker):
                display_board(Board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(Board):
                    display_board(Board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(Board)
            position = player_choice(Board)
            place_marker(Board, player2_marker, position)

            if win_check(Board, player2_marker):
                display_board(Board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(Board):
                    display_board(Board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break    
    
