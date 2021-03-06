from card_game import Card, Deck, Player, Game
import CONSTANTS
import unittest

class CardTestCase(unittest.TestCase):
    def setUp(self):
        self.card = Card('red', 12)

    def test_value(self):
        self.assertEqual(self.card.color, 'red', 'wrong color assigned')
        self.assertEqual(self.card.number, 12, 'wrong number assigned')

    def test_color_value_exception(self):
        self.assertRaises(ValueError, Card, 'happy', 12)

    def test_number_value_exception(self):
        self.assertRaises(ValueError, Card, 'red', 13)

class DeckTestCase(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.cards = [Card('red', 1), Card('green', 3)]
        self.smDeck = Deck(self.cards)
        self.emptyDeck = Deck([])

        # new_deck contains cards with all color and number in order
        self.new_deck = Deck([Card(color, number) for color in \
        CONSTANTS.COLORS for number in \
        range(1, CONSTANTS.NUM_CARDS_EACH_COLOR_IN_DECK + 1)])

    def test_init_value_no_given_cards(self):
        # the deck contains all cards in order
        self.assertEqual(len(self.new_deck.cards), len(self.deck.cards))
        for i in range(len(self.new_deck.cards)):
            self.assertEqual(self.new_deck.cards[i].color, \
            self.deck.cards[i].color)
            self.assertEqual(self.new_deck.cards[i].number, \
            self.deck.cards[i].number)

    def test_init_value_given_cards(self):
        for i in range(len(self.cards)):
            self.assertEqual(self.cards[i].color, self.smDeck.cards[i].color)
            self.assertEqual(self.cards[i].number, self.smDeck.cards[i].number)

    def test_sort(self):
        color_order = CONSTANTS.COLORS
        self.deck.shuffle()
        self.deck.sort(color_order)
        # the deck contains all cards in order
        self.assertEqual(len(self.new_deck.cards), len(self.deck.cards))
        for i in range(len(self.new_deck.cards)):
            self.assertEqual(self.new_deck.cards[i].color, \
            self.deck.cards[i].color)
            self.assertEqual(self.new_deck.cards[i].number, \
            self.deck.cards[i].number)

    def test_get_from_non_empty(self):
        got_card = self.smDeck.get()
        self.assertEqual('green', got_card.color)
        self.assertEqual(3, got_card.number)
        self.assertEqual(1, self.smDeck.size)
        self.assertEqual(1, len(self.smDeck.cards))
        self.assertEqual('red', self.smDeck.cards[0].color)
        self.assertEqual(1, self.smDeck.cards[0].number)

    def test_get_from_empty(self):
        self.assertRaises(IndexError, self.emptyDeck.get)


class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.cards = [Card('red', 1), Card('green', 3)]
        self.deck = Deck(self.cards)
        self.emptyDeck = Deck([])
        self.player_with_cards = Player(self.cards)

    def test_init_value(self):
        self.assertEqual(0, self.player.num_cards)
        self.assertEqual(0, len(self.player.cards))

    def test_get_card_from_non_empty_deck(self):
        self.player.get_card(self.deck)
        self.assertEqual('green', self.player.cards[0].color)
        self.assertEqual(3, self.player.cards[0].number)
        self.assertEqual(1, len(self.deck.cards))
        self.assertEqual('red', self.deck.cards[0].color)
        self.assertEqual(1, self.deck.cards[0].number)

    def test_get_card_from_empty_deck(self):
        self.assertRaises(ValueError, self.player.get_card, self.emptyDeck)

    def test_get_score(self):
        self.assertEqual(6, self.player_with_cards.get_score())

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.new_deck = Deck([Card(color, number) for color in \
        CONSTANTS.COLORS for number in \
        range(1, CONSTANTS.NUM_CARDS_EACH_COLOR_IN_DECK + 1)])

    def test_init_value(self):
        self.assertEqual(0, self.game.player0.num_cards)
        self.assertEqual(0, self.game.player1.num_cards)
        # the deck contains all cards in order
        self.assertEqual(len(self.new_deck.cards), len(self.game.deck.cards))
        for i in range(len(self.new_deck.cards)):
            self.assertEqual(self.new_deck.cards[i].color, \
            self.game.deck.cards[i].color)
            self.assertEqual(self.new_deck.cards[i].number, \
            self.game.deck.cards[i].number)



if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=0).run()
