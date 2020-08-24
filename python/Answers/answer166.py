"""
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
    rules = (
        lambda a, b, c, d, e, f, g, h: a + b + c - d - e,
        lambda a, b, c, d, e, f, g, h: a + b + c * 2 - d - e - f,
        lambda a, b, c, d, e, f, g, h: g + a + c - h - f,
        lambda a, b, c, d, e, f, g, h: g + d + e - c - h,
        lambda a, b, c, d, e, f, g, h: a + b + 2 * c + h + - d - 2 * e - f,
        lambda a, b, c, d, e, f, g, h: g + e + f - c - h,
        lambda a, b, c, d, e, f, g, h: h + f - a,
        lambda a, b, c, d, e, f, g, h: d + e - c
    )
    return sum(all(0 <= r(*p) <= 9 for r in rules) for p in product(range(10), repeat=8))


if __name__ == "__main__":
    print("Answer is:", answer())
