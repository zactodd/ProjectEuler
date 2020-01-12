"""
Question 168:
Consider the number 142857. We can right-rotate this number by moving the last digit (7) to the front of it, giving us 714285.
It can be verified that 714285=5×142857.
This demonstrates an unusual property of 142857: it is a divisor of its right-rotation.

Find the last 5 digits of the sum of all integers n, 10 < n < 10100, that have this property.
"""


def answer():
    s = 0
    for a in range(1, 100):
        for k in range(1, 10):
            for d in range(1, 10):
                if d * (10 ** a - k) % (10 * k - 1) == 0:
                    c = d * (10 ** a - k) // (10 * k - 1)
                    if 10 ** (a - 1) <= c < 10 ** a:
                        s += 10 * c + d
    return int(str(s)[-5:])


if __name__ == '__main__':
    print("Answer is:", answer())
