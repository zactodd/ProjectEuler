"""
Question 27:
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

from utils import fast_primes, is_prime


def answer():
    n = 1000
    max_value = 0
    p = None
    for b in fast_primes(n + 1):
        for a in range(-b + 2, 0, 2):
            n = 1
            while is_prime(abs(n * n + a * n + b)):
                n += 1
            if n > max_value:
                max_value, p = n, a * b
    return p


if __name__ == '__main__':
    print("Answer is:", answer())
