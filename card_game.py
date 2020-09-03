#!/usr/bin/env python
# encoding: utf-8
"""
card_game.py
This file contains the implementation of the card game.
"""

import CONSTANTS

class Card():
    def __init__(self, color, number):
        """
        Init function, validate input when init the object.
        color: color of the card. Should be in CONSTANTS.COLORS.
        number: number of the card. Should be in range
                [1, CONSTANTS.NUM_CARDS_EACH_COLOR_IN_DECK]
        """
        # Validate color and number
        if color not in CONSTANTS.COLORS:
            raise ValueError('{color} is not in valid colors{colors}.' \
                                .format(color=color, colors=CONSTANTS.COLORS))

        if number not in range(1, CONSTANTS.NUM_CARDS_EACH_COLOR_IN_DECK + 1):
           raise ValueError("{num} is not in valid range [1, {max_num}]." \
            .format(num=number, max_num=CONSTANTS.NUM_CARDS_EACH_COLOR_IN_DECK))

        self.color = color
        self.number = number

class Deck():
    def __init__(self):
        self.cards = [Card(color, number) for color in CONSTANTS.COLORS for \
                number in range(1, CONSTANTS.NUM_CARDS_EACH_COLOR_IN_DECK + 1)]

        self.size = len(self.cards)

    def shuffle(self):
        pass

    def get(self):
        pass

    def sort(self, color_order):
        pass

class Player():
    def __init__(self):
        self.cards = []
        self.num_cards = 0

    def get_card(self, deck):
        pass

    def get_score(self):
        pass
