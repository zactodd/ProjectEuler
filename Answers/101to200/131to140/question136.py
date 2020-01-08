"""
Question 136:
The positive integers, x, y, and z, are consecutive terms of an arithmetic progression. Given that n is a positive integer, the equation, x2 − y2 − z2 = n, has exactly one solution when n = 20:

132 − 102 − 72 = 20

In fact there are twenty-five values of n below one hundred for which the equation has a unique solution.

How many values of n less than fifty million have exactly one solution?
"""
from utils import fast_primes


def answer():
    n = 50000000
    primes = fast_primes(n)
    c = 0
    for i in range(len(primes)):
        if primes[i] < n / 4:
            c += 1
        if primes[i] < n / 16:
            c += 1
        if (primes[i] - 3) % 4 == 0:
            c += 1
    return c


if __name__ == '__main__':
    print("Answer is:", answer())

