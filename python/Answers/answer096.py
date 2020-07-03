"""
Problem 96:
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

0 0 3
9 0 0
0 0 1	0 2 0
3 0 5
8 0 6	6 0 0
0 0 1
4 0 0
0 0 8
7 0 0
0 0 6	1 0 2
0 0 0
7 0 8	9 0 0
0 0 8
2 0 0
0 0 2
8 0 0
0 0 5	6 0 9
2 0 3
0 1 0	5 0 0
0 0 9
3 0 0

4 8 3
9 6 7
2 5 1	9 2 1
3 4 5
8 7 6	6 5 7
8 2 1
4 9 3
5 4 8
7 2 9
1 3 6	1 3 2
5 6 4
7 9 8	9 7 6
1 3 8
2 4 5
3 7 2
8 1 4
6 9 5	6 8 9
2 5 3
4 1 7	5 1 4
7 6 9
3 8 2
A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""
from functools import reduce
import pickle, copy
CONSTRAINTS, INVERSE = pickle.load(open('../../resources/constraints.db', 'rb'))
SUDOKU_FILE = "../../resources/sudoku.txt"
with open(SUDOKU_FILE, "r") as f:
    lines = f.readlines()
    GRIDS = [[list(j.rstrip()) for j in lines[i + 1: i + 10]] for i in range(0, len(lines), 10)]


def exactcover(constraints, inverse, solution=[]):
    if not len(inverse):
        yield sorted(solution)
    else:
        for r in inverse[min(inverse, key=lambda k: len(inverse[k]))]:
            solution.append(r)
            cache = trim(constraints, inverse, r)
            for s in exactcover(constraints, inverse, solution):
                yield s
            recover(constraints, inverse, r, cache)
            solution.pop()


def trim(constraints, inverse, r):
    cache = {}
    for j in constraints[r]:
        for i in inverse[j]:
            for k in constraints[i]:
                if k != j:
                    inverse[k].remove(i)
        cache[j] = inverse.pop(j)
    return cache


def recover(constraints, inverse, r, cache):
    for j in reversed(constraints[r]):
        inverse[j] = cache.pop(j)
        for i in inverse[j]:
            for k in constraints[i]:
                if k != j:
                    inverse[k].add(i)


def solve(grid, constraints=CONSTRAINTS, inverse=copy.deepcopy(INVERSE)):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '0':
                trim(constraints, inverse, (i, j, grid[i][j]))
    return list({tuple(s) for s in exactcover(constraints, inverse)})


def answer():
    s = 0
    for g in GRIDS:
        for r in solve(g, constraints=CONSTRAINTS, inverse=copy.deepcopy(INVERSE))[0]:
            g[r[0]][r[1]] = r[2]
        s += int(''.join(g[0][:3]))
    return s


if __name__ == '__main__':
    print("Answer is:", answer())