"""
Question 104:
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
"""
from utils import is_perm


def is_pandigital(a):
    return is_perm(a, "123456789")


def top(n):
    t = n * 0.20898764024997873 + (-0.3494850021680094)
    return int((pow(10, t - int(t) + 8)))


def answer():
    fn, f0, f1 = 2, 1, 1
    while not is_pandigital(f1) or not is_pandigital(top(fn)):
        f0, f1 = f1, (f1 + f0) % 10 ** 9
        fn += 1
    return fn


if __name__ == '__main__':
    print("Answer is:", answer())
