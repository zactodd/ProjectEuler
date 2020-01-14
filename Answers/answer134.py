"""
Question 134:
Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 1219 is the smallest number such that the last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes, p2 > p1, there exist values of n for which the last digits are formed by p1 and n is divisible by p2. Let S be the smallest of these values of n.

Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.
"""
from itertools import count
from utils import fast_primes, reciprocal_mod

import math

def answer():
    limit, s = int(1e6), 0
    primes = fast_primes(2 * limit)
    for i in count(2):
        if (p := int(primes[i])) > limit:
            break
        q, k = int(primes[i + 1]), 10 ** round(math.log10(p))
        m = (q - p) * reciprocal_mod(k % q, q) % q
        s += m * k + p
    return s


if __name__ == '__main__':
    print("Answer is:", answer())
