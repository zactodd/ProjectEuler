"""
Problem 73:
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""


def ceil_division(a, b):
    return -(-a // b)


def answer():
    limit = 12000
    n1, n2, d1, d2 = 1, 1, 3, 2
    n = [0] * (limit + 1)
    for d in range(1, limit + 1):
        n[d] += ceil_division(n2 * d, d2) - ceil_division(n1 * d, d1) - 1
        n[2 * d::d] = [k - n[d] for k in n[2 * d::d]]
    return sum(n)


if __name__ == '__main__':
    print("Answer is:", answer())
