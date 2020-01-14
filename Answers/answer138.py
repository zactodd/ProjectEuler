"""
Problem 138:

"""

from utils import fast_fib


def answer():
    ns = 12
    return sum(fast_fib(6 * n + 3) // 2 for n in range(1, ns + 1))


if __name__ == '__main__':
    print("Answer is:", answer())
