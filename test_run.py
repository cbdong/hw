from card_game import Card, Deck, Player, Game
import CONSTANTS
def print_deck(deck):
    for card in deck.cards:
        print(card.color, card.number)

deck = Deck()
deck.shuffle()

player0 = Player()
player0.get_card(deck)


for card in player0.cards:
    print(card.color, card.number)
