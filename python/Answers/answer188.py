"""
Problem 188:
The hyperexponentiation or tetration of a number a by a positive integer b, denoted by a↑↑b or ba, is recursively defined by:

a↑↑1 = a,
a↑↑(k+1) = a(a↑↑k).

Thus we have e.g. 3↑↑2 = 33 = 27, hence 3↑↑3 = 327 = 7625597484987 and 3↑↑4 is roughly 103.6383346400240996*10^12.

Find the last 8 digits of 1777↑↑1855.
"""

import sys
from python.utils import totient


def tetration_mod(x, y, m):
    return x % m if y == 1 else pow(x, tetration_mod(x, y - 1, totient(m)), m)


def answer(x=1777, y=1855, m=10 ** 8):
    sys.setrecursionlimit(y + 30)
    return tetration_mod(x, y, m)


if __name__ == '__main__':
    print("Answer is:", answer())
