"""
Problem 93:
By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) and brackets/parentheses, it is possible to form different positive integer targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) − 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.
"""
from itertools import combinations, permutations, product
from operator import add, sub, mul, truediv


# TODO make general
def answer(ops=(add, mul, sub, truediv)):
    return int("".join(str(i) for i in max((({x for p in permutations(terms) for o in product(ops, repeat=3)
            for x in (o[0](o[1](p[0], p[1]), o[2](p[2], p[3])), o[0](o[1](o[2](p[0], p[1]), p[2]), p[3]))
                        if x % 1 == 0 and x > 0}, terms) for terms in combinations(range(1, 10), 4)),
               key=lambda x: next(i for i in range(1, 1 + len(x[0])) if i not in x[0]))[1]))


if __name__ == '__main__':
    print("Answer is:", answer())
