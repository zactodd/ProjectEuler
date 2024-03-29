"""
Problem 14:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

Solved: O(n * CP)
"""
from functools import cache


@cache
def recursive_hailstone(n):
    return 1 if n == 1 else recursive_hailstone(3 * n + 1 if n % 2 else n // 2) + 1


def answer(limit=int(1e6)):
    return max(range(1, limit), key=recursive_hailstone)


if __name__ == '__main__':
    print("Answer is:", answer())
