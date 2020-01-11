"""
Question 160:
For any N, let f(N) be the last five digits before the trailing zeroes in N!.
For example,

9! = 362880 so f(9)=36288
10! = 3628800 so f(10)=36288
20! = 2432902008176640000 so f(20)=17664

Find f(1,000,000,000,000)
"""


def fact(n):
    return even_fact(n) * odd_fact(n) % 100000


def even_fact(n):
    return 1 if n == 0 else fact(n // 2)


def odd_fact(n):
    return 1 if n == 0 else odd_fact(n // 5) * fact_co_prime(n) % 100000


def fact_co_prime(n):
    n %= 100000
    product = 1
    for i in range(1, n + 1):
        if i % 2 != 0 and i % 5 != 0:
            product = i * product % 100000
    return product


def count_factors(end, n):
    return 0 if end == 0 else end // n + count_factors(end // n, n)


def answer():
    n = 10 ** 12
    t = count_factors(n, 2) - count_factors(n, 5)
    if t >= 2505:
        t = (t - 5) % 2500 + 5
    return fact(n) * pow(2, t, 100000) % 100000


if __name__ == '__main__':
    print("Answer is:", answer())
