"""
Problem 120:
Let r be the remainder when (a−1)n + (a+1)n is divided by a2.

For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax.
"""


def answer():
    return sum(i * (i - (2 if i % 2 == 0 else 1)) for i in range(3, 1001))


if __name__ == '__main__':
    print("Answer is:", answer())
