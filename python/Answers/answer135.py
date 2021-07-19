"""
Problem 135:
Given the positive integers, x, y, and z, are consecutive terms of an arithmetic progression, the least value of the positive integer, n, for which the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 27:

342 − 272 − 202 = 122 − 92 − 62 = 27

It turns out that n = 1155 is the least value which has exactly ten solutions.

How many values of n less than one million have exactly ten distinct solutions?
"""
from collections import Counter
from itertools import takewhile


def answer(limit=10 ** 6):
    s = Counter(i for m in range(1, limit * 2)
                for i in takewhile(lambda i: i < limit,
                                   map(lambda k: (m - k) * (k * 5 - m), range(m // 5 + 1, (m + 1) // 2))))
    return sum(v == 10 for v in s.values())


if __name__ == '__main__':
    print("Answer is:", answer())
