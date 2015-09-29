# README.md

"Connect 4" - CS111 Final Project

by Anna Meyer & Alex Olson, Fall 2014

Here is a little background about the project, how it's organized, and how to play:

Background:

• The mission of the final project in CS 111 was to create a computer game that incorporated
some level of computer intelligence. We were expected to complete the project in a partnership
of our choice, and I ended up working with a fellow classmate named Anna. We treated it as a 
pair programming assignment, so in turn we wrote 95% of the code when we were both in front of 
the same computer and constantly took turns at the the keyboard. Both of us had a similar
level of proficiency with Python and contributed equally to the project.

The Game Itself:

• We created a game of Connect 4! The player first chooses their tile color and then they 
take turns with the computer placing tiles on the board. Whoever gets four in a row first
wins. If there are no four in a rows at the end of the game, it is a tie game.

• Our program makes use of 4 classes - button, player, computer, and lists. The button
class (stored in a separate module) controls the buttons that label the columns. The
player and computer classes are in charge of implementing the player and computer's
turns. The list class stores the list representation of the board. It updates and
manipulates this data to make it possible to check for four in a rows in every direction.

• There are also several functions not part of a class. DrawButtons and addBoard design
the graphics window. ChooseColor lets the user choose what color tile to use. Find4(List)
is implemented to check whether there are any four in a rows (if so, it will declare a
winner) and find3(list) checks for three in a rows so that the computer can place its
next tile more intelligently. DiplayResult(window, outcome) prints the outcome of the
game in the graphics window once someone has won, or when the the game is a tie. 
The game function executes the bulk of the game by controlling when it is each player's turn 
and calling on displayResult at the appropriate time.

• Our program works! The computer is not incredibly smart but is much smarter than
it was orignally. Rather than always playing a random tile, the computer checks whether or not 
it can complete its own four in a row or block the player from getting a four in a row. 

≈≈ INSTRUCTIONS FOR GAMEPLAY ≈≈

1. Place Connect4.py, button.py, and graphics.py in the same folder.
2. In terminal, run Connect4.py. 
3. Wait a few seconds. Then choose your tile color by clicking on one of the
   colored boxes. 
4. In the Connect 4 window, click on one of the numbered buttons to place a tile
   in that column.
5. After you place a tile, the computer will then play a tile.
6. Continue placing tiles with the goal of getting four in a row of your tile color.
7. If you want an additional challenge, try to make the game a tie.

≈≈ Have Fun! ≈≈
