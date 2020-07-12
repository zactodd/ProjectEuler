"""
Problem 108:
In the following equation x, y, and n are positive integers.

1x+1y=1n
For n = 4 there are exactly three distinct solutions:

15+12016+11218+18=14=14=14
What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.
"""

from itertools import count, takewhile
from math import sqrt, prod


def count_divisors_squared(n):
    c = prod(next(j for j in count(1) if (n := (n // i)) % i != 0) * 2 + 1
             for i in takewhile(lambda x: x <= int(sqrt(n)), count(2)) if n % i == 0)
    return c * 3 if n != 1 else c


def answer(limit=1000):
    return next((n for n in count(1) if (count_divisors_squared(n) + 1) // 2 > limit), None)


if __name__ == '__main__':
    print("Answer is:", answer())
