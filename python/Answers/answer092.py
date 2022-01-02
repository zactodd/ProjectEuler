"""
Problem 92:
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

from collections import Counter
from python.utils import multinomial
from functools import cache
import math


def sq_digits(n):
    n *= 10
    return sum((((n := n // 10) % 10) ** 2 for _ in range(int(math.log10(n)))))


@cache
def partitions(n, k, v):
    if n == 0:
        return [Counter()]
    elif k == 0 or len(v) == 0 or n < v[0]:
        return []
    pp = [p.copy() for p in partitions(n - v[0], k - 1, v)]
    for p in pp:
        p[v[0]] += 1
    return pp + partitions(n, k, v[1:])


def num_count(counts, min_digits, max_digits):
    counts_sum = sum(counts)
    return sum(
        multinomial(digits - 1, tuple(sorted(counts[:i] + (d - 1,) + counts[i + 1:] + (digits - counts_sum,))))
        for digits in range(max(min_digits, counts_sum), max_digits + 1) for i, d in enumerate(counts)
    )


def answer(limit=10 ** 7):
    md = len(str(limit - 1))
    sl = md * 9 ** 2 + 1
    arrive = [None] * sl
    arrive[1], arrive[89] = 1, 89
    for n in range(2, sl):
        chain = []
        while not arrive[n]:
            chain.append(n)
            n = sq_digits(n)
        dest = arrive[n]
        for term in chain:
            arrive[term] = dest
    sqs = tuple(i ** 2 for i in range(1, 10))
    return sum(sum(num_count(tuple(sorted(p.values())), 1, md) for p in partitions(n, md, sqs))
               for n in range(2, sl) if arrive[n] == 89)


if __name__ == '__main__':
    print("Answer is:", answer())
