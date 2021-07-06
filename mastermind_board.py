from game_setup import *
from collections import Counter
from helper_functions import get_nth_place
import random
import numpy as np


class Board:

    def __init__(self, gameModes):

        #mySpecs = make_specs(gameModes)
        mySpecs = gameModes
        
        self.pins = make_pins_number(mySpecs['pins'])
        self.colours = make_colour_number(mySpecs['colours'])
        self.guesses = make_guess_number(mySpecs['guesses'])
        self.truth_mode = mySpecs['truth']
        self.player = mySpecs['player']
        self.currentGuess = 0

        self.board = np.zeros([self.guesses, self.pins])
        self.scores = np.zeros([self.guesses])
        self.truth = self.make_truth()

    def get_pins(self) -> int:
        return self.pins

    def get_colours(self) -> int:
        return self.colours

    def get_guesses(self) -> int:
        return self.guesses

    def get_truth(self):
        return self.truth

    def get_board(self):
        return self.board

    def make_truth(self) -> np.array:

        pins = self.pins
        colours = self.colours

        if self.truth_mode == 'random':

            trueColours = np.empty([pins], dtype=int)

            for pin in range(pins):
                colour = random.randint(1, colours)
                trueColours[pin-1] = colour

        elif self.truth_mode == 'pregen':

            trueColours = np.ones([pins])

        elif self.truth_mode == 'input':

            trueColours = np.empty([pins], dtype=int)

            for pin in range(pins):
                trueColours[pin-1] = input("What is the truth for pin{}?".format(pin))

        return trueColours

    def make_guess(self, place) -> int:
        
        if self.player == 'me':
            guess = input("Please guess the {} val".format(get_nth_place(place)))
        elif self.player == 'random':
            guess = random.randint(1, self.colours)
        elif self.player == 'ai':
            print("Not implemented yet")
            guess = 0
        else:
            print("feck")
            guess = 0

        return guess

    def calc_score(self, turn):

        colours = self.get_colours()
        truth = self.truth
        toScore = self.board[0-turn]

        greens = 0
        amberTrues = []
        amberGuess = []
        for pin_num in range(len(truth)):

            T = truth[pin_num] # Colour of pin for true 
            G = toScore[pin_num] # Colour of pin from guess

            if T == G:
                greens += 1

            else:
                amberTrues.append(T)
                amberGuess.append(G)

        ambers = 0
        true_counter = Counter(amberTrues)
        guess_counter = Counter(amberGuess)

        for colour in range(colours):
            ambers += min(true_counter[colour], guess_counter[colour])
        
        score = (greens, ambers)

        return score

    def take_turn(self):

        self.currentGuess += 1
        turn = self.currentGuess

        for place in range(self.pins):

            thisPin = self.make_guess(place+1)
            self.board[0-turn, place] = thisPin

        score = self.calc_score(turn)
        print("You got", score[0], "correct, and", score[1], "close.")
        
        if score == (self.pins, 0):
            print("You won!!!!!!!!!")
            state = 'win'

        #if last guess, lose :(
        elif turn == self.guesses:
            print("you ran out of guesses :(")
            state = 'loss'

        else:
            print("Keep going!")
            state = 'draw'



        return state
