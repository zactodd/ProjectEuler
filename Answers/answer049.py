"""
Question 49:
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from utils import is_prime


def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))


def answer():
    n, sign = 1487, -1
    while True:
        n += 3 + sign
        sign = -sign
        b, c = n + 3330, n + 6660
        if is_prime(n) and is_prime(b) and is_prime(c) and is_perm(n, b) and is_perm(b, c):
            return int(str(n) + str(b) + str(c))


if __name__ == '__main__':
    print("Answer is:", answer())

