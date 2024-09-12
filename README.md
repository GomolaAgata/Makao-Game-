# Makao-Game

Project realised during **Fundamentals of Python programming** course in Polish-Japanese Academy of Information Technology

## Overview

Makao is a popular card game

## Game Rules

The rules of Makao:

   - Each player starts with 5 cards.
   - The goal of the game is to get rid of all your cards.

 **Playing a Card**:
   - Players must play a card that matches the value or color of the top card on the pile.

 **Special Cards**:
   - **2 and 3**: These cards force the next player to draw two or three cards from the deck. If the next player has a 2 or 3, they can pass the penalty to the following player.
   - **4**: Known as the "Skip" or "Pause" card. Playing a 4 skips the next player's turn. If another 4 is played, the skip moves to the next player.
   - **Kings**: The King of Hearts and King of Clubs are "War" cards. Playing one of these forces the next player to draw 5 cards from the deck.
   - **Ace**: Allows the player to choose a specific color.
   - **Jack**: Allows the player to choose a specific card value.

 **Drawing a Card**:
   - If a player cannot or does not want to play a card, they must draw one from the deck. If the drawn card can be played, the player may do so immediately.

   - When playing the second-to-last card, the player must say "Makao" after placing the card. If they fail to do so, they will be forced to draw 5 cards.

## User Interface

The game interface is in Polish and provides a menu with the following options:

1. **Display Game Rules**:
   - Shows the rules of the game to help players understand how to play.

2. **Display Ranking**:
   - Displays the current ranking of players based on their performance. Rankings are saved in a separate file.

3. **Start a New Game**:
   - Begins a new game session.

4. **Exit**:
   - Exits the game.

## Console Colors

The console output is colorized using the `colorama` library, which adds visual appeal to the game.

