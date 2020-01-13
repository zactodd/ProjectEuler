"""
Question 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from utils import fast_primes


def answer():
    n = int(2e6)
    return sum(int(p) for p in fast_primes(n))


if __name__ == '__main__':
    print("Answer is:", answer())
