import random
import numpy as np

def make_guess_number(mode : str) -> int:

    if mode == 'rand':
        guessCount = random.randint(5, 10)
    else:
        guessCount = 8

    return guessCount

def make_colour_number(mode : str) -> int:

    if mode == 'rand':
        colourCount = random.randint(3, 10)
    else:
        colourCount = 4

    return colourCount

def make_pins_number(mode : str) -> int:

    if mode == 'rand':
        pinsCount = random.randint(4, 6)
    else:
        pinsCount = 4

    return pinsCount

def make_specs(modes : dict = {}) -> dict:

    colours = make_colour_number(modes['colour'])
    pins = make_pins_number(modes['pins'])
    guesses = make_guess_number(modes['guesses'])

    specs = {'colours':colours,
             'pins':pins,
             'guesses':guesses}

    return specs

if __name__ == "__main__":

    modes = {'colour':'',
             'pins':'',
             'guesses':''}
    specs = make_specs(modes)

    for ele in specs:
        print(ele, specs[ele])

