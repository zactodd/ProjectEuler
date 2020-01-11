"""
Question 153:

"""

import math


def arithmetic_series(lower_bound, upper_bound, step=1):
    return (step + upper_bound) * (upper_bound // step) // 2 - (step + lower_bound) * (lower_bound // step) // 2


def rational_sigma(n):
    rv, i = 0, 1
    while i <= n:
        q = n // i
        min_i = n // (q + 1)
        max_i = n // q
        rv += arithmetic_series(min_i, max_i) * q
        i += (max_i - min_i)
    return rv


def gaussian_sigma(n):
    rv, i = 0, 1
    while 2 * i <= n:
        q = n // (2 * i)
        min_i, max_i = n // (q + 1) - n // (q + 1) % 2, n // q - n // q % 2
        rv += arithmetic_series(min_i, max_i, 2) * q
        i += (max_i - min_i) // 2
    for a in range(1, int(math.sqrt(n))):
        for b in range(a + 1, math.ceil(math.sqrt(n - a ** 2))):
            c = a ** 2 + b ** 2
            if math.gcd(a, b) > 1:
                continue
            i = 1
            while c * i <= n:
                q = n // (c * i)
                min_i, max_i = n // (q + 1) - n // (q + 1) % c, n // q - n // q % c
                rv += arithmetic_series(min_i // c, max_i // c) * q * 2 * (a + b)
                i += (max_i - min_i) // c
    return rv


def answer():
    n = 10 ** 8
    return rational_sigma(n) + gaussian_sigma(n)


if __name__ == '__main__':
    print("Answer is:", answer())
