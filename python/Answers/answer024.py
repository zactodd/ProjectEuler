"""
Problem 24;
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Solved: O(1), limit occurs on the permutation which is O(n!) but is the same list each time.
"""

from itertools import permutations


def answer(n=int(1e6)):
    return "".join(list(permutations("0123456789", 9))[n - 1])


if __name__ == '__main__':
    print("Answer is:", answer())
