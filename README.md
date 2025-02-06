# Tic-Tac-Toe AI

## Project Overview

This project implements a classic Tic-Tac-Toe game with an unbeatable AI opponent. The AI uses the Minimax algorithm to make optimal decisions, ensuring that it will either win or draw the game.  It provides a fun game to play and a good example of game AI.

## Project Structure

The project consists of two main Python files:

-   `runner.py`:  Handles the graphical user interface (GUI) using Pygame, user input (mouse clicks), and display of the game board and messages.
-   `tictactoe.py`:  Contains the core game logic and the AI implementation (Minimax algorithm).

## Game Mechanics

Tic-Tac-Toe is played on a 3x3 grid.  Players 'X' and 'O' take turns placing their marks in empty cells. The goal is to get three of your marks in a row (horizontally, vertically, or diagonally). If the board is full and no one has won, the game is a draw.

## Minimax Algorithm

The AI uses the Minimax algorithm to find the best move.  Minimax is a recursive algorithm that:

1.  **Explores:** It explores all possible future game states by recursively simulating moves for both players.
2.  **Evaluates:** It assigns a score to each terminal game state (win, lose, or draw) using the `utility` function.
3.  **Chooses:**  The AI (as the maximizing player) chooses the move that leads to the highest possible score, assuming the opponent (the minimizing player) will always choose the move that leads to the lowest possible score.

## Functions in `tictactoe.py`

### Core Game Logic

-   `initial_state()`: Returns an empty 3x3 board (a list of lists) representing the starting state of the game.
-   `player(board)`: Returns the player whose turn it is ('X' or 'O') given the current `board` state.  'X' always goes first.
-   `actions(board)`: Returns a set of all possible actions (empty cells) on the `board`.  Each action is a tuple `(i, j)` representing the row and column indices.
-   `result(board, action)`: Returns a *new* board state that results from applying the given `action` to the current `board`.  This function does *not* modify the original board.  It also includes error handling for invalid actions.
-   `winner(board)`: Returns the winner of the game ('X' or 'O') if there is one, and `None` otherwise.
-   `terminal(board)`: Returns `True` if the game is over (either someone has won or the board is full), and `False` otherwise.
-   `utility(board)`: Returns the utility of a terminal board state: `1` if 'X' wins, `-1` if 'O' wins, and `0` for a draw.

## Functions in `runner.py`

-   `main()`: Initializes Pygame, sets up the game window and handles the main game loop.
-   `draw_board(screen, board)`: Draws the Tic-Tac-Toe grid and the current marks on the screen.
-   `handle_click(mouse_pos)`: Processes mouse clicks to determine the player's move.
-   `display_message(screen, message)`: Shows messages like "X wins!", "O wins!", or "Draw!".
- `choose_player()`: Handles displaying the initial player choice buttons (X or O).

### AI Logic

-   `minimax(board)`: Implements the Minimax algorithm.  It returns the optimal action (a tuple `(i, j)`) for the current player on the given `board`.
-   `max_value(board)`: A helper function for `minimax`.  It simulates the maximizing player (X) trying to get the highest score.
-   `min_value(board)`: A helper function for `minimax`. It stimulates the minimizing player (O) trying to get the lowest score.

## How to Run the Game

1.  **Prerequisites:**
    *   Python Until 3.12
    *   Pygame library: Install it using pip:
         ```bash
        pip install pygame
        ```
         **(On some systems, you might need to use `pip3 install pygame` or `python3 -m pip install pygame`)**

2.  **Execution:**
    *   Run the game from the command line: `python runner.py`

3.  **Gameplay:**
    *   The game window will open.
    *   You'll be prompted to choose whether to play as 'X' or 'O'. Click the corresponding button.
    *   To make a move, click on an empty cell on the board.
    *   The AI will automatically make its move after you.
    *   The game will continue until there's a winner or a draw.
    *   A "Play Again" button will appear at the end of the game. Clicking this button resets the game board to the initial state, allowing you to play another round. The starting player ('X') remains the same.

## AI Behavior

-   The AI will always play optimally.
-   If both players play perfectly, the game will always end in a draw.
-   The AI will never make a mistake that allows the human player to win.
## Game Rules
- X always starts the game
- Players take turns placing their mark in an empty cell
- The first player to get three marks in a row, column, or diagonal wins
- If all cells are filled without a winner, the game is a draw

## Enjoy the Game!
Challenge the AI and see if you can find a way to win!
