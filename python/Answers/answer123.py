"""
Problem 123:
Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 109 is 7037.

Find the least value of n for which the remainder first exceeds 10^10.
"""

from python.utils import fast_primes


def answer(limit=10 ** 10):
    primes = [0] + fast_primes(250000)
    return next((n + 2 for n in range(1, len(primes), 2) if 2 * n * primes[n] > limit), None)


if __name__ == '__main__':
    print("Answer is:", answer())
