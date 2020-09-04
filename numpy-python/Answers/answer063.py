"""
Problem63:
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


def answer(limit=25):
    return sum(len(str(i ** j)) == j for i in range(1, 10) for j in range(1, limit))


if __name__ == '__main__':
    print("Answer is:", answer())
