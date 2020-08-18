"""
Problem 141:
A positive integer, n, is divided by d and the quotient and remainder are q and r respectively. In addition d, q, and r are consecutive positive integer terms in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4. It can also be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2).
We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 1022, happen to also be perfect squares.
The sum of all progressive perfect squares below one hundred thousand is 124657.

Find the sum of all progressive perfect squares below one trillion (1012).
"""
from math import gcd
from itertools import count, takewhile
from python.utils import is_perfect_square


def answer(limit=int(1e12)):
    return sum({n for a, a3 in map(lambda i: (i, i ** 3), range(2, 10000))
               for b, b2 in takewhile(lambda x: a3 * x[1] + x[1] < limit, map(lambda i: (i, i ** 2), range(1, a)))
               for n in takewhile(lambda x: x < limit, map(lambda c: a3 * b * c ** 2 + b2 * c, count()))
               if is_perfect_square(n)})


if __name__ == '__main__':
    print("Answer is:", answer())
