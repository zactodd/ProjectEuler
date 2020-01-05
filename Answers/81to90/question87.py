"""
Question 87:
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
    limit = 50000000
    p = set()
    for a, b, c in product(fast_primes(7072), fast_primes(369), fast_primes(85)):
        q = a ** 2 + b ** 3 + c ** 4
        if q >= limit:
            continue
        p.add(q)
    return len(p)


if __name__ == '__main__':
    print("Answer is:", answer())
