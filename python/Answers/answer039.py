"""
Problem 39:

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


def py_triples(n):
    return sum(a * a + b * b == (n - a - b) ** 2 for a in range(1, n + 1) for b in range(a + 1, n + 1))


def answer(n=1001):
    return max(range(n), key=py_triples)


if __name__ == '__main__':
    print("Answer is:", answer())
