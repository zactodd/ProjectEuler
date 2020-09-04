"""
Problem 5:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Solved: O(n)
"""

from math import gcd
from functools import reduce


def answer(n=20):
    return reduce(lambda x, y: x * y // gcd(y, x), range(1, n + 1), 1)


if __name__ == '__main__':
    print("Answer is:", answer())

