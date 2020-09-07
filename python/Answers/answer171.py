"""
Problem 171:
For a positive integer n, let f(n) be the sum of the squares of the digits (in base 10) of n, e.g.

f(3) = 32 = 9,
f(25) = 22 + 52 = 4 + 25 = 29,
f(442) = 42 + 42 + 22 = 16 + 16 + 4 = 36

Find the last nine digits of the sum of all n, 0 < n < 1020, such that f(n) is a perfect square.
"""


import math


def answer(l=20, b=10, m=10 ** 9):
    max_sqrt_sum = (b - 1) ** 2 * l
    sqsum, c = [[0] * (max_sqrt_sum + 1)], [[1] + [0] * max_sqrt_sum]
    for i in range(1, l + 1):
        sqsum.append([0] * (max_sqrt_sum + 1))
        c.append([0] * (max_sqrt_sum + 1))
        for j in range(b):
            for k, index in enumerate(range(j ** 2, max_sqrt_sum)):
                sqsum[i][index] = (sqsum[i][index] + sqsum[i - 1][k] + pow(b, i - 1, m) * j * c[i - 1][k]) % m
                c[i][index] = (c[i][index] + c[i - 1][k]) % m
    return sum(sqsum[l][i ** 2] for i in range(1, int(math.sqrt(max_sqrt_sum)))) % m


if __name__ == '__main__':
    print("Answer is:", answer())
