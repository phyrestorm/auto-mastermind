from game_setup import make_specs
import random
import numpy as np


class Board:

    def __init__(self, gameModes):

        mySpecs = make_specs(gameModes)
        
        self.pins = mySpecs['pins']
        self.colours = mySpecs['colours']
        self.guesses = mySpecs['guesses']
        self.truth = mySpecs['truth']
        self.player = mySpecs['player']
        self.currentGuess = 1

        self.board = np.zeros([self.guesses, self.pins])
        self.scores = np.zeros([self.guesses])
        self.truth = self.get_truth()

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

        if self.truth == 'random':
            
            pins = self.pins
            colours = self.colours

            trueColours = np.empty([pins], dtype=int)

            for pin in range(pins):
                colour = random.randint(1, colours)
                trueColours[pin-1] = colour

        elif self.truth == 'pregen':

            trueColours = np.ones([pins])

        elif self.truth == 'input':

            trueColours = np.empty([pins], dtype=int)

            for pin in range(pins):
                trueColours[pin-1] = input("What is the truth for pin{}?".format(pin))

        return trueColours

    def make_guess(self) -> int:

        if self.player == 'me':
            guess = input("Please guess the val")
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

        truth = self.truth
        toScore = self.board[turn]

        #get the 
        score = (0,0)

        return score

    def take_turn(self):

        #get current turn number
        turn = self.currentGuess
        #get guess
        for place in range(self.pins):
            #go through pins, and get colour for each
            thisPin = self.make_guess()
            self.board[turn, place] = thisPin

        #return score for guess
        score = self.calc_score(turn)
            #if 100% win!
        #if last guess, lose :(
