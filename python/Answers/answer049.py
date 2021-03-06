"""
Problem 49:
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from python.utils import is_prime, is_perm
from itertools import cycle, accumulate


def is_stepping_prime_perm(n, s):
    a, b = n + s, n + 2 * s
    return is_prime(n) and is_prime(a) and is_prime(b) and is_perm(n, a) and is_perm(n, b)


def answer(s=3330, n=1487):
    return next(int(str(n) + str(n + s) + str(n + 2 * s)) for n in accumulate(cycle((4, 2)), initial=n + 2)
                if is_stepping_prime_perm(n, s))


if __name__ == '__main__':
    print("Answer is:", answer())
