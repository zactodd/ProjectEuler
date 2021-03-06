"""
Problem 15:
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

Solved: O(n)
"""

from python.utils import binomial


def answer(n=40, k=20):
    return binomial(n, k)


if __name__ == '__main__':
    print("Answer is:", answer())
