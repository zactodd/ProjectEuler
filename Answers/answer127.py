"""
Question 127:
The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32
It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.
"""
import math


def rads(n):
    r = [0] + [1] * (n - 1)
    for i in range(2, len(r)):
        if r[i] == 1:
            for j in range(i, len(r), i):
                r[j] *= i
    return r


def answer():
    limit = 120000

    rs = rads(limit)
    srs = sorted((r, n) for (n, r) in enumerate(rs))[1:]

    s = 0
    for c in range(2, limit):
        for (r, a) in srs:
            r *= rs[c]
            if r >= c:
                break
            b = c - a
            if a < b and r * rs[b] < c and math.gcd(a, b) == 1:
                s += c
    return s


if __name__ == '__main__':
    print("Answer is:", answer())
