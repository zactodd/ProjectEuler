"""
Problem 148:
We can easily verify that none of the entries in the first seven rows of Pascal's triangle are divisible by 7:

 	 	 	 	 	 	 1
 	 	 	 	 	 1	 	 1
 	 	 	 	 1	 	 2	 	 1
 	 	 	 1	 	 3	 	 3	 	 1
 	 	 1	 	 4	 	 6	 	 4	 	 1
 	 1	 	 5	 	10	 	10	 	 5	 	 1
1	 	 6	 	15	 	20	 	15	 	 6	 	 1
However, if we check the first one hundred rows, we will find that only 2361 of the 5050 entries are not divisible by 7.

Find the number of entries which are not divisible by 7 in the first one billion (109) rows of Pascal's triangle.
"""


def int2(n, b):
    ret = []
    while n != 0:
        n, k = divmod(n, b)
        ret.append(k)
    ret.reverse()
    return ret


def f(l, b):
    if not l:
        return 0
    r = l[0]
    if r == 0:
        return f(l[1:], b)
    else:
        s = b * (b + 1) // 2
        return r * (r + 1) // 2 * s ** (len(l) - 1) + (r + 1) * f(l[1:], b)


def answer(m=10 ** 9):
    return f(int2(m, 7), 7)


if __name__ == '__main__':
    print("Answer is:", answer())


