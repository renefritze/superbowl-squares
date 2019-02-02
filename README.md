Superbowl Squares!
=================
Python script to help you and your friends play superbowl squares this Sunday.

What the eff is Superbowl Squares?
================================
A super fun way to bet on the superbowl!

- the board starts off as an empty 10x10 grid
- the axes are labeled 0-9
- each team is assigned to an axis (e.g. Patriots on left, Seahawks on top)
- each participant is assigned 100/count(participants) squares
- pick a buy in for a person
- all of the squares should be filled before the game starts
- at the end of each quarter, the score of the game determines a winner
- the squares reflect the last digit of the score of the game
    - (7, 2) is the winning square for scores 7 - 22, 17 - 12, etc.
- payouts happen at the end of each quarter and can vary
    - e.g. winner of 1st/2nd/3rd/4th quarters respectively: $50/$100/$50/$300 


What does this script do?
========================
It randomly generates the board (squares) and outputs it into a csv file, 
generates a latex file with tables for each participant and.

How do I use it?
=================
Clone this repository, edit 'REAL_NAMES' in sbsq.py, run ```make```, 
print superbowl_squares.pdf
