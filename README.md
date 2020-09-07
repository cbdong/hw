# Homework

## Table of content :books:

- [Card game design overview](#card-game-design-overview)
  - [Goal](#goal)
  - [Data structure](#data-structure)

## Card game design overview

### Goal

We would like to design a card game with the following four functions:

1.	Shuffle cards in the deck
2.  Get a card from the top of the deck
3.  Sort cards

Then we implement a game where two players play the game. They will draw 3 cards by taking turns. Whoever has the high score wins the game.

### Data Structure

1. **Card**
  - Variables:
    - color
    - number
  - Init status
    - both the variable are assigned by the parameter, note that color and number needs to be valid values. Color should be in the valid color list, and number should be in the expected range.
2. **Deck**
  - Variables
    - cards, a list of card, used to record the remaining cards in the deck. This is used in a stack behavior. The top of the deck is the last element in the list.
    - size, a int, used to record the number of cards left in the deck
  - Public method
    - shuffle, shuffle the cards in the deck
    - get, get the top card and return it
    - sort, sort the cards in the decking according to the given color order and the number
  - Private method
    - isEmpty, check if the deck is already empty
  - Init status
    - cards, three color red, yellow, green, number from 1 to the max number of the card in each color, or the given cards
    - size, the length of the given cards
3. **Player**
  - Variables
    - cards, a list of card, used to record the cards that the player has
    - num_cards, int, used to record the number of cards that the player has
  - Public method
    - get_card, this function add a card from the top of the deck to the player
    - get_score, this function is used to calculate the score that the player get
  - Init status
    - cards, empty list or given cards
    - num_card, length of cards

4. **Game**
  - Variables
    - player0, the first player
    - player1, the second player
    - deck, the deck of cards that the two players use
  - Public method
    - play, this function play the game where two players get cards in turn and compare the score, return 0 if first player win, return 1 if second player win, return -1 when they get the same score
  - Private method
    - _take_cards: shuffle the deck, two players take the cards from the deck in turn
    - _find_winner: calculate the score of each player, and find the winner
