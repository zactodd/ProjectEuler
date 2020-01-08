"""
Question 137:
Consider the infinite polynomial series AF(x)=xF1+x2F2+x3F3+…, where Fk is the kth term in the Fibonacci sequence: 1,1,2,3,5,8,…; that is, Fk=Fk−1+Fk−2, F1=1 and F2=1.

For this problem we shall be interested in values of x for which AF(x) is a positive integer.

Surprisingly	AF(12)=(12)×1+(12)2×1+(12)3×2+(12)4×3+(12)5×5+⋯=12+14+28+316+532+⋯=2
The corresponding values of x for the first five natural numbers are shown below.

x	AF(x)
2–√−1	1
12	2
13√−23	3
89√−58	4
34√−35	5
We shall call AF(x) a golden nugget if x is rational, because they become increasingly rarer; for example, the 10th golden nugget is 74049690.

Find the 15th golden nugget.
"""

from utils import fast_fib


def answer():
    n = 15
    return fast_fib(2*n) * fast_fib(2*n+1)


if __name__ == '__main__':
    print("Answer is:", answer())
