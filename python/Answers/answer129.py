"""
Problem 129:
A number consisting entirely of ones is called a repunit. We shall define R(k) to be a repunit of length k; for example, R(6) = 111111.

Given that n is a positive integer and GCD(n, 10) = 1, it can be shown that there always exists a value, k, for which R(k) is divisible by n, and let A(n) be the least such value of k; for example, A(7) = 6 and A(41) = 5.

The least value of n for which A(n) first exceeds ten is 17.

Find the least value of n for which A(n) first exceeds one-million.
"""
from itertools import count


def least_divisible(n):
    if n % 2 == 0 or n % 5 == 0:
        return 0
    k, s, p = 1, 1, 1
    while s % n != 0:
        k += 1
        p = p * 10 % n
        s = (s + p) % n
    return k


def answer(limit=10 ** 6):
    return next((n for n in count(limit) if least_divisible(n) > limit), None)


if __name__ == '__main__':
    print("Answer is:", answer())
