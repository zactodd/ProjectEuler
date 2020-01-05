"""
Question 66:
onsider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×2^2 = 1
22 – 3×1^2 = 1
92 – 5×4^2 = 1
52 – 6×2^2 = 1
82 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""
from utils import pell
import math


def answer():
    limit = 1000
    max_x = 0
    max_d = 2
    for d in range(2, limit + 1):
        if int(math.sqrt(d)) ** 2 != d:
            x = pell(d)
            if x > max_x:
                max_x, max_d = x, d
    return max_d


if __name__ == '__main__':
    print("Answer is:", answer())
