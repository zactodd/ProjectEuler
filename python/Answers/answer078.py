"""
Problem 78:
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""
from itertools import takewhile, count
from functools import reduce


def answer(m=1e6):
    k = sum([[i * (3 * i - 1) / 2, i * (3 * i - 1) / 2 + i] for i in range(1, 250)], [])
    p, sign, n, = [1], [1, 1, -1, -1], 1
    while p[-1] > 0:
        px = sum(p[int(n - v)] * sign[i % 4] for i, v in enumerate(takewhile(lambda t: t <= n, k)))
        p.append(px % m)
        n += 1
    return n


if __name__ == '__main__':
    print("Answer is:", answer())
