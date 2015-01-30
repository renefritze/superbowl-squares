Superbowl Squares!
=================
Python script to help you and your friends play superbowl squares this Sunday.

What the eff is Superbowl Squares?
================================
A super fun way to bet on the superbowl!

- the board starts off as an empty 10x10 grid
- the axes are labeled 0-9
- each team is assigned to an axis (e.g. Patriots on left, Seahawks on top)
- each participant is assigned up to 5 squares
- pick a buy in for a square ($5/square is a good choice)
- all of the squares should be filled before the game starts
- at the end of each quarter, the score of the game determines a winner
- the squares reflect the last digit of the score of the game
    - (7, 2) is the winning square for scores 7 - 22, 17 - 12, etc.
- payouts happen at the end of each quarter and can vary
    - e.g. winner of 1st/2nd/3rd/4th quarters respectively: $50/$100/$50/$300 


What does this script do?
========================
It randomly generates the board (squares) and outputs it into a csv file
(i.e. it saves you the hassle of manual entry)

How do I use it?
=================
Just edit the names and number of entries in the file and run it.

For the less techincal:

- save sbsq.py to your Desktop
- edit the file with the names you want
- open up a terminal
- enter these commands:

```
    $ cd ~/Desktop
    $ chmod +x sbsq.py
    $ python sbsq.py
```

- The file superbowl_squares.csv will be saved on your computer
- You can open it with excel or google docs

