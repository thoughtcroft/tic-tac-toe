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
    print(' {0} | {1} | {2} '.format(board[0], board[1], board[2]))
    print('---|---|---')
    print(' {0} | {1} | {2} '.format(board[3], board[4], board[5]))
    print('---|---|---')
    print(' {0} | {1} | {2} '.format(board[6], board[7], board[8]))
    print()


def make_move(board, position, player):
    '''
    Add players move to the board
    '''
    pos = position - 1
    if board[pos] != ' ':
        # raise an error
        pass
    else:
        board[pos] = player


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
        return get_diagonal(board, 1) == win or get_diagonal(board, 3) == win
    else:
        return False


def get_row(board, position):
    '''
    Return the row result
    '''
    pos = position - 1
    row = pos / 3 * 3
    return board[row:row + 3]


def get_column(board, position):
    '''
    Return the column result
    '''
    pos = position - 1
    col = pos % 3
    return [board[x] for x in (col, col + 3, col + 6)]


def get_diagonal(board, diagonal):
    '''
    Return the diagonal result
    based on whether it is 1 or 3
    '''
    if diagonal == 1:
        return [board[x] for x in (0, 4, 8)]
    elif diagonal == 3:
        return [board[x] for x in (2, 4, 6)]


def get_next_move(board, player):
    '''
    Prompt player to enter their next move
    '''
    print("Player '{}' please enter your next move".format(player))
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
    Return available moves
    '''
    return [i for i, n in enumerate(board) if n == ' ']


def main():
    '''
    This is where the action starts
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

        if moves > 4:
            if winning_move(board, position, player):
                print("Congratulations '{}', you are the winner :)".format(player))
                print()
                sys.exit(0)

        if moves > 8:
            print("Stalemate, no-one is a winner :(")
            print()
            sys.exit(0)

# end of main


if __name__ == "__main__":
    # Support Python 2 and 3 input
    # Default to Python 3's input()
    get_input = input

    # If this is Python 2, use raw_input()
    if sys.version_info[:2] <= (2, 7):
        get_input = raw_input

    main()
