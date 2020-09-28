"""
Problem 172:
How many 18-digit numbers n (without leading zeros) are there such that no digit occurs more than three times in n?
"""
import math
from collections import Counter


def count_ways(freqs, l, b):
    histogram = Counter()
    for x in freqs:
        histogram[x] += 1
    ways = math.factorial(b)
    for x in histogram.values():
        ways //= math.factorial(x)
    ways *= math.factorial(l)
    for x in freqs:
        ways //= math.factorial(x)
    return ways


def partitions(s, m, terms, l, b):
    if len(terms) == b:
        return count_ways(terms, l, b) if s == 0 else 0
    else:
        return sum(partitions(s - i, i, terms + [i], l, b) for i in reversed(range(min(m, s) + 1)))


def answer(l=18, b=10, max_count=3):
    return partitions(l, max_count, [], l, b) * (b - 1) // b


if __name__ == '__main__':
    print("Answer is:", answer())
