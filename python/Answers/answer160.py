from functools import reduce


def fact(n):
    return even_fact(n) * odd_fact(n) % 100000


def even_fact(n):
    return fact(n // 2) if n else 1


def odd_fact(n):
    return odd_fact(n // 5) * fact_coprime(n) % 100000 if n else 1


def fact_coprime(n):
    return reduce(lambda i, p: i * p % 100000, filter(lambda i: i % 2 != 0 and i % 5 != 0, range(1, n % 100000 + 1)), 1)


def count_factors(end, n):
    return end // n + count_factors(end // n, n) if end else 0


def answer(n=10 ** 12):
    twos = count_factors(n, 2) - count_factors(n, 5)
    return fact(n) * pow(2, twos if twos < 2505 else (twos - 5) % 2500 + 5, 100000) % 100000
