"""
Question 80:
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""
from decimal import getcontext, Decimal


def answer():
    getcontext().prec = 102
    limit, d, s = 100, 100, 0
    p = 10 ** (d - 1)
    for i in range(2, limit):
        q = Decimal(i).sqrt()
        s += sum(int(c) for c in str(q * p)[:d]) if q % 1 != 0 else 0
    return s


if __name__ == '__main__':
    print("Answer is:", answer())
