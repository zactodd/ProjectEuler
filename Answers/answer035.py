"""
Problem 35:

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from utils import fast_primes


def circle(n):
    str_n = str(n)
    return [n] + [int(str_n[i:] + str_n[:i]) for i in range(1, len(str(n)))]


def answer():
    n = int(1e6)
    primes = fast_primes(n)
    return sum(all(c in primes for c in circle(p)) for p in primes)


if __name__ == '__main__':
    print("Answer is:", answer())