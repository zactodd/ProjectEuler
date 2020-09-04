"""
Problem 4:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Solved: O(n^2)
"""
from python.utils import is_palindrome
from itertools import permutations


def answer():
    return max(r for i, j in permutations(range(100, 1000), 2) if is_palindrome(r := i * j))


if __name__ == '__main__':
    print("Answer is:", answer())
