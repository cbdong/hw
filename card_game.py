#!/usr/bin/env python
# encoding: utf-8
"""
card_game.py
This file contains the implementation of the card game.
"""

import CONSTANTS
import random
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
    def __init__(self, cards=None):
        self.cards = [Card(color, number) for color in CONSTANTS.COLORS for \
            number in range(1, CONSTANTS.NUM_CARDS_EACH_COLOR_IN_DECK + 1)] \
            if cards is None else cards

        self.size = len(self.cards)

    def _isEmpty(self):
        return self.size == 0

    def shuffle(self):
        random.shuffle(self.cards)

    def get(self):
        if self._isEmpty():
            raise IndexError("Try to get a card from an empty deck")

        self.size -= 1
        return self.cards.pop()

    def sort_cards(self, color_order):
        if self._isEmpty():
            return
        def card_compare(cardA, cardB):
            color_to_idx = {color: i for i, color in enumerate(color_order)}
            if cardA.color == cardB.color:
                return cardA.number - cardB.number
            else:
                return color_to_idx[cardA.color] - color_to_idx[cardB.color]
        self.cards.sort(cmp=card_compare)


class Player():
    def __init__(self, cards=None):
        self.cards = [] if cards is None else cards
        self.num_cards = 0

    def get_card(self, deck):
        pass

    def get_score(self):
        pass
