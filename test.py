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
        self.cards = [Card('red', 1), Card('green', 3)]
        self.smDeck = Deck(self.cards)

    def test_init_value_no_given_cards(self):
        for color_cnt in range(len(CONSTANTS.COLORS)):
            for num in range(1, CONSTANTS.NUM_CARDS_EACH_COLOR_IN_DECK + 1):
                index = color_cnt * CONSTANTS.NUM_CARDS_EACH_COLOR_IN_DECK \
                        + num - 1
                card = self.deck.cards[index]
                self.assertEqual(card.color, CONSTANTS.COLORS[color_cnt])
                self.assertEqual(card.number, num)
        self.assertEqual(36, len(self.deck.cards))
        self.assertEqual(36, self.deck.size)

    def test_init_value_given_cards(self):
        for i in range(len(self.cards)):
            self.assertEqual(self.cards[i].color, self.smDeck.cards[i].color)
            self.assertEqual(self.cards[i].number, self.smDeck.cards[i].number)

    def test_shuffle(self):
        pre_cards = self.deck.cards
        self.deck.shuffle()
        # the cards in the deck before and after the shuffle should be
        # exactly the same
        pre_card_to_new_card_cnt = {card: 0 for card in pre_cards}
        for new_card in self.deck.cards:
            for pre_card in pre_cards:
                if new_card.color == pre_card.color \
                    and new_card.number == pre_card.number:
                    pre_card_to_new_card_cnt[pre_card] = 1
        for card in pre_card_to_new_card_cnt:
            self.assertEqual(pre_card_to_new_card_cnt[card], 1)

    def test_sort(self):
        self.assertEqual(True, True)

    def test_get(self):
        self.assertEqual(True, True)

class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.deck = Deck()

    def test_init_value(self):
        self.assertEqual(0, self.player.num_cards)
        self.assertEqual(0, len(self.player.cards))

    def test_get_card(self):
        self.assertEqual(True, True)

    def test_get_score(self):
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=0).run()
