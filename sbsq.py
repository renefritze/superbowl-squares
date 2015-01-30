#!/usr/bin/python
# Alex Bok

import random
import csv

MAX_ENTRIES = 5
PARTICIPANTS = {

	'alex'		: 5,
	'isaac'		: 5,
	'aron'		: 5,
	'ryan'		: 3,
	'eric'		: 5,
	'finn'		: 5,
	'matt'		: 4,
	'chris'		: 5,
	'ezra'		: 5,
	'nick'		: 3,
	'zach'		: 2,
	'mike'		: 5,
	'ellen'		: 5,
	
	'john'		: 5,
	'jim'		: 5,
	'kc'		: 5,
	'robbie'	: 5,
	'mom'		: 5,
	'dad'		: 5,
	'jack'		: 5,
	'jane'		: 3,
	'max'		: 5

}

'''
Don't edit below this point
'''

def initialize_board():
	board = [[0 for x in range(11)] for x in range(11)]
	for i in range(1, 11):
		board[i][0] = i - 1
		board[0][i] = i - 1
	board[0][0] = ""
	return board

def print_board(board):
	for row in board:
		for val in row:
			print '{:7}'.format(val),
		print	

def check_participants(p):
	total = 0
	for k in p:
		if p[k] < 0 or p[k] > 5 or not isinstance(p[k], int):
			raise Exception("Illegal value for %s." % k)
		total += p[k]
	if total != 100:
		raise Exception("Total squares: %d, needed: 100." % total)

def generate_squares(p, b):

	n = len(b) - 1
	m = len(b[0]) - 1

	finished = []

	for k in p:
		num_entries = p[k]
		while num_entries > 0:
			row = random.randint(1, n)
			col = random.randint(1, m)
			if isinstance(b[row][col], int) and b[row][col] == 0:
				b[row][col] = k
				num_entries -= 1


def print_to_csv(fp, b):
	with open(fp, 'wb') as outfile:
		csv.writer(outfile).writerows(b)


if __name__=="__main__":
	b = initialize_board()
	check_participants(PARTICIPANTS)
	generate_squares(PARTICIPANTS, b)
	print_to_csv("superbowl_squares.csv", b)

