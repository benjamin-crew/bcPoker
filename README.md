# bcPoker
No limit hold'em poker created in Python.

# Description
The aim of this project is to first of all create a working game of poker. If I can achieve this, then I'd like to keep adding features and take it as far as I can. A good outcome would be to get this hosted on a website and allow people to join the table and play.

This is a fairly difficult project for a beginner like myself, but lets see what I can do!

# Learning Objectives
- Become more familiar with Python.
- Look into Django and Flask and understand the differences.
- Create a website to host the game.
- Research how to allow for multiplayer.

# How to play Poker
This is a list of the rules or general flow of poker, but it also works as a flow for the program itself:

### Requirements
- 2-7 Players
- 52 Card Deck
- Poker Chips/Money
- Dealer button
- Small blind button
- Big blind button

### How to play
- Randomly select a player to be the dealer for the first hand. Denote that player with the dealer button.
- Dealer shuffles the cards.
- Player to the left of the dealer is given the small blind button. This player posts the small blind bet.
- Player two places to the left of the dealer is given the big blind button. This player posts the big blind bet.
- Dealer deals two cards face-down to each player.
- First round of betting begins, starting with the player to the left of the big blind and continuing clockwise.
- Each player can call and/or raise the blind bet, or fold their hand. They can also go "all-in", staking their entire hand. A player can call by placing a bet of the same amount as the players "all-in".
- Dealer "burns", or discards, one card, then turns up three communal cards, called the "flop", in the middle of the table.
- Second round of betting begins, starting with the player to the left of the dealer and continuing clockwise.
- Dealer burns another card and turns up a fourth communal card, called the "turn".
- Third round of betting follows.
- Dealer burns another card and turns up the fifth commual card, called the "river".
- Fourth round of betting follows.
- If everyone but a single player has folded, that player wins and does not need to reveal their cards.
- If two or more players remain, those players reveal their cards in what is called the "showdown".
- The winner is the player with the highest five-card poker hand made up of any combination of the five community cards and the players two private cards.
- If two or more players have the same winning hand, the pot is divided evenly.
- In a showdown, the last player to call the bet shows their cards last. If nobody has bet, it's the person to the left of the dealers button.
- When the hand finishes, the buttons move one space clockwise.

# TODO:
- [ ] Create general game logic
    - [x] Get input of how many players and add them to dictionary
        - [ ] May need to change this to classes
    - [x] Assign players money
    - [x] Create dealer, small and big blind references
    - [x] Assign ante to blinds
    - [x] Shuffle deck
    - [x] Choose dealer for first hand
    - [ ] Deal the hand