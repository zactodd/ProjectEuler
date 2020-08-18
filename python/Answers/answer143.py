"""
Problem 143:
Let ABC be a triangle with all interior angles being less than 120 degrees. Let X be any point inside the triangle and let XA = p, XC = q, and XB = r.

Fermat challenged Torricelli to find the position of X such that p + q + r was minimised.

Torricelli was able to prove that if equilateral triangles AOB, BNC and AMC are constructed on each side of triangle ABC, the circumscribed circles of AOB, BNC, and AMC will intersect at a single point, T, inside the triangle. Moreover he proved that T, called the Torricelli/Fermat point, minimises p + q + r. Even more remarkable, it can be shown that when the sum is minimised, AN = BM = CO = p + q + r and that AN, BM and CO also intersect at T.


If the sum is minimised and a, b, c, p, q and r are all positive integers we shall call triangle ABC a Torricelli triangle. For example, a = 399, b = 455, c = 511 is an example of a Torricelli triangle, with p + q + r = 784.

Find the sum of all distinct values of p + q + r ≤ 120000 for Torricelli triangles.
"""
import math
from itertools import takewhile, chain


def answer(limit=120000):
    sq_limit = int(math.sqrt(limit))
    pairs = []
    for i in range(1, sq_limit):
        for a, b in takewhile(lambda p: sum(p) <= limit,
                              map(lambda j: (2 * i * j + j ** 2, i ** 2 - j ** 2),
                                  filter(lambda j: (i - j) % 3 != 0 and math.gcd(i, j) == 1, range(1, i)))):
            for k in range(1, math.ceil(limit / (a + b))):
                pairs.extend([(k * a, k * b), (k * b, k * a)])
    pairs.sort()
    index = [None] * limit
    for i, (a, _) in enumerate(pairs):
        if index[a] is None:
            index[a] = i
    s = set()
    for i, (a, b) in enumerate(pairs):
        va = {bj for _, bj in takewhile(lambda p: p[0] == a, map(lambda j: pairs[j], range(index[a], len(pairs))))}
        vb = {bj for _, bj in takewhile(lambda p: p[0] == b, map(lambda j: pairs[j], range(index[b], len(pairs))))}
        s |= {ss for aj in va if aj in vb and (ss := (a + b + aj)) < limit}
    return sum(s)


if __name__ == '__main__':
    print("Answer is:", answer())
