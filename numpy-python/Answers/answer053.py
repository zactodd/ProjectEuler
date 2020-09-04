"""
Problem 53:

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (53)=10.

In general, (nr)=n!r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.

It is not until n=23, that a value exceeds one-million: (2310)=1144066.

How many, not necessarily distinct, values of (nr) for 1≤n≤100, are greater than one-million?
"""
from python.utils import binomial


def answer():
    return sum(binomial(n, k) > 1000000 for n in range(1, 101) for k in range(0, n + 1))


if __name__ == '__main__':
    print("Answer is:", answer())
