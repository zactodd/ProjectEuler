import math
import random
from queue import Queue
from itertools import count, islice
import numpy as np
import math


SQRT5 = math.sqrt(5)
PHI = (1 + SQRT5) / 2


def fast_fib(n):
    """
    Calualted the nth fibanci number
    :param n:
    :return:
    """
    return round(math.pow(PHI, n) / SQRT5)


def is_prime(n):
    """
    Determines if n is a prime number.
    :param n: The number to check.
    :return:
    """
    if n & 1 == 0:
        return False
    return all(n % d != 0 for d in range(3, int(math.sqrt(n) + 1), 2))


# primes below 1000
SMALL_PRIMES = (2,) + tuple(n for n in range(3, 1000, 2) if is_prime(n))


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


def generate_primes():
    yield 2
    for num in count(3, 2):
        if is_prime(num):
            yield num


def nth_prime(n):
    return next(islice(generate_primes(), n, None))


def fast_primes(n):
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)]


def binomial(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def bin_as_10(n):
    return int(str(bin(n))[2:])


def is_prime_list(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, len(sieve), i):
                sieve[j] = False
    return sieve


def intpow(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    elif (exp & 1) != 0:
        return base * intpow(base * base, exp // 2)
    else:
        return intpow(base * base, exp // 2)


def pell(n):
    m, k, a, b = 1, 1, 1, 0
    while k != 1 or b == 0:
        m = k * (m // k + 1) - m
        m -= int((m - math.sqrt(n)) // k) * k
        a, b = (a + b * m) // abs(k), (a * m + n * b) // abs(k)
        k = (m * m - n) // k
    return a


def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))


def totients(n):
    result = list(range(n + 1))
    for i in range(2, len(result)):
        if result[i] == i:
            for j in range(i, len(result), i):
                result[j] -= result[j] // i
    return result


def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return True


def reciprocal_mod(x, m):
    y = x
    x = m
    a, b = 0, 1
    while y != 0:
        a, b = b, a - x // y * b
        x, y = y, x % y
    return a % m


def is_perfect_square(n):
    root = math.sqrt(n)
    return int(root + 0.5) ** 2 == n


def lambda_feedback(inputs, func, repeat=None, cond=lambda _: True, depth=1):
    return lambda_feedback(func(inputs), func, repeat, depth=depth + 1) \
        if (repeat is None or repeat > depth) and cond(inputs) else inputs


def multinomial(n, k):
    r = math.factorial(n)
    for i in k:
        r //= math.factorial(i)
    return r


def divide_till(s, d, t=0):
    while s > t:
        yield s
        s //= d
