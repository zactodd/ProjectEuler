"""
Problem 87:
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 23 + 24
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""
from itertools import product
from utils import fast_primes


def answer():
    limit = int(5e7)
    return len({q for a, b, c in product(fast_primes(7072), fast_primes(369), fast_primes(85))
               if (q := (a ** 2 + b ** 3 + c ** 4)) < limit})


if __name__ == '__main__':
    print("Answer is:", answer())
