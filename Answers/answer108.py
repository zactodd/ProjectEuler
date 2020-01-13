"""
Question 108:
In the following equation x, y, and n are positive integers.

1x+1y=1n
For n = 4 there are exactly three distinct solutions:

15+12016+11218+18=14=14=14
What is the least value of n for which the number of distinct solutions exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110; it is strongly advised that you solve this one first.
"""

from itertools import count
import math


def count_divisors_squared(n):
    c = 1
    end = math.sqrt(n)
    for i in count(2):
        if i > end:
            break
        elif n % i != 0:
            continue
        for j in count():
            n //= i
            if n % i != 0:
                c *= j * 2 + 1
                break
        end = math.sqrt(n)
    return c * 3 if n != 1 else c


def answer():
    return next((n for n in count(1)  if (count_divisors_squared(n) + 1) // 2 > 1000), None)


if __name__ == '__main__':
    print("Answer is:", answer())
