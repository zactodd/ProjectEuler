"""
Problem 140:
Consider the infinite polynomial series AG(x)=xG1+x2G2+x3G3+⋯, where Gk is the kth term of the second order recurrence relation Gk=Gk−1+Gk−2, G1=1 and G2=4; that is, 1,4,5,9,14,23,… .

For this problem we shall be concerned with values of x for which AG(x) is a positive integer.

The corresponding values of x for the first five natural numbers are shown below.

x	AG(x)
5√−14	1
25	2
22√−26	3
137√−514	4
12	5
We shall call AG(x) a golden nugget if x is rational, because they become increasingly rarer; for example, the 20th golden nugget is 211345365.

Find the sum of the first thirty golden nuggets.
"""
from utils import  SQRT5


def answer():
    limit, f = 30, [7, 14, 50, 97]
    for i in range(limit - 4):
        f.append(7 * f[-2] - f[-4])
    return sum(int(x / SQRT5) - 1 for x in f)


if __name__ == '__main__':
    print("Answer is:", answer())
