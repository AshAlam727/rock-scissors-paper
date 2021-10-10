# #!/usr/bin/env python3

# """This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round."""

# """The Player class is the parent class for all of the Players
# in this game"""
import random
import colorama
from colorama import Fore, Style
colorama.init()

moves = ['rock', 'paper', 'scissors']

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class HumanPlayer(Player):
    def move(self):
        choice = input("Enter a word (rock, paper or scissors): ").lower()
        while choice not in moves:
            print(RED+'Enter valid word'+Style.RESET_ALL)
            choice = input("Enter a word (rock, paper or scissors): ").lower()
        return choice


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class OnlyPlaysRock(Player):
    pass


class ReflectPlayer(Player):
    def __init__(self):
        super(ReflectPlayer, self).__init__()

    def move(self):
        self.their_move = random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move


class CyclePlayer(Player):
    my_move = random.choice(moves)

    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'

    def learn(self, my_move, thier_move):
        self.my_move = my_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.count_p1 = 0
        self.count_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        score = CYAN + \
            f'Score: Player1> {self.count_p1}, Player2> {self.count_p2}' + \
            Style.RESET_ALL
        if Player.beats(move1, move2):
            self.count_p1 += 1
            print('*You Win*')
            print(score)
        elif Player.beats(move2, move1):
            self.count_p2 += 1
            print('*You Loose*')
            print(score)
        elif move1 == move2:
            print('*Tie*')
            print(score)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        self.round = 6
        print("Rock Paper Scissors, Go!")
        for round in range(self.round):
            print(f"Round {round}:")
            self.play_round()
        print(GREEN+"Game over!"+Style.RESET_ALL)
        print(
            f'Final Score: Plaer1> {self.count_p1}, Plaer2> {self.count_p2}')
        if self.count_p1 > self.count_p2:
            print(MAGENTA+"***You Won***"+Style.RESET_ALL)
        elif self.count_p1 < self.count_p2:
            print(MAGENTA+"***You Lost***"+Style.RESET_ALL)
        else:
            print(MAGENTA+"***Its a Tie***"+Style.RESET_ALL)

        ask = input("Would you like to paly again(yes/no)?: ")
        if ask == 'yes':
            return self.play_game()
        else:
            print('Thak You\nSee you later')
            quit()


if __name__ == '__main__':
    game = Game(Player(), CyclePlayer())
    game.play_game()
