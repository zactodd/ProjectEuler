"""
Problem 141:
A positive integer, n, is divided by d and the quotient and remainder are q and r respectively. In addition d, q, and r are consecutive positive integer terms in a geometric sequence, but not necessarily in that order.

For example, 58 divided by 6 has quotient 9 and remainder 4. It can also be seen that 4, 6, 9 are consecutive terms in a geometric sequence (common ratio 3/2).
We will call such numbers, n, progressive.

Some progressive numbers, such as 9 and 10404 = 1022, happen to also be perfect squares.
The sum of all progressive perfect squares below one hundred thousand is 124657.

Find the sum of all progressive perfect squares below one trillion (1012).
"""
import math
from itertools import count
from python.utils import is_perfect_square


def answer(limit=int(1e12)):
    p_set = set()
    for a in range(2, 10000):
        for b in range(1, a):
            a3, b2 = a ** 3, b ** 2
            if a3 * b2 + b2 >= limit:
                break
            elif math.gcd(a, b) > 1:
                continue
            for c in count():
                if (n := (a3 * b * c ** 2 + b2 * c)) >= limit:
                    break
                elif is_perfect_square(n):
                    p_set.add(n)
    return sum(p_set)


if __name__ == '__main__':
    print("Answer is:", answer())
