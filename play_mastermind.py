from game_setup import make_specs
from mastermind_board import Board

## Before game can run, get specs!

"""
gameModes = {'colours':'',
             'pins':'',
             'guesses':'',
             'player':'me',
             'truth':'pregen'}
"""

#gameSpecs = make_specs(gameModes)

## Check that the settings have loaded

"""myBoard = Board(gameModes)
print(myBoard.get_guesses())
print(myBoard.get_board())
myBoard.take_turn()
#myBoard.make_board()
"""

def play_mastermind(modes):

    myBoard = Board(gameModes)
    state = 'draw'

    while state == 'draw':
        print(myBoard.get_board())
        state = myBoard.take_turn()

    if state == 'win':
        print(":D")
    elif state == 'loss':
        print("D:")

    print("You won in", myBoard.currentGuess, "turns.")

if __name__ == "__main__":

    gameModes = {'colours':'',
                 'pins':'',
                 'guesses':'',
                 'player':'me',
                 'truth':'pregen'}

    play_mastermind(gameModes)