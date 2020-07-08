"""
Problem 62:
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""
from collections import defaultdict
from itertools import count


def answer():
    n, d = 100, 5
    cubes = defaultdict(list)
    for n in count(n):
        c = n ** 3
        digits = "".join(sorted(str(c)))
        cubes[digits].append(c)
        if len(cubes[digits]) == d:
            return cubes[digits][0]


if __name__ == '__main__':
    print("Answer is:", answer())
