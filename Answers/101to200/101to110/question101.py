"""
Question 101:

"""


def u(n):
    return sum(n ** i * (1 if i % 2 == 0 else -1) for i in range(11))


def tld(x):
    return [x[i] - x[i - 1] for i in range(1, len(x))]


def answer():
    k = 10
    seq = [list(map(u, range(1, k + 1)))]
    for i in range(k):
        seq += [tld(seq[-1])]
    return sum(sum(seq, []))


if __name__ == '__main__':
    print("Answer is:", answer())
