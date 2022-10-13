import math
import random


class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid square from board
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-8): ')
            # we are going to check that this is correct input or not
            # if it's not an integer , we give it is as an invalid input
            # if the spot is not available on the board , it is invalid input
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square ! Try again.')
        return val


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # get the square based on the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None, 'Score': 1 * (state.num_empty_square() + 1) if other_player == max_player else -1*(
                    state.num_empty_square() + 1)}
        elif not state.empty_square():
            return {'position': None, 'Score': 0}

        # initialize some dictionaries
        if player == max_player:
            best = {'position': None, 'Score': -math.inf}
        else:
            best = {'position': None, 'Score': math.inf}

        for possible_moves in state.available_moves():
            # step - 1 : make a move : try that spot
            state.make_move(possible_moves, player)
            # step - 2 : recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)
            # step - 3 : undo the move
            state.board[possible_moves] = ' '
            state.current_winner = None
            sim_score['position'] = possible_moves
            # step - 4 : update the dictionary if necessary

            if player == max_player:  # we are trying to maximize the player
                if sim_score['Score'] > best['Score']:
                    best = sim_score                      # replace best
            else:
                if sim_score['Score'] < best['Score']:
                    best = sim_score                  # replace best
        return best









