from game_setup import make_specs
from mastermind_board import Board

## Before game can run, get specs!

gameModes = {'colour':'',
             'pins':'',
             'guesses':'',
             'player':'me',
             'truth':'pregen'}

#gameSpecs = make_specs(gameModes)

## Check that the settings have loaded

myBoard = Board(gameModes)
print(myBoard.get_guesses())
#myBoard.make_board()