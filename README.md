# Connect-Four

### Overview

This project implements a Connect Four game with various player options, including an AI player that utilizes alpha-beta pruning and expectimax search for intelligent decision-making.

### Files:

1) ConnectFour.py: Contains UI.
2) Player.py: Contains game logic (algorithms).

### AI player Implementation:
1) Uses alpha-beta pruning and minimax to choose the best move for the AI.
2) Uses expectimax search to evaluate possible moves when it's the opponent's turn (minimizing player).

### How To Play

1) Open a command prompt or terminal and navigate to the directory containing the game files
2) Run the game using the following command: python ConnectFour.py arg1 arg2
Replace arg1 and arg2 with your desired player types:
AI: Artificial intelligence opponent
Human: Human player
Random: Random AI opponent

### Examples:

python ConnectFour.py human random: For Human Vs Random.

### GamePlay:

1) If playing against a human, players take turns choosing a column to drop their piece.
2) When playing against an AI or Random AI, the computer will automatically choose a column after your turn.
3) Click "Enter" or press the Enter key after entering your desired column number.
4) The board state will be displayed after each turn.
5) The game continues until one player achieves four pieces in a row (horizontally, vertically, or diagonally), or the board is filled.












