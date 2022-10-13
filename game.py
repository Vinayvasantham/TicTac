import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class Tictactoe():
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # We use list for representing 3*3 board
        self.current_winner = None  # keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| '+' | '.join(row)+' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+' | '.join(row)+' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
        # moves =[]
        # for i,spot in enumerate(self.board):
        # ['X','X','O'] --> [(0,'X'),(1,'X'),(2,'O')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves

    def empty_square(self):
        return ' ' in self.board

    def num_empty_square(self):
        return self.board.count(' ')

    def winner(self, square, letter):
        # winner if three in a row anywhere.we have to check all of these
        # first let's check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3: (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # check column
        column_ind = square % 3
        column = [self.board[column_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # diagonals are (0,2,4,6,8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # from top left to bottom right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # from top right to bottom left
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all of these fail
        return False

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False


def play(game, x_player, o_player, print_game=True):
    # return the winner of the game ! None for tie
    if print_game:
        game.print_board_nums()

    letter = 'X'  # initial letter
    # iterate while the board has empty squares
    # we don't want to worry about winning we return result when there is no empty squares
    while game.empty_square():
        # get the move for the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        # let's define a function to make move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to the square {square}')
                game.print_board()
                print('')  # just empty line

            if game.current_winner is not None:
                if print_game:
                    print(letter + ' wins !')
                return letter

            # After we made our move we have to alternate
            letter = 'O' if letter == 'X' else 'X'  # Switches player

        time.sleep(0.8)

    if print_game:
        print("it's a tie")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = SmartComputerPlayer('O')
    t = Tictactoe()
    play(t, x_player, o_player, print_game=True)
