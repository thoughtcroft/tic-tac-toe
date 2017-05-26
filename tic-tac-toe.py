#!/usr/bin/env python
#
# Tic Tac Toe game
#
# Created for the Milestone 1 Project
#
# the board is a 9 element list which will
# store 'X' and 'O' for player moves
# a space represents an unoccupied position


# python2 and python3 portability
from __future__ import print_function
import sys


def display_board(board):
    '''
    Print the current board layout
    '''
    print()
    print(' {} | {} | {} '.format(*board[0:3]))
    print('---|---|---')
    print(' {} | {} | {} '.format(*board[3:6]))
    print('---|---|---')
    print(' {} | {} | {} '.format(*board[6:9]))
    print()


def make_move(board, position, player):
    '''
    Add player's move to the board
    '''
    # only valid moves are passed in here
    board[position - 1] = player


def winning_move(board, position, player):
    '''
    Check if the player made a winning move
    '''
    win = list(player * 3)
    if get_row(board, position) == win:
        return True
    elif get_column(board, position) == win:
        return True
    elif position % 2 != 0:
        # odd positions are on the diagonals
        return get_diagonal(board, 1) == win or get_diagonal(board, 3) == win
    else:
        return False


def get_row(board, position):
    '''
    Return the row result
    '''
    row = (position - 1) / 3 * 3
    return board[row:row + 3]


def get_column(board, position):
    '''
    Return the column result
    '''
    col = (position - 1) % 3
    return [board[x] for x in (col, col + 3, col + 6)]


def get_diagonal(board, diagonal):
    '''
    Return the diagonal result
    based on whether it is 1 or 3
    '''
    if diagonal == 1:
        positions = (0, 4, 8)
    elif diagonal == 3:
        positions = (2, 4, 6)
    return [board[x] for x in positions]


def get_next_move(board, player):
    '''
    Prompt player to enter their next move
    '''
    print("Player '{}' please enter your next move:".format(player))
    while True:
        move = get_input('> ')
        if '1' <= move <= '9':
            move = int(move)
            if move - 1 in valid_moves(board):
                break
        print("That is not a valid move, please try again...")
    return move


def valid_moves(board):
    '''
    Return available moves ie unoccupied index positions
    '''
    return [i for i, x in enumerate(board) if x == ' ']


def main():
    '''
    This is where it all comes together
    '''
    print()
    print('Welcome to Tic Tac Toe!')
    print('-----------------------')
    print()
    print('To make a move, please enter a position from 1 - 9')
    print('corresponding to the layout of your phone keypad')
    print()

    board = list(' ' * 9)
    players = ['X', 'O']
    moves = 0
    display_board(board)

    while True:
        player = players.pop(0)
        players.append(player)
        moves += 1
        position = get_next_move(board, player)
        make_move(board, position, player)
        display_board(board)

        if moves > 4 and winning_move(board, position, player):
            print("Congratulations '{}', you are the winner :)".format(player))
            break

        if moves > 8:
            print("Stalemate, no-one is a winner :(")
            break

    print()
    sys.exit(0)

# end of main

# python2 and python3 portability
if __name__ == "__main__":
    # Support Python 2 and 3 input
    # Default to Python 3's input()
    get_input = input

    # If this is Python 2, use raw_input()
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    main()
