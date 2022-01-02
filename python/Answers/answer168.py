"""
Problem 168:
Consider the number 142857. We can right-rotate this number by moving the last digit (7) to the front of it, giving us 714285.
It can be verified that 714285=5×142857.
This demonstrates an unusual property of 142857: it is a divisor of its right-rotation.

Find the last 5 digits of the sum of all integers n, 10 < n < 10100, that have this property.
"""


def answer(m=10 ** 5):
    return sum(10 * x + y for k in range(1, 100) for d in range(1, 10)
               for y, (x, r) in map(lambda y: (y, divmod((10 ** k - d) * y, 10 * d - 1)), range(1, 10))
               if r == 0 and x >= 10 ** (k - 1)) % m


if __name__ == "__main__":
    print("Answer is:", answer())
