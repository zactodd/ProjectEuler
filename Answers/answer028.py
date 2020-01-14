"""
Problem 28:
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def answer():
    n = 1001
    d = (n - 1) // 2
    return (16 * d ** 3 + 30 * d ** 2 + 26 * d + 3) // 3


if __name__ == '__main__':
    print("Answer is:", answer())
