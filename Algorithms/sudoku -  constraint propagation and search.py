import time

# In this essay I tackle the problem of solving every Sudoku puzzle.
# It turns out to be quite easy (about one page of code for the main idea and two pages for embellishments) using two ideas:
# constraint propagation and search.

                        # A1 A2 A3| A4 A5 A6| A7 A8 A9    4 . . |. . . |8 . 5     4 1 7 |3 6 9 |8 2 5
                        #  B1 B2 B3| B4 B5 B6| B7 B8 B9    . 3 . |. . . |. . .     6 3 2 |1 5 8 |9 4 7
                        #  C1 C2 C3| C4 C5 C6| C7 C8 C9    . . . |7 . . |. . .     9 5 8 |7 2 4 |3 1 6
                        # ---------+---------+---------    ------+------+------    ------+------+------
                        #  D1 D2 D3| D4 D5 D6| D7 D8 D9    . 2 . |. . . |. 6 .     8 2 5 |4 3 7 |1 6 9
                        #  E1 E2 E3| E4 E5 E6| E7 E8 E9    . . . |. 8 . |4 . .     7 9 1 |5 8 6 |4 3 2
                        #  F1 F2 F3| F4 F5 F6| F7 F8 F9    . . . |. 1 . |. . .     3 4 6 |9 1 2 |7 5 8
                        # ---------+---------+---------    ------+------+------    ------+------+------
                        #  G1 G2 G3| G4 G5 G6| G7 G8 G9    . . . |6 . 3 |. 7 .     2 8 9 |6 4 3 |5 7 1
                        #  H1 H2 H3| H4 H5 H6| H7 H8 H9    5 . . |2 . . |. . .     5 7 3 |2 9 1 |6 8 4
                        #  I1 I2 I3| I4 I5 I6| I7 I8 I9    1 . 4 |. . . |. . .     1 6 4 |8 7 5 |2 9 3

# We can implement the notions of units, peers, and squares in the programming language
def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

units = dict((s, [u for u in unitlist if s in u])  for s in squares)

peers = dict( (s, set(sum(units[s],[]))-set([s]))  for s in squares )

def test():
    "A set of unit tests."
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                           ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                           ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                               'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                               'A1', 'A3', 'B1', 'B3'])
    print ('All tests pass.')

# Here is the code to parse a grid into a values dict:
def parse_grid(grid):
    """Convert grid to a dict of possible values, {square: digits}, or
    return False if a contradiction is detected."""
    ## To start, every square can be any digit; then assign values from the grid.
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False ## (Fail if we can't assign d to square s.)
    return values

def grid_values(grid):
    "Convert grid into a dict of {square: char} with '0' or '.' for empties."
    chars = [c for c in grid if c in digits or c in '0.']
    assert len(chars) == 81
    return dict(zip(squares, chars))

# Constraint Propagation
#
# The function parse_grid calls assign(values, s, d). We could implement this as values[s] = d,
# but we can do more than just that. Those with experience solving Sudoku puzzles know that there
# are two important strategies that we can use to make progress towards filling in all the squares:
# (1) If a square has only one possible value, then eliminate that value from the square's peers.
# (2) If a unit has only one possible place for a value, then put the value there.
# As an example of strategy (1) if we assign 7 to A1, yielding {'A1': '7', 'A2':'123456789', ...},
# we see that A1 has only one value, and thus the 7 can be removed from its peer A2
# (and all other peers), giving us {'A1': '7', 'A2': '12345689', ...}.
# As an example of strategy (2), if it turns out that none of A3 through A9 has a 3 as a possible value,
# then the 3 must belong in A2, and we can update to {'A1': '7', 'A2':'3', ...}.
# These updates to A2 may in turn cause further updates to its peers, and the peers of those peers, and so on.
# This process is called constraint propagation.
# The function assign(values, s, d) will return the updated values (including the updates from constraint propagation),
# but if there is a contradiction--if the assignment cannot be made consistently--then assign returns False.
# For example, if a grid starts with the digits '77...' then when we try to assign the 7 to A2,
# assign would notice that 7 is not a possibility for A2, because it was eliminated by the peer, A1.
#
# It turns out that the fundamental operation is not assigning a value,
# but rather eliminating one of the possible values for a square, which we implement with eliminate(values, s, d).
# Once we have eliminate, then assign(values, s, d) can be defined as "eliminate all the values from s except d".


def assign(values, s, d):
    """Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def eliminate(values, s, d):
    """Eliminate d from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected."""
    if d not in values[s]:
        return values ## Already eliminated
    values[s] = values[s].replace(d,'')
    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
    	return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0 :
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1 :
            # d can only be in one place in unit; assign it there
                if not assign(values, dplaces[0], d):
                    return False
    return values

# Now before we can go much further, we will need to display a puzzle:

def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print (''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF': print (line)
    print()

# Now we're ready to define the solve function in terms of the search function:

def solve(grid):
    return search(parse_grid(grid))

def search(values):
    "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in squares):
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d))
		for d in values[s])

def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False

# Loading an external File :
def load_file_3(filename) :
    matrix=''
    f = open(filename, 'r')
    text = f.read()
    for row in text.split('\n'):
        matrix+=row
    return matrix

filename = "sudoku - backtracking - test_matrix.txt"

grid = load_file_3(filename)
print(' Initial grid : ', grid, '\n\n')

t1  = time.time()

display(parse_grid(grid))

t2  = time.time()
print('\nCompleted in :', round((t2-t1)*1000,6), 'ms\n\n')