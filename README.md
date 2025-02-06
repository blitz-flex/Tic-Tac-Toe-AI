# Tic-Tac-Toe  AI

## Project Overview

This project is a Python implementation of the classic game Tic-Tac-Toe, featuring an unbeatable AI opponent.  The AI employs the Minimax algorithm with Alpha-Beta Pruning to ensure optimal decision-making, guaranteeing it will never lose. This project serves as both an engaging game to play and an excellent educational resource for learning about game AI principles.

## Project Structure

- `runner.py`: The main executable file.  It handles the graphical user interface (GUI) using Pygame, user input, and displaying the game.
- `tictactoe.py`:  Contains the core game logic and the AI's implementation (Minimax with Alpha-Beta Pruning).


## Game Mechanics
Tic-Tac-Toe is played on a 3x3 grid. Two players, typically designated as 'X' and 'O', take turns placing their respective marks in empty cells. The objective is to be the first player to align three of their marks in a row, either horizontally, vertically, or diagonally. If all cells are filled and no player has achieved a winning alignment, the game is declared a draw.

## Minimax Algorithm
The AI uses the Minimax algorithm to determine the optimal move. This recursive algorithm:
- Explores all possible game states
- Evaluate each potential move
- Chooses the move that maximizes the AI's chances of winning (or minimizing losing)

## Functions in `tictactoe.py`

### Core Game Logic
- `initial_state()`:  This function initializes and returns an empty 3x3 Tic-Tac-Toe game board. The board is represented as a list of lists.
  
- `player(board)`: Given the current state of the `board`, this function determines and returns whose turn it is to play. It returns 'X' or 'O' to indicate the current player.
  
- `actions(board)`:  This function identifies all possible moves available on the `board` in its current state. It returns a set of empty cells, with each cell represented as a `(row, col)` tuple.
  
- `result(board, action)`:  This function takes the current `board` state and a player's `action` (move) as input. It returns a new board state that reflects the result of applying the given `action` to the provided `board`. Crucially, this function operates without modifying the original `board` and includes validation to ensure the `action` is valid.
  
- `winner(board)`:  This function checks the `board` to determine if a player has won the game. It returns 'X' if player X has won, 'O' if player O has won, and `None` if there is no winner in the current board state.
  
- `terminal(board)`: This function assesses whether the game has reached a terminal state, meaning the game is over. It returns `True` if the game has ended (either by a win or a draw) and `False` otherwise.
  
- `utility(board)`:  This function evaluates a final `board` state when the game is over. It returns a utility score: `1` if 'X' wins, `-1` if 'O' wins, and `0` in the case of a draw.

### AI Logic
- `minimax(board)`: Implements the Minimax algorithm to choose the optimal move

## How to Play
1. Ensure you have Python installed
2. Run the game with: `python runner.py`
3. Play against the AI by clicking on the board
4. The AI will make optimal moves to either win or force a draw

## AI Behavior
- If both players play perfectly, the game will always end in a draw
- The AI never makes a mistake that would allow the human player to win

## Requirements
- Python 3.x
- Pygame library (for graphical interface)

## Installation
1. Clone the repository
2. Install required dependencies: `pip install pygame`
3. Run the game: `python runner.py`

## Game Rules
- X always starts the game
- Players take turns placing their mark in an empty cell
- The first player to get three marks in a row, column, or diagonal wins
- If all cells are filled without a winner, the game is a draw

## Enjoy the Game!
Challenge the AI and see if you can find a way to win!
