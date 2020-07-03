"""
Problem 47:

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

"""


def answer():
    limit = int(1e7)
    n = 4
    limit += n
    fs = [0] * limit
    c = 0
    for i in range(2, limit):
        if fs[i] == n:
            c += 1
            if c == n:
                return i - n + 1
        elif fs[i] == (c := 0):
            fs[i::i] = [x + 1 for x in fs[i::i]]
    return n


if __name__ == '__main__':
    print("Answer is:", answer())


