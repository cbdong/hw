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

    def sort(self, color_order):
        if self._isEmpty():
            return
        def card_compare(cardA, cardB):
            color_to_idx = {color: i for i, color in enumerate(color_order)}
            for i in range(len(color_order)):
                color_to_idx[color_order[i]] = i
            if cardA.color == cardB.color:
                return cardA.number - cardB.number
            else:
                return color_to_idx[cardA.color] - color_to_idx[cardB.color]
        self.cards.sort(cmp=card_compare)


class Player():
    def __init__(self, cards=None):
        self.cards = [] if cards is None else cards
        self.num_cards = len(self.cards)

    def get_card(self, deck):
        """
        Player try to get a card from a card deck
        deck: the deck that the player will get a card from. If the deck is
              empty, raise ValueError
        """
        if deck.size == 0:
            raise ValueError("The input deck is empty")

        card = deck.get()
        self.cards.append(card)
        self.num_cards += 1

    def get_score(self):
        return sum([CONSTANTS.COLOR_WEIGHT[card.color] * card.number for \
                    card in self.cards])

class Game():
    def __init__(self):
        self.player0 = Player()
        self.player1 = Player()
        self.deck = Deck()

    def _take_cards(self):
        self.deck.shuffle()
        for i in range(CONSTANTS.NUM_CARDS_TO_GET_BY_PLAYER):
            self.player0.get_card(self.deck)
            self.player1.get_card(self.deck)

    def _find_winner(self):
        print("Player0 has the following cards:")
        for card in self.player0.cards:
            print("({},{})".format(card.color, card.number))
        print("Player1 has the following cards:")
        for card in self.player1.cards:
            print("({},{})".format(card.color, card.number))
        score0 = self.player0.get_score()
        score1 = self.player1.get_score()
        print("Score that player0 get: {}".format(score0))
        print("Score that player1 get: {}".format(score1))
        if score0 > score1:
            return 0
        elif score1 > score0:
            return 1
        else:
            return -1

    def play(self):
        self._take_cards()
        return self._find_winner()
