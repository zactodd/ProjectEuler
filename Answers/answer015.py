"""
Problem 15:
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

from utils import binomial


def answer():
    n, k = 40, 20
    return binomial(n, k)


if __name__ == '__main__':
    print("Answer is:", answer())
