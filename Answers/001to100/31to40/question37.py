"""
Question 37:

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from utils import fast_primes


def truncates(n):
    str_n = str(n)
    ts = set()
    for i in range(1, len(str(n))):
        ts |= {int(str_n[i:]), int(str_n[:i])}
    return ts


def answer():
    limit = int(1e6)
    s = 0
    count = 0
    primes = fast_primes(limit)
    for p in primes:
        if p > 10 and all(c in primes for c in truncates(p)):
            count += 1
            s += p
        if count == 11:
            break
    return s


if __name__ == '__main__':
    print("Answer is:", answer())
