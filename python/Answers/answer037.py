"""
Problem 37:

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Solved: O(n * (log n)^2)
"""
from python.utils import fast_primes
from itertools import islice


def truncates(n):
    ts = set()
    for i in range(1, len(str_n := str(n))):
        ts |= {int(str_n[i:]), int(str_n[:i])}
    return ts


def answer(limit=int(1e6)):
    primes = fast_primes(limit)
    return sum(islice((p for p in primes if p > 10 and all(c in primes for c in truncates(p))), 11))


if __name__ == '__main__':
    print("Answer is:", answer())
