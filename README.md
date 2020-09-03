# Homework

## Table of content :books:

- [Card game design overview](#card-game-design-overview)
  - [Goal](#goal)
  - [Data structure](#data-structure)
- [Shuffle method](#shuffle-method)
- [Get method](#get-method)
- [Sort method](#sort-method)
- [Two players play the game](#two-players-play-the-game)

## Card game design overview

### Goal

We would like to design a card game with the following four functions:

1.	Shuffle cards in the deck
2.  Get a card from the top of the deck
3.  Sort cards

Then we implement a game where two players play the game. They will draw 3 cards by taking turns. Whoever has the high score wins the game.

### Data Structure

1. **Class Card**
  - Variables:
    - color
    - number
  - init status
    - both the variable are assigned by the parameter
2. **Class Deck**
  - Variables
    - cards, a list of card, used to record the remaining cards in the deck
    - size, a int, used to record the number of cards left in the deck
  - public method
    - shuffle, shuffle the cards in the deck
    - get, get the top card and return it
    - sort, sort the cards in the decking according to the given color order and the number
  - private method
    - isEmpty, check if the deck is already empty
  - init status
    - cards, three color red, yellow, green, number from 1 to 12
    - size = 36
3. **Player**
  - Variables
    - cards, a list of card, used to record the cards that the player has
    - num_card, int, used to record the number of cards that the player has
  - public method
    - get_card, this function add a card from the top of the deck to the player
    - get_score, this function is used to calculate the score that the player get
  - init status
    - cards, empty
    - num_card, 0

## Shuffle method

## Get method

## Sort method

## Two players play the game
