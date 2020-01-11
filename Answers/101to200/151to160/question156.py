"""
Question156:
Starting from zero the natural numbers are written down in base 10 like this:
0 1 2 3 4 5 6 7 8 9 10 11 12....

Consider the digit d=1. After we write down each number n, we will update the number of ones that have occurred and call this number f(n,1). The first values for f(n,1), then, are as follows:

n	f(n,1)
0	0
1	1
2	1
3	1
4	1
5	1
6	1
7	1
8	1
9	1
10	2
11	4
12	5
Note that f(n,1) never equals 3.
So the first two solutions of the equation f(n,1)=n are n=0 and n=1. The next solution is n=199981.

In the same manner the function f(n,d) gives the total number of digits d that have been written down after the number n has been written.
In fact, for every digit d ≠ 0, 0 is the first solution of the equation f(n,d)=n.

Let s(d) be the sum of all the solutions for which f(n,d)=n.
You are given that s(1)=22786974071.

Find ∑ s(d) for 1 ≤ d ≤ 9.

Note: if, for some n, f(n,d)=n for more than one value of d this value of n is counted again for every value of d for which f(n,d)=n.
"""


def f(n, digit):
    c, factor = 0, 1
    while n // factor != 0:
        lower_number = n - (n // factor) * factor
        curr_number = (n // factor) % 10
        higher_number = n // (factor * 10)
        if curr_number < digit:
            c += higher_number * factor
        elif curr_number == digit:
            c += higher_number * factor + lower_number + 1
        else:
            c += (higher_number + 1) * factor
        factor *= 10
    return c


def f_naive(self, n, digit):
    return sum([self.count_naive(i, digit) for i in range(1, n + 1)])


def count_naive(n, digit):
    count = 0
    while n > 0:
        n, r = divmod(n, 10)
        if r == digit:
            count += 1
    return count


def s(digit):
    found = []

    def binary_search(lower, upper, digit):
        if lower + 1 == upper:
            if f(lower, digit) == lower:
                found.append(lower)
        else:
            middle = (lower + upper) // 2
            l, u, m = f(lower, digit), f(upper, digit), f(middle, digit)
            if m >= lower and middle >= l:
                binary_search(lower, middle, digit)
            if u >= middle and upper >= m:
                binary_search(middle, upper, digit)

    binary_search(1, 10 ** 11, digit)
    return sum(found)


def answer():
    return sum(s(digit) for digit in range(1, 10))


if __name__ == '__main__':
    print("Answer is:", answer())
