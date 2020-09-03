from card_game import Card, Deck, Player
import CONSTANTS
import unittest

class CardTestCase(unittest.TestCase):
    def setUp(self):
        self.card = Card('red', 12)

    def test_value(self):
        self.assertEqual(self.card.color, 'red', 'wrong color assigned')

    def test_color_value_exception(self):
        self.assertRaises(ValueError, Card, 'happy', 12)

    def test_number_value_exception(self):
        self.assertRaises(ValueError, Card, 'red', 13)

class DeckTestCase(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init_value(self):
        for color_cnt in range(len(CONSTANTS.COLORS)):
            for num in range(1, CONSTANTS.NUM_CARDS_EACH_COLOR_IN_DECK + 1):
                index = color_cnt * CONSTANTS.NUM_CARDS_EACH_COLOR_IN_DECK \
                        + num - 1
                card = self.deck.cards[index]
                self.assertEqual(card.color, CONSTANTS.COLORS[color_cnt])
                self.assertEqual(card.number, num)
        self.assertEqual(36, len(self.deck.cards))
        self.assertEqual(36, self.deck.size)

    def test_shuffle(self):
        self.assertEqual(True, True)

    def test_sort(self):
        self.assertEqual(True, True)

    def test_get(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    cardSuite = unittest.TestLoader().loadTestsFromTestCase(CardTestCase)
    alltests = unittest.TestSuite([cardSuite])

    unittest.TextTestRunner(verbosity=2).run(cardSuite)
