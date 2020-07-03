"""
Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from python.utils import fast_primes


def answer():
    limit = int(2e6)
    return sum(int(p) for p in fast_primes(limit))


if __name__ == '__main__':
    print("Answer is:", answer())
