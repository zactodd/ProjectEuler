"""
Problem 62:
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""
import math
from collections import defaultdict


def answer():
    digits, min_cube = "", float('Inf')
    n, d = 100, 5
    cubes = defaultdict(list)
    while len(digits) <= math.log10(min_cube):
        c = n ** 3
        digits = "".join(sorted(str(c)))
        cubes[digits].append(c)
        if len(cubes[digits]) == d and min_cube > (candidate := cubes[digits][0]):
            min_cube = candidate
        n += 1
    return min_cube


if __name__ == '__main__':
    print("Answer is:", answer())
