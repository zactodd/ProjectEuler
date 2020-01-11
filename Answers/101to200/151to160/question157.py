from itertools import product

from math import sqrt

from utils import is_prime, fast_primes, factors

N = 9
SMALL_PRIMES = [n for n in range(3, int(sqrt(2 ** N + 5 ** N + 0.5) + 1), 2) if is_prime(n)]


def divisors(n, p0=1):
    if n == 1:
        return 1
    for p in SMALL_PRIMES:
        if p ** 2 > n:
            return 2
        elif p <= p0:
            continue
        if n % p == 0:
            n /= p
            rep = 1
            while n % p == 0:
                n /= p
                rep += 1
            return (rep + 1) * divisors(n, p)
    return 2


def e(n, p):
    counter = 0
    while n % p == 0:
        counter += 1
        n /= p
    return counter


def gen_exp(n):
    for q, r in product(range(n + 1), repeat=2):
        k = 2 ** q
        l = 5 ** r
        yield k, l, n - q + 1, n - r + 1
        if q > 0 and r > 0:
            yield 1, k * l, n - q + 1, n - r + 1


def num_solutions(n):
    c = 0
    for k, l, s, t in gen_exp(n):
        kl = k + l
        ds, dt = e(kl, 2), e(kl, 5)
        s += ds
        t += dt
        kl /= 2 ** ds * 5 ** dt
        c += divisors(kl) * s * t
    return c


def answer():
    return sum(map(num_solutions, range(1, N + 1)))


if __name__ == '__main__':
    print("Answer is:", answer())
