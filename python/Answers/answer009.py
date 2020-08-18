"""
Problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Solved: O(n^2)
"""
from itertools import combinations


def answer(n=1000):
    return next(a * b * c for a, b in combinations(range(1, n + 1), 2) if a * a + b * b == (c := (n - a - b)) ** 2)


if __name__ == '__main__':
    print("Answer is:", answer())
