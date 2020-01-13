"""
Question 40:

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""


def answer():
    limit = int(1e6)
    c = "".join(str(i) for i in range(1, limit))
    prod = 1
    for i in range(6):
        prod *= int(c[10 ** i - 1])
    return prod


if __name__ == '__main__':
    print("Answer is:", answer())

