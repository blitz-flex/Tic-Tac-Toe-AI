# Tic-Tac-Toe AI

## Project Overview
This Python implementation of Tic-Tac-Toe features an AI opponent using the Minimax algorithm. The AI plays optimally, ensuring it never loses a game when playing perfectly.

## Project Structure
- `runner.py`: Contains the graphical user interface for the game
- `tictactoe.py`: Implements the game logic and AI functionality

## Game Mechanics
The game uses a 3x3 grid. Two players (X and O) take turns placing their marks. The objective is to get three of your marks in a row, column, or diagonal.

## Minimax Algorithm
The AI uses the Minimax algorithm to determine the optimal move. This recursive algorithm:
- Explores all possible game states
- Evaluate each potential move
- Chooses the move that maximizes the AI's chances of winning (or minimizing losing)

## Functions in `tictactoe.py`