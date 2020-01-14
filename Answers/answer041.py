"""
Problem 41:

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from utils import fast_primes
from itertools import permutations


def answer():
    n = int(1e9)
    primes = fast_primes(n)
    return next(candidate for p in permutations("7654321") if (candidate := int("".join(p))) in primes)


if __name__ == '__main__':
    print("Answer is:", answer())

