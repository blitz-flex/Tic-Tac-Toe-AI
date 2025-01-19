"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0

    # Iterate through each row and each cell on the board
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    # If X's count is greater than O's count, O will make the next move
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Creating an empty set to store possible actions.
    actions_set = set() 
    # 3x3 check
    for i in range(3):
        for j in  range(3):
            if board[i][j] == EMPTY:    # If the tray is empty
                actions_set.add((i,j))  #The pair of actions (i, j) must be added to this cell.

    return actions_set   # Returns the set of all possible actions.


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        raise ValueError ("action canot br None")
    
    
    i, j = action    # Unpack the action tuple into row (i) and column (j)
    if board[i][j] != EMPTY:
        raise ValueError("Invalid action: Cell is not empty")
    
    # Create board copy
    new_board = [row[:] for row in board]

    # Place the current player's symbol (X or O) on the new board
    new_board[i][j] = player(board)

    return new_board

    # Example
    """
    Input
    board = [
    [X, O, EMPTY],
    [EMPTY, X, O],
    [O, EMPTY, EMPTY]
    ]

    Action: (2, 1)
    Check if board[1][0] is EMPTY ✓
    Make copy

    new_board = [
    [X, O, EMPTY],
    [EMPTY, X, O],
    [O, EMPTY, EMPTY]
    ]

    Place X (since X=2 moves, O=2 moves)
    new_board[1][0] = X

    Output
    new_board = [
    [X, O, EMPTY],
    [X, X, O],
    [O, EMPTY, EMPTY]
    ]
    """
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check rows for a winner
    for row in board:
        if row[0] is not None and row[0] == row[1] == row[2]:
            return row[0]
        
    #Check colums for a winner
    for col in range(3):
        if board[0][col] is not None and board[0][col] == board[1][col] ==board[2][col]:
            return board[0][col]
    
    # check diagonals for a winner
    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    # no winner found
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner (board) is not None:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
