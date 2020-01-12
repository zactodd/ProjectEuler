"""
Question 166:
A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9.

It can be seen that in the grid

6 3 3 0
5 0 4 3
0 7 1 4
1 2 4 5

the sum of each row and each column has the value 12. Moreover the sum of each diagonal is also 12.

In how many ways can you fill a 4x4 grid with the digits d, 0 ≤ d ≤ 9 so that each row, each column, and both diagonals have the same sum?
"""
from itertools import product


def answer():
    pool = [[] for _ in range(37)]
    for p in product(range(10), repeat=4):
        pool[sum(p)].append(p)

    count = 0
    for s, ls in enumerate(pool):
        dd = {}
        for a in ls:
            for b in ls:
                key = (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3], a[0] + b[1], a[3] + b[2])
                dd.setdefault(key, 0)
                dd[key] += 1
        for ii, c in dd.items():
            key = (s - v for v in ii)
            count += c * dd.get(key, 0)
    return count


if __name__ == '__main__':
    print("Answer is:", answer())
