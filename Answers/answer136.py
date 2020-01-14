"""
Question 136:
The positive integers, x, y, and z, are consecutive terms of an arithmetic progression. Given that n is a positive integer, the equation, x2 − y2 − z2 = n, has exactly one solution when n = 20:

132 − 102 − 72 = 20

In fact there are twenty-five values of n below one hundred for which the equation has a unique solution.

How many values of n less than fifty million have exactly one solution?
"""
from utils import fast_primes


def answer():
    limit = int(5e7)
    return sum((p < limit / 4) + (p < limit / 16) + ((p - 3) % 4 == 0) for p in fast_primes(limit))


if __name__ == '__main__':
    print("Answer is:", answer())

