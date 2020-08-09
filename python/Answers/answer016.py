"""
Problem 16:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def answer(p=1000):
    return sum(int(i) for i in str(2 ** p))


if __name__ == '__main__':
    print("Answer is:", answer())
