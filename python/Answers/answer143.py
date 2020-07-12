"""
Problem 143:
Let ABC be a triangle with all interior angles being less than 120 degrees. Let X be any point inside the triangle and let XA = p, XC = q, and XB = r.

Fermat challenged Torricelli to find the position of X such that p + q + r was minimised.

Torricelli was able to prove that if equilateral triangles AOB, BNC and AMC are constructed on each side of triangle ABC, the circumscribed circles of AOB, BNC, and AMC will intersect at a single point, T, inside the triangle. Moreover he proved that T, called the Torricelli/Fermat point, minimises p + q + r. Even more remarkable, it can be shown that when the sum is minimised, AN = BM = CO = p + q + r and that AN, BM and CO also intersect at T.


If the sum is minimised and a, b, c, p, q and r are all positive integers we shall call triangle ABC a Torricelli triangle. For example, a = 399, b = 455, c = 511 is an example of a Torricelli triangle, with p + q + r = 784.

Find the sum of all distinct values of p + q + r ≤ 120000 for Torricelli triangles.
"""
import math


def answer(limit=120000):
    sq_limit = int(math.sqrt(limit))
    pairs = []
    for i in range(1, sq_limit):
        for j in range(1, i):
            if (i - j) % 3 == 0 or math.gcd(i, j) != 1:
                continue
            a = 2 * i * j + j ** 2
            b = i ** 2 - j ** 2
            if a + b > limit:
                break
            for k in range(1, math.ceil(limit / (a + b))):
                pairs.extend([(k * a, k * b), (k * b, k * a)])
    pairs.sort()
    index = [None] * limit
    sums = [False] * limit
    for i, (a, _) in enumerate(pairs):
        if index[a] is None:
            index[a] = i

    for i in range(len(pairs)):
        a, b = pairs[i]
        va, vb = [], []

        for j in range(index[a], len(pairs)):
            aj, bj = pairs[j]
            if aj != a:
                break
            va.append(bj)

        for j in range(index[b], len(pairs)):
            aj, bj = pairs[j]
            if aj != b:
                break
            vb.append(bj)
        for j in range(len(va)):
            if va[j] in vb and a + b + va[j] < limit:
                sums[a + b + va[j]] = True
    return sum(i for i in range(limit) if sums[i])


if __name__ == '__main__':
    print("Answer is:", answer())
