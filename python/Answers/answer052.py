"""
Problem 52:
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
from itertools import permutations
from python.utils import is_perm


def answer():
    # More effect with doing check inside 13: nested for
    candidates = [int("".join(p)) for i in range(6, 9) for p in permutations("0123456789", i) if p[0] != "0"]
    return next((c for c in candidates if all(is_perm(c, c * i) for i in range(2, 7))), None)


if __name__ == '__main__':
    print("Answer is:", answer())
