"""
Problem 80:
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""
from decimal import getcontext, Decimal


def answer(limit=100, d=100):
    getcontext().prec = d + 2
    p = 10 ** (d - 1)
    return sum(sum(int(c) for c in str(q * p)[:d]) for q in map(lambda i: Decimal(i).sqrt(), (2, limit)) if q % 1 != 0)


if __name__ == '__main__':
    print("Answer is:", answer())

