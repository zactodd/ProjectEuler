"""
Problem 110:
In the following equation x, y, and n are positive integers.

1
x
+
1
y
=
1
n
It can be verified that when n = 1260 there are 113 distinct solutions and this is the least value of n for which the total number of distinct solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions exceeds four million?

NOTE: This problem is a much more difficult version of Problem 108 and as it is well beyond the limitations of a brute force approach it requires a clever implementation.
"""

from functools import reduce
from python.utils import fast_primes


def generator(limit):
    l = [1] * 14
    while l[13] < limit:
        i = 13
        while i > 0 and (l[i] == l[i - 1]):
            l[i] = 1
            i -= 1
        l[i] += 2
        yield l


def answer():
    primes = fast_primes(50)
    mult = lambda x: reduce(lambda y, z: y * z, x, 1)
    translate = lambda x: mult(int(primes[i]) ** ((x[i] - 1) // 2) for i in range(len(x)))
    return min(translate(l) for l in generator(13) if mult(l) > 8000000)


if __name__ == '__main__':
    print("Answer is:", answer())
