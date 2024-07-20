# Tic-Tac-Toe Project Description


## Overview:

The Tic-Tac-Toe project is a classic game implemented to run human vs. AI game. The AI uses an optimized algorithm to ensure that it is unbeatable, leveraging Minimax with Alpha-Beta Pruning. The game features a user-friendly graphical interface that visually represents the game board, providing a clear and interactive experience for players.

## Features

####  Game Modes:

Human vs. AI: A single player competes against an AI opponent. The AI uses the Minimax algorithm with Alpha-Beta Pruning to make optimal moves, ensuring it is always a challenging opponent.

#### Game Board:

A 6 X 6 grid is used to represent the Tic-Tac-Toe board.
Each cell can be clicked to place a mark, with immediate visual feedback to show the current state of the game.
AI Implementation:

#### Minimax Algorithm:

The AI evaluates all possible moves and chooses the one that maximizes its chances of winning or minimizes the opponent’s chances.
Alpha-Beta Pruning: Optimizes the Minimax algorithm by eliminating branches in the game tree that do not need to be explored, improving performance.
Visual Enhancements:

#### Graphical User Interface (GUI): 

Developed using a library like Tkinter or Pygame, providing a clear and intuitive interface.
Visual Feedback: Highlighted cells when clicked, with visual indicators for winning lines or a draw.
Animations: Smooth transitions and animations for placing marks and updating the board state.
Game Logic:

#### Win Conditions:

Checks for three consecutive marks horizontally, vertically, or diagonally.
Draw Condition: Detects when all cells are filled and no player has won.
User Interface:

#### Start Menu:

Allows players to choose between human vs. human or human vs. AI modes.

#### Restart and Quit Options:

Buttons to restart the game or quit, with confirmation prompts to avoid accidental exits.
