"""
Question 164:
How many 20 digit numbers n (without any leading zero) exist such that no three consecutive digits of n have a sum greater than 9?
"""

from itertools import product


def f(n):
    ret = {}
    if n == 2:
        for i, j in product(range(10), range(10)):
            ret[i, j] = int(i>0 and i+j<=9)
        return ret
    for (k, i), v in f(n-1).items():
        for j in range(10-i-k):
            ret.setdefault((i, j), 0)
            ret[i, j] += v
    return ret


def answer():
    n = 20
    return sum(f(n).values())


if __name__ == '__main__':
    print("Answer is:", answer())
