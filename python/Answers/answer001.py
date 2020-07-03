"""
Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from python.utils import gauss


def divide_gauss(n, f):
    return f * gauss(n // f)


def answer():
    n = 999
    return divide_gauss(n, 3) + divide_gauss(n, 5) - divide_gauss(n, 15)


if __name__ == '__main__':
    print("Answer is:", answer())
