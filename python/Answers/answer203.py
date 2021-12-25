
from python.utils import binomial, fast_primes
import math


def answer():
    numbers = {binomial(n, k) for n in range(51) for k in range(n + 1)}
    ps = [p * p for p in fast_primes(int(math.sqrt(max(numbers))) + 1)]
    return sum(n for n in numbers if next((b for p in ps if (b := (p > n)) or n % p == (b := 0)), True))
