"""
Problem 39:

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
from itertools import combinations


def answer(n=1001):
    return max(range(n), key=lambda x: sum(a * a + b * b == (n - a - b) ** 2 for a, b in combinations(range(1, x), 2)))


if __name__ == '__main__':
    print("Answer is:", answer())
