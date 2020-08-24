"""
How many 20 digit numbers n (without any leading zero) exist such that no three consecutive digits of n have a sum greater than 9?
"""


def digit_sum(n):
    return sum(int(c) for c in str(n))


def answer(digits=20, consecutive=3, max_sum=9, base=10):
    inner = base ** consecutive
    ways = [[1] + [0] * (inner - 1)]
    for d in range(1, digits + consecutive + 1):
        ways.append([sum(ways[d - 1][(j := p % (base ** (consecutive - 1)) * base):j + base])
                     if digit_sum(p) <= max_sum else 0 for p in range(inner)])
    return ways[-1][0] - ways[-2][0]


if __name__ == "__main__":
    print("Answer is:", answer())
