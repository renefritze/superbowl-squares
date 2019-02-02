#!/usr/bin/python
# Alex Bok

import random
import csv
from jinja2 import Template
import string

    
TOPLEFT = '∅'
NOBODY = 'L'
REAL_NAMES = ['Tom','Jenny','Maik','Damian','René','Hakan','Repping','Nils',]


'''
Don't edit below this point
'''

def initialize_board():
	board = [[0 for x in range(11)] for x in range(11)]
	for i in range(1, 11):
		board[i][0] = i - 1
		board[0][i] = i - 1
	board[0][0] = TOPLEFT
	return board


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
	with open(fp, 'wt') as outfile:
		csv.writer(outfile).writerows(b)


def name_table(p, fp):
    def _tuple(n):
        if n == 'L':
            return (n, 'XXXX', NOBODY)
        return (n, '\_ '*4, '\_\_')
    tb = [ _tuple(n) for n in p]
    with open(fp, 'wt') as outfile:
        out = csv.writer(outfile)
        out.writerow([ "Name", "Zahl", "Kürzel"])
        out.writerows(tb)
          
          
def tbl_tex(p, fn):
    tpl = '''
    {% for name in names %}
    \\newsavebox{\Box{?name?}}
    \sbox{\Box{?name?}}{\pgfplotstabletypeset[%    
    before row=\hline,every last row/.style={after row=\hline},
    column type/.add={|}{},
    every last column/.style={column type/.add={}{|} },
postproc cell content/.append code={\ifnum \pdf@strcmp{#1}{{?name?}}=0 %
    \pgfkeys{/pgfplots/table/@cell content/.add={\cellcolor{red!10!white} }{} }\\fi},
]{\squarestable}}
\\begin{tikzpicture}
    \\node[inner sep=0pt] (rams) at (-2.5,0)
    {\\includegraphics[width=.25\\textwidth]{rams.jpg}};
    \\node[inner sep=0pt] (patriots) at (4,4.5)
    {\\includegraphics[width=.25\\textwidth]{patriots.jpg}};
    \\node[inner sep=0pt] (table) at (4,0)
    {\\usebox{\Box{?name?}}};
\\end{tikzpicture}
    \\\\\\\\\\\\
    {% endfor %}
    '''
    with open(fn, 'wt') as out:
        tpl = Template(tpl, comment_start_string='{=', variable_start_string='{?', variable_end_string='?}')
        names = list(p.keys())
        out.write(tpl.render(names=names))
        
    
def make_participants(p):
    shorts = [x for x in string.ascii_uppercase if x != NOBODY]
    lp = len(p)
    pd = {shorts[i]: 100//lp for i in range(lp)}
    pd[NOBODY] = 100-(100//lp)*lp
    return pd
    

if __name__=="__main__":
	b = initialize_board()
	participants = make_participants(REAL_NAMES)
	generate_squares(participants, b)
	print_to_csv("squares.csv", b)
	name_table(REAL_NAMES, "people.csv")
	tbl_tex({p:l for p,l in participants.items() if p != 'L'}, 'tables.tex')

