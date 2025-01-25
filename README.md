# Tic-Tac-Toe with Minimax AI

## Project Overview
This is a Python implementation of Tic-Tac-Toe featuring an AI opponent using the Minimax algorithm. The AI plays optimally, ensuring it never loses a game when playing perfectly.

## Project Structure
- `runner.py`: Contains the graphical user interface for the game
- `tictactoe.py`: Implements the game logic and AI functionality

## Game Mechanics
The game uses a 3x3 grid where two players (X and O) take turns placing their marks. The objective is to get three of your marks in a row, column, or diagonal.

## Minimax Algorithm
The AI uses the Minimax algorithm to determine the optimal move. This recursive algorithm:
- Explores all possible game states
- Evaluate each potential move
- Chooses the move that maximizes the AI's chances of winning (or minimizing losing)

## Functions in `tictactoe.py`

### Core Game Logic
- `initial_state()`: Returns the initial empty game board
- `player(board)`: Determines the current player's turn
- `actions(board)`: Generates list of possible moves
- `result(board, action)`: Creates a new board state after a move
- `winner(board)`: Checks for a winner
- `terminal(board)`: Checks if the game is over
- `utility(board)`: Assigns utility values (1 for X win, -1 for O win, 0 for draw)

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