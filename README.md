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

1. Class Card
  The class Card has two variables:
  - color
  - number
2. Class Deck
  It two variables
  - cards, a list of card, used to record the remaining cards in the deck
  - size, a int, used to record the number of cards left in the deck
  It has the following public method:
  - shuffle
  - get
  - sort
  It has the following private method:
  - isEmpty
  In the following part of the doc, we will discuss how to implement the methods for the deck.

## Shuffle method

## Get method

## Sort method

## Two players play the game

### Player data structure
It contains the following variable:
- cards, a list of card, used to record the cards that the player has
- num_card, int, used to record the number of cards that the player has
It contains the following method:
- get_card, this function add a card from the top of the deck to the player
- get_score, this function is used to calculate the score that the player get 
