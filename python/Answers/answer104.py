"""
Problem 104:
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.
"""
from python.utils import is_pandigital, generate_fib


def top(n):
    t = n * 0.20898764024997873 - 0.3494850021680094
    return int((pow(10, t - int(t) + 8)))


def answer():
    return next(i for i, f in enumerate(generate_fib(1), 1) if is_pandigital(f) and is_pandigital(top(i)))


if __name__ == '__main__':
    print("Answer is:", answer())
