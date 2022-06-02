# A simple cli Rock-Paper-Scissors game written in python

# Steps
# Display the rules and instructions for the game
# Define the list of possible moves
# cpu selects a move
# Player selects a move (validate input; repeat until valid input)
# Compare the moves and determine a winner
# Display the results to the player and end game

import random

print('''
Hello human 😌,
Welcome to the Rock-Paper-Scissors game!
I am the cpu that's about to beat you 😏.
''')


class RpsGame:
    def __init__(self):
        # Define the list of possible moves
        # R -> rock, P -> paper, S -> scissors
        self.possible_moves = ['R', 'P', 'S']
        self.cpu_move = random.choice(self.possible_moves)
        self.player_move = None

    def get_player_move(self):
        while True:
            # Get player move
            self.player_move = input(
                'Choose your move: R for Rock, P for Paper or S for Scissors? 😎 ').upper().strip()
            if self.player_move not in self.possible_moves:
                print('Invalid move. Please try again. 😒')
            else:
                break

    def move_to_string(self, move):
        if move == 'R':
            return 'rock'
        elif move == 'P':
            return 'paper'
        elif move == 'S':
            return 'scissors'

    def get_cpu_move(self):
        # Get the cpu's move
        self.cpu_move = random.choice(self.possible_moves)

    def compare_moves(self):
        # Compare the moves and determine a winner

        # Change options to full words
        self.player_move = self.move_to_string(self.player_move)
        self.cpu_move = self.move_to_string(self.cpu_move)

        # Display the moves played to the player
        print(f'Player ({self.player_move}) : CPU ({self.cpu_move}).')

        if self.player_move == self.cpu_move:
            print(
                f'It\'s a tie! Both players chose {self.player_move} 😵‍💫')
            # it's a tie, repeat the game
            self.play_game()

        elif self.player_move == 'rock' and self.cpu_move == 'scissors':
            # the player won
            print(
                f'You win! {self.player_move} beats {self.cpu_move} 🤯')

        elif self.player_move == 'paper' and self.cpu_move == 'rock':
            # the player won
            print(
                f'You win! {self.player_move} beats {self.cpu_move} 🤯')

        elif self.player_move == 'scissors' and self.cpu_move == 'paper':
            # the player won
            print(
                f'You win! {self.player_move} beats {self.cpu_move} 🤯')

        else:
            # the cpu won
            print(
                f'You lose! {self.cpu_move} beats {self.player_move} 😎')

    def play_game(self):
        self.get_player_move()
        self.get_cpu_move()
        self.compare_moves()


game = RpsGame()
game.play_game()
