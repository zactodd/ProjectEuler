"""
Problem 179:

Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""
from collections import Counter


def answer(n=10 ** 7):
    ds = Counter(j for i in range(2, (n + 1) // 2) for j in range(i * 2, n, i))
    return sum(ds[i] == ds[i + 1] for i in range(2, n))


if __name__ == "__main__":
    print("Answer is:", answer())
