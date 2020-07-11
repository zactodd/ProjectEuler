"""
Problem 48:
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def answer(d=10, n=1000):
    return int(str(sum(pow(i, i) for i in range(1, n + 1)))[-d:])


if __name__ == '__main__':
    print("Answer is:", answer())
