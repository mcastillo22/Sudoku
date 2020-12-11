# **Sudoku Python Game**

**Play Sudoku!**

Getting Started:

## GUI for Extra Credit: 
Go to: https://repl.it/@mcastillo22/Sudoku

1. Click on "Run" when `main.py` is selected

Note: if an error is displayed, click on "Run" again until it does work

## To Play:

1. Click on a cell, and type in a number 1-9 to place it in the selected cell.

2. Click on 'Verify' at any time to verify the current state of the puzzle.

The program will not verify an incomplete board.

## CLI: 
In the folder 
In the terminal, enter `python3 TerminalGame.py`
Note: This version can run on Flip servers

### To Play:
The game will start with an incomplete puzzle.
   1. Enter a number to place on a square
   2. Enter the location of where the number
      should be placed using the alpha numeric
      board coordinates.
      Do not use spaces in between coordinates!
      For example, `A2`
   3. When the board is filled in completely,
      the game will ask if you'd like to check
      your answers (enter y/n)

   Type 0 at any time to quit

For TAs: \
    When prompted for a number: \
      - Enter `show solution` to fill in puzzle and verify solution \
      - Enter `random fill` to randomly fill empty squares and verify puzzle \
      - Enter `verify` to attempt to verify puzzle \
      - Enter `restart` to restart puzzle

### **Gameplay and Rules**

Sudoku is based on a logical placement of numbers on a n^2 x n^2 grid. \
This game utilizes a 9x9 grid. 

The goal is to fill in this grid so that every row, column, and 3x3 section contains all of the digits between 1 and 9. This means that each row, column, and 3x3 section cannot have any repeating numbers.

An example of a completed puzzle is below:
![alt text](https://www.urbanrim.org.uk/images/sudoku-99.gif)

