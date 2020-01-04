import math
import random
from queue import Queue



SQRT5 = math.sqrt(5)
PHI = (1 + SQRT5) / 2


def fast_fib(n):
    return round(math.pow(PHI, n) / SQRT5)


def isprime(n):
    if n & 1 == 0:
        return False
    d = 3
    sq_n = math.sqrt(n)
    while d <= sq_n:
        if n % d == 0:
            return False
        d += 2
    return True


# primes below 1000
SMALL_PRIMES = (2,) + tuple(n for n in range(3, 1000, 2) if isprime(n))


def rabin_miller(p):
    if p < 2 or p != 2 and p % 2 == 0:
        return False
    s = int(p - 1)
    while s % 2 == 0:
        s >>= 1
    for i in range(10):
        a = random.randrange(p - 1) + 1
        temp = s
        mod = pow(a, temp, int(p))
        while temp != p - 1 and mod != 1 and mod != p - 1:
            mod = (mod * mod) % p
            temp = temp * 2
        if mod != p - 1 and temp % 2 == 0:
            return False
    return True


def brent(n):
    if n % 2 == 0:
        return 2
    x, c, m = random.randrange(0, n), random.randrange(1, n), random.randrange(1, n)
    y, r, q = x, 1, 1
    g, ys = 0, 0
    while g <= 1:
        x = y
        for i in range(r):
            y, k = (y * y + c) % n, 0
        while k < r or g <= 1:
            ys = y
            for i in range(min(m, r - k)):
                y, q = (y * y + c) % n, q * abs(x - y) % n
            g, k = math.gcd(q, n), k + m
        r = 2 * r
    if g == n:
        while g <= 1:
            ys, g = (x * x + c) % n, math.gcd(abs(x - ys), n)
    return g


def pollard(n):
    if n % 2 == 0:
        return 2
    x = random.randrange(2, 1000000)
    c = random.randrange(2, 1000000)
    y = x
    d = 1
    while d == 1 or d == n:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = math.gcd(int(x - y), int(n))
    return d


def factors(n):
    q1 = Queue()
    q2 = []
    q1.put(n)
    while not q1.empty():
        l = q1.get()
        if rabin_miller(l):
            q2.append(l)
            continue
        d = pollard(l)
        if d == l:
            q1.put(l)
        else:
            q1.put(d)
            q1.put(l / d)
    return q2


def gauss(n):
    return n * (n + 1) // 2
