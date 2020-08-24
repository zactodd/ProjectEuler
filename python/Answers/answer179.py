"""
Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors. For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""


def answer(l=10 ** 7):
    ds = [2] * l
    for i in range(2, (len(ds) + 1) // 2):
        for j in range(i * 2, len(ds), i):
            ds[j] += 1
    return sum(i == j for i, j in zip(ds[2:], ds[3:]))


if __name__ == "__main__":
    print("Answer is:", answer())
