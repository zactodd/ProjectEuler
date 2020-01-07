"""
Question 39:

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


def py_triples(n):
    count = 0
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            c = n - a - b
            if a * a + b * b == c * c:
                count += 1
    return count


def answer():
    return max(range(1001), key=py_triples)


if __name__ == '__main__':
    print("Answer is:", answer())
