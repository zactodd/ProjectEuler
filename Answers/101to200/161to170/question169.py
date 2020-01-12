"""
Question 169:
Define f(0)=1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers of 2 using each power no more than twice.

For example, f(10)=5 since there are five different ways to express 10:

1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8

What is f(1025)?
"""


def answer():
    n = 10 ** 25
    f = {0: 1, 1: 1}

    def recur(n):
        if n in f:
            return f[n]
        if n % 2:
            val = recur(n // 2)
        else:
            val = recur(n // 2) + recur(n // 2 - 1)
        f[n] = val
        return val

    return recur(n)


if __name__ == '__main__':
    print("Answer is:", answer())
