#!/usr/bin/env python
"""
This script plays tic-tac-toe in the terminal.
First player is randomnly selected.
Computer plays ranodomnly.
Player is always 'x'
Computer is always 'o'
Board is labelled 'A0' - 'C2'
Example:
  0 1 2 <-- column labels
A X   o
B   X
C o o X
^
|
|Row labels

The MIT License (MIT)

Copyright (c) 2023 Alice Williams

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import random


class Tic_Tac_Toe:
    def __init__(self):
        self.board: list[list] = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        if (random.random() >= 0.5):
            self.turn: str = "player"
        else:
            self.turn: str = "computer"
        self.num_turns = 0

    def play_player(self):
        self.num_turns += 1
        self.display()
        move = ""
        move_row = -1

        while (True):
            move = input("Pick a move ('A0'-'C2'): ")
            if len(move) == 2:
                if (move[0] == 'A' or move[0] == 'B' or move[0] == 'C') and (move[1] == '0' or move[1] == '1' or move[1] == '2'):
                    if move[0] == 'A':
                        move_row = 0
                    elif move[0] == 'B':
                        move_row = 1
                    elif move[1] == 'C':
                        move_row = 2
                    if self.board[move_row][int(move[1])] != 'x' and self.board[move_row][int(move[1])] != 'o':
                        break

        self.board[move_row][int(move[1])] = 'x'
        self.turn = "computer"

    def play_computer(self):
        self.num_turns += 1
        self.display()
        a = random.randint(0, 2)
        b = random.randint(0, 2)
        while self.board[a][b] == 'x' or self.board[a][b] == 'o':
            a = random.randint(0, 2)
            b = random.randint(0, 2)
        self.board[a][b] = 'o'
        self.turn = "player"

    def display(self) -> None:
        print("current turn is " + self.turn + " number of turns is " + str(self.num_turns))
        print("     0    1    2")
        print("A: " + str(self.board[0]))
        print("B: " + str(self.board[1]))
        print("C: " + str(self.board[2]))

    def is_won(self) -> str:
        # horizontal win conditions
        if (self.board[0][0] == 'x' and self.board[0][1] == 'x' and self.board[0][2] == 'x') or (self.board[0][0] == 'o' and self.board[0][1] == 'o' and self.board[0][2] == 'o'):
            return self.board[0][0]
        if (self.board[1][0] == 'x' and self.board[1][1] == 'x' and self.board[1][2] == 'x') or (self.board[1][0] == 'o' and self.board[1][1] == 'o' and self.board[1][2] == 'o'):
            return self.board[1][0]
        if (self.board[2][0] == 'x' and self.board[2][1] == 'x' and self.board[2][2] == 'x') or (self.board[2][0] == 'o' and self.board[2][1] == 'o' and self.board[2][2] == 'o'):
            return self.board[2][0]
        # vertical win conditions
        if (self.board[0][0] == 'x' and self.board[1][0] == 'x' and self.board[2][0] == 'x') or (self.board[0][0] == 'o' and self.board[1][0] == 'o' and self.board[2][0] == 'o'):
            return self.board[0][0]
        if (self.board[0][1] == 'x' and self.board[1][1] == 'x' and self.board[2][1] == 'x') or (self.board[0][1] == 'o' and self.board[1][1] == 'o' and self.board[2][1] == 'o'):
            return self.board[0][1]
        if (self.board[0][2] == 'x' and self.board[1][2] == 'x' and self.board[2][2] == 'x') or (self.board[0][2] == 'o' and self.board[1][2] == 'o' and self.board[2][2] == 'o'):
            return self.board[0][2]
        # diagnonal win conditions
        if (self.board[0][0] == 'x' and self.board[1][1] == 'x' and self.board[2][2] == 'x') or (self.board[0][0] == 'o' and self.board[1][1] == 'o' and self.board[2][2] == 'o'):
            return self.board[0][0]
        if (self.board[0][2] == 'x' and self.board[1][1] == 'x' and self.board[2][0] == 'x') or (self.board[0][2] == 'o' and self.board[1][1] == 'o' and self.board[2][0] == 'o'):
            return self.board[0][1]
        if (self.board[0][0] == 'x' or self.board[0][0] == 'o') and (self.board[0][1] == 'x' or self.board[0][1] == 'o') and (self.board[0][2] == 'x' or self.board[0][2] == 'o') and (self.board[1][0] == 'x' or self.board[1][0] == 'o') and (self.board[1][1] == 'x' or self.board[1][1] == 'o') and (self.board[1][2] == 'x' or self.board[1][2] == 'o') and (self.board[2][0] == 'x' or self.board[2][0] == 'o') and (self.board[2][1] == 'x' or self.board[2][1]  == 'o') and (self.board[2][2] == 'x' or self.board[2][2] == 'o'):
            return "board full"
        return ""

    def play(self):
        while self.is_won() == "":
            if self.turn == "player":
                self.play_player()
            else:
                self.play_computer()
        if self.is_won() == "board full":
            self.display()
            print("game is a draw.")
            return
        if self.turn == "player":
            win: str = "computer"
        else:
            win: str = "player"
        self.display()
        print(win + " wins the game!")


if __name__ == "__main__":
    game: Tic_Tac_Toe = Tic_Tac_Toe()
    game.play()
