"""
Question 77:

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""
from utils import SMALL_PRIMES
from itertools import count

def answer():
    limit = 5000
    for t in count(11):
        ways = [1] + [0] * t
        for p in SMALL_PRIMES:
            for i in range(p, t + 1):
                ways[i] += ways[i - p]
        if ways[t] > limit:
            return t


if __name__ == '__main__':
    print("Answer is:", answer())
