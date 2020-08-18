"""
Problem 6:
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Solved: O(1)
"""

from python.utils import gauss


def gauss_squares(n):
    return (2 * n + 1) * gauss(n) / 3


def answer(n=100):
    return gauss(n) ** 2 - gauss_squares(n)


if __name__ == '__main__':
    print("Answer is:", answer())

