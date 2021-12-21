"""
Problem 70:
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""

from python.utils import totients, is_perm
from functools import reduce


def answer(limit=10 ** 7):
    return reduce(lambda x, y: (ts[y[0]], y[0]) if is_perm(*y) and x[0] * y[0] < x[1] * y[1] else x,
                  enumerate((ts := totients(limit))[2:], 2), (0, 1))[0]


if __name__ == '__main__':
    print("Answer is:", answer())
